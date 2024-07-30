from rest_framework import serializers
from .models import Customers, Purchases

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchases
        exclude = ['customer']
        

class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customers
        exclude = ['id']
        
    def create(self, validated_data):
        purchase_data = validated_data.pop('purchases')
        customer = Customers.objects.create(**validated_data)
        for purchase in purchase_data:
            purchase['customer'] = customer
            Purchases.objects.create(**purchase)
        return customer