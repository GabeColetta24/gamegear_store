from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .models import Order, OrderItem
from .forms import OrderForm


# Checkout view
# Handles customer checkout and order creation
def checkout(request):

    cart = request.session.get('cart', {})

    # Redirect user if cart is empty
    if not cart:
        return redirect('home')

    total = 0
    cart_items = []

    # Build cart data
    for product_id, quantity in cart.items():

        product = Product.objects.get(id=product_id)

        subtotal = product.price * quantity
        total += subtotal

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    # Handle form submission
    if request.method == 'POST':

        form = OrderForm(request.POST)

        # Check if form is valid
        if form.is_valid():

            order = form.save(commit=False)

            # Link logged in user if authenticated
            if request.user.is_authenticated:
                order.user = request.user

            order.total = total
            order.save()

            # Create order items
            for item in cart_items:

                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                    subtotal=item['subtotal'],
                )

            # Clear cart after successful order
            request.session['cart'] = {}

            return redirect('order_success', order_id=order.id)

    else:
        form = OrderForm()

    context = {
        'form': form,
        'cart_items': cart_items,
        'total': total,
    }

    return render(request, 'checkout/checkout.html', context)

# Order success view
# Displays confirmation after an order has been placed
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    context = {
        'order': order,
    }

    return render(request, 'checkout/order_success.html', context)