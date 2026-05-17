from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product


# View cart page
# Displays all products currently in the shopping cart
def view_cart(request):

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0

    # Loop through cart items
    for product_id, quantity in cart.items():

        product = get_object_or_404(Product, id=product_id)

        subtotal = product.price * quantity
        total += subtotal

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    context = {
        'cart_items': cart_items,
        'total': total,
    }

    return render(request, 'cart/cart.html', context)


# Add product to cart
def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    # Increase quantity if item already exists in cart
    if product_id in cart:
        cart[product_id] += 1

    # Add new item to cart
    else:
        cart[product_id] = 1

    request.session['cart'] = cart

    return redirect('view_cart')

# Remove product from cart
def remove_from_cart(request, product_id):

    # Get cart from session
    cart = request.session.get('cart', {})

    # Remove product if it exists
    if str(product_id) in cart:
        del cart[str(product_id)]

    # Save updated cart
    request.session['cart'] = cart

    return redirect('view_cart')