from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')
    sku = models.CharField(max_length=50, unique=True)
    barcode = models.CharField(
        max_length=100, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.sku})"


class Stock(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='stock')
    quantity = models.IntegerField(
        default=0, validators=[MinValueValidator(0)])
    last_updated = models.DateTimeField(default=timezone.now)
    reorder_level = models.IntegerField(
        default=10, validators=[MinValueValidator(0)])
    reorder_quantity = models.IntegerField(
        default=20, validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.product.name} - {self.quantity} units"

    def needs_reorder(self):
        return self.quantity <= self.reorder_level
