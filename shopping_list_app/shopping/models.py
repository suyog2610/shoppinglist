from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ShoppingList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name
