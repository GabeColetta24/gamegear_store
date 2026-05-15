from django.db import models


# Product model
# Stores each item available to buy in the shop
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    # Shows the product name in the Django admin panel
    def __str__(self):
        return self.name