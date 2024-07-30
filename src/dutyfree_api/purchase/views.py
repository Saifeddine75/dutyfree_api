from django.shortcuts import render
from rest_framework import viewsets
from .models import Customers
from .serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer