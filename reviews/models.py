from django.db import models
from django.contrib.auth.models import User

from products.models import Product


# Review model
# Allows logged-in users to leave feedback on products
class Review(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Shows useful review information in the admin panel
    def __str__(self):
        return f"{self.product.name} review by {self.user.username}"