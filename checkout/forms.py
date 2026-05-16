from django import forms
from .models import Order


# Checkout form
# Allows users to enter delivery information
class OrderForm(forms.ModelForm):

    class Meta:
        model = Order

        fields = [
            'full_name',
            'email',
            'address',
        ]