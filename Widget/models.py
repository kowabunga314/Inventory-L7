from django.core.validators import MinValueValidator
from django.db import models


"""
This file contains the table definitions for the inventory system. Changes in this file must be applied using the 
commands 'python manage.py makemigrations' and 'python manage.py migrate'.
"""


class Supplier(models.Model):
    name = models.CharField(null=False, blank=False, unique=True, max_length=64)


class Warehouse(models.Model):
    name = models.CharField(null=False, blank=False, unique=True, max_length=3)


class Widget(models.Model):
    widget = models.CharField(null=False, blank=False, unique=True, max_length=64)
    supplier = models.ForeignKey(to=Supplier, on_delete=models.CASCADE, to_field='name')
    cost = models.DecimalField(null=False, max_digits=6, decimal_places=2)
    warehouse = models.ForeignKey(to=Warehouse, on_delete=models.CASCADE, to_field='name')
    quantity = models.IntegerField(null=False, validators=[MinValueValidator(0)])
    minimum_quantity = models.IntegerField(null=False, validators=[MinValueValidator(0)])


class Packaging(models.Model):
    widget = models.ForeignKey(to=Widget, on_delete=models.CASCADE, to_field='widget')
    type = models.CharField(null=False, blank=False, max_length=64)
    size = models.IntegerField(null=False, validators=[MinValueValidator(1)])


class Customer(models.Model):
    name = models.CharField(null=False, blank=False, unique=True, max_length=64)


class Sales(models.Model):
    packaging = models.ForeignKey(to=Packaging, on_delete=models.CASCADE)
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE, to_field='name')
    price = models.DecimalField(null=False, max_digits=6, decimal_places=2)
