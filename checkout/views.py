from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.urls import reverse
import stripe

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

    # Configure Stripe secret key
    stripe.api_key = settings.STRIPE_SECRET_KEY

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
            line_items = []

            for item in cart_items:

                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                    subtotal=item['subtotal'],
                )

                # Stripe line item data
                line_items.append({
                    'price_data': {
                        'currency': 'gbp',
                        'product_data': {
                            'name': item['product'].name,
                        },
                        'unit_amount': int(item['product'].price * 100),
                    },
                    'quantity': item['quantity'],
                })

            # Create Stripe checkout session
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=line_items,
                mode='payment',

                success_url=request.build_absolute_uri(
                    reverse('order_success', args=[order.id])
                ),

                cancel_url=request.build_absolute_uri(
                    reverse('view_cart')
                ),
            )

            # Clear cart after successful order
            request.session['cart'] = {}

            return redirect(checkout_session.url)

    else:
        form = OrderForm()

    context = {
        'form': form,
        'cart_items': cart_items,
        'total': total,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
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