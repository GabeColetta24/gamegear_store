from django.contrib import admin
from .models import Product


# Register Product model so products can be added and edited in admin
admin.site.register(Product)