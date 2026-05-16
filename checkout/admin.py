from django.contrib import admin
from .models import Order, OrderItem


# Register checkout models in admin panel
admin.site.register(Order)
admin.site.register(OrderItem)