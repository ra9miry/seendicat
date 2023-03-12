from django.db import models
from ecommerce.apps.catalog.models import Product

class Order(models.Model):
    full_name = models.CharField(max_length=75)
    email = models.EmailField(max_length=40)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=120)    
    phone = models.CharField(max_length=10)
    total = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Тапсырыс"
        verbose_name_plural = "Тапсырыстар"
        ordering = ("-created",)

    def __str__(self):
        return str(self.created)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="order_items", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Тапсырыс тауары"
        verbose_name_plural = "Тапсырыс тауарлары"


    def __str__(self):
        return f"{self.id} - {self.order.full_name}"

