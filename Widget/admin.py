from django.contrib import admin
from .models import Widget


@admin.register(Widget)
class WidgetAdmin(admin.ModelAdmin):
    fields = ['widget', 'packaging', 'customer', 'price', 'supplier',
              'cost', 'warehouse', 'quantity', 'minimum_quantity']
    list_display = ('widget', 'packaging', 'customer', 'price', 'supplier',
                    'cost', 'warehouse', 'quantity', 'minimum_quantity')
