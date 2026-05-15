from django.shortcuts import render
from .models import Product


# Homepage view
# Displays all active products on the homepage
def home(request):

    # Get all active products from database
    products = Product.objects.filter(is_active=True)

    context = {
        'products': products,
    }

    return render(request, 'products/home.html', context)