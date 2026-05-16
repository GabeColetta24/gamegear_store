from django.urls import path
from .views import checkout


# Checkout app URL patterns
urlpatterns = [
    path('', checkout, name='checkout'),
]