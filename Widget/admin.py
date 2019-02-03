from django.contrib import admin
from .models import Supplier, Warehouse, Widget, Packaging, Customer, Sales


"""
This file defines how each model is displayed on the admin and browsable API pages.
"""


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']


@admin.register(Widget)
class WidgetAdmin(admin.ModelAdmin):
    fields = ['widget', 'supplier', 'cost', 'warehouse', 'quantity', 'minimum_quantity']
    list_display = ('widget', 'supplier', 'cost', 'warehouse', 'quantity', 'minimum_quantity')


@admin.register(Packaging)
class PackagingAdmin(admin.ModelAdmin):
    fields = ['widget', 'type', 'size']
    list_display = ('widget', 'type', 'size')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']


@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    fields = ['packaging', 'customer', 'price']
    list_display = ('packaging', 'customer', 'price')
