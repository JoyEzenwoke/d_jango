# ecommerce\products\models.py

from django.db import models
from cloudinary.models import CloudinaryField

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = CloudinaryField('image', blank=True, null=True)

    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    discount = models.PositiveIntegerField(blank=True, null=True)  # e.g. 20 (%)
    rate = models.FloatField(default=0)  # rating like 4.5

    category = models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name