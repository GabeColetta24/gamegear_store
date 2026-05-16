from django.urls import path
from .views import checkout, order_success


# Checkout app URL patterns
urlpatterns = [
    path('', checkout, name='checkout'),
    path('success/<int:order_id>/', order_success, name='order_success'),
]