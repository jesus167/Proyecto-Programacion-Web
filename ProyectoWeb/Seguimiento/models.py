from django.db import models
from Tienda.models import Producto

# Create your models here.


class Order(models.Model):
    num_order = models.CharField(max_length=10, null=True, blank=True)
    cliente = models.CharField(max_length= 200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.num_order

class OrderDetail(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cant = models.IntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.producto