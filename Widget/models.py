from django.core.validators import MinValueValidator
from django.db import models


class Widget(models.Model):
    widget = models.CharField(null=False, blank=False, max_length=64)
    packaging = models.CharField(null=False, blank=False, max_length=64)
    customer = models.CharField(null=False, blank=False, max_length=64)
    price = models.DecimalField(null=False, max_digits=6, decimal_places=2)
    supplier = models.CharField(null=False, blank=False, max_length=64)
    cost = models.DecimalField(null=False, max_digits=6, decimal_places=2)
    warehouse = models.CharField(null=False, blank=False, max_length=64)
    quantity = models.IntegerField(null=False, validators=[MinValueValidator(0)])
    minimum_quantity = models.IntegerField(null=False, validators=[MinValueValidator(0)])
