from datetime import datetime
from rest_framework import serializers
from .models import Customers, Purchases

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchases
        fields = ['product_id', 'price', 'currency', 'quantity', 'purchased_at']

class CustomerSerializer(serializers.ModelSerializer):
    purchases = PurchaseSerializer(many=True)

    class Meta:
        model = Customers
        fields = ['salutation', 'title', 'lastname', 'firstname', 'email', 'purchases', 'postal_code', 'city']

    def create(self, validated_data):
        print("validated_data", validated_data)
        purchases_data = validated_data.pop('purchases')
        print("purchases_data", purchases_data)
        salutation = validated_data.get('salutation')
        if salutation == 'Mrs':
            validated_data['title'] = 1
        elif salutation == 'Mr':
            validated_data['title'] = 2
        customer = Customers.objects.create(**validated_data,)
        for purchase_data in purchases_data:
            Purchases.objects.create(customer=customer, **purchase_data)
        return customer
