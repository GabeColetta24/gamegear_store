from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from products.models import Product
from .models import WishlistItem


# Display the logged-in user's wishlist
@login_required
def view_wishlist(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)

    return render(
        request,
        'wishlist/wishlist.html',
        {
            'wishlist_items': wishlist_items,
        }
    )


# Add a product to the logged-in user's wishlist
@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    WishlistItem.objects.get_or_create(
        user=request.user,
        product=product,
    )

    return redirect('product_detail', product.id)


# Remove a product from the logged-in user's wishlist
@login_required
def remove_from_wishlist(request, item_id):
    wishlist_item = get_object_or_404(
        WishlistItem,
        id=item_id,
        user=request.user,
    )

    wishlist_item.delete()

    return redirect('view_wishlist')