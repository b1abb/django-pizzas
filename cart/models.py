from django.db import models
from pizzastore.models import Pizza
# Create your models here.

class Cart(models.Model):
    cart_session = models.CharField(max_length=250)
    add_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.cart_session


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField()


