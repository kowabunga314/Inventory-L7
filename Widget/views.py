from django.shortcuts import render
from rest_framework import viewsets
from .models import Supplier, Warehouse, Widget, Packaging, Customer, Sales
from .serializers import SupplierSerializer, WarehouseSerializer, WidgetSerializer, PackagingSerializer, \
    CustomerSerializer, SalesSerializer, FullDetailSerializer


"""
This file contains the viewsets that provide CRUD functions to each model in the database. Django REST Framework uses 
these definitions along with those of the models and serializers to generate views for creating, viewing, summarizing, 
updating, and deleting database records.
"""


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class WidgetViewSet(viewsets.ModelViewSet):
    queryset = Widget.objects.all()
    serializer_class = WidgetSerializer


class PackagingViewSet(viewsets.ModelViewSet):
    queryset = Packaging.objects.all()
    serializer_class = PackagingSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer


class FullDetailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = FullDetailSerializer


def table(request):
    """
    This view allows Django to display inventory data in the form of a table within an HTML page.
    :param request: Request made by user's browser
    :return: A rendering of the table.html page
    """
    sales = Sales.objects.all()[:50]
    return render(request, 'table.html', {'sales': sales})
