from rest_framework import serializers
from .models import Supplier, Warehouse, Widget, Packaging, Customer, Sales


"""
This file contains the serializers that allow the model viewsets to function. The viewsets are used in both the 
RESTful API as well as the browsable API interface.
"""


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = '__all__'


class WarehouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warehouse
        fields = '__all__'


class WidgetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Widget
        fields = '__all__'


class PackagingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Packaging
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'


class SalesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sales
        fields = '__all__'


# Serializers for use with the read-only view set
class WidgetDetailSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(many=False, read_only=True)
    warehouse = WarehouseSerializer(many=False, read_only=True)

    class Meta:
        model = Widget
        fields = '__all__'


class PackagingDetailSerializer(serializers.ModelSerializer):
    widget = WidgetDetailSerializer(many=False, read_only=True)

    class Meta:
        model = Packaging
        fields = '__all__'


class FullDetailSerializer(serializers.ModelSerializer):
    packaging = PackagingDetailSerializer(many=False, read_only=True)
    customer = CustomerSerializer(many=False, read_only=True)

    class Meta:
        model = Sales
        fields = '__all__'

