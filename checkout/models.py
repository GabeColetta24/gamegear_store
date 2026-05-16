from django.db import models
from django.contrib.auth.models import User


# Order model
# Stores customer order information
class Order(models.Model):

    # Link order to logged in user
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    total = models.DecimalField(max_digits=10, decimal_places=2)

    # Shows useful order information in admin panel
    def __str__(self):
        return f"Order {self.id}"


# Order item model
# Stores individual products within an order
class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )

    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField(default=1)

    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    # Shows order item information in admin panel
    def __str__(self):
        return f"{self.product.name} - Order {self.order.id}"