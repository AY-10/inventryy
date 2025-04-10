from django.db import models
from django.core.validators import MinValueValidator
from inventory.models import Product


class Store(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class StoreInventory(models.Model):
    store = models.ForeignKey(
        Store, on_delete=models.CASCADE, related_name='inventory')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='store_inventory')
    quantity = models.IntegerField(
        default=0, validators=[MinValueValidator(0)])
    last_updated = models.DateTimeField(auto_now=True)
    reorder_level = models.IntegerField(
        default=10, validators=[MinValueValidator(0)])
    reorder_quantity = models.IntegerField(
        default=20, validators=[MinValueValidator(0)])

    class Meta:
        unique_together = ('store', 'product')
        verbose_name_plural = "Store Inventories"

    def __str__(self):
        return f"{self.store.name} - {self.product.name} ({self.quantity})"

    def needs_reorder(self):
        return self.quantity <= self.reorder_level
