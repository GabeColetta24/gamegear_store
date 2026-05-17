from django.shortcuts import render, get_object_or_404, redirect

from .models import Product
from .forms import UserRegisterForm

# Homepage view
# Displays all active products on the homepage
def home(request):

    # Get all active products from database
    products = Product.objects.filter(is_active=True)

    context = {
        'products': products,
    }

    return render(request, 'products/home.html', context)

# Product detail view
# Displays full information for one selected product
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_active=True)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

# Register view
# Allows new users to create an account
def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'products/register.html', context)