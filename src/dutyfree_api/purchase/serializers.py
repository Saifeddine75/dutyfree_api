from rest_framework import serializers
from .models import Customers, Purchases

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchases
        fields = ['product_id', 'price', 'currency', 'quantity', 'purchased_at']
        

class CustomerSerializer(serializers.ModelSerializer):
    # purchased_at = serializers.DateField(format='%Y-%m-%d', input_formats=['%Y-%m-%d'])
    salutation = serializers.CharField(source='title')
    purchases = PurchaseSerializer(many=True)
    
    class Meta:
        model = Customers
        fields = ['salutation', 'last_name', 'first_name', 'email', 'purchases']
        
        
    def create(self, validated_data):
        print("validated_data", validated_data)
        salutation = validated_data.get('salutation')
        if salutation == 'Mrs':
            validated_data['title'] = 1
        elif salutation == 'Mr':
            validated_data['title'] = 2
        
        purchases_data = validated_data.pop('purchases')
        customer = Customers.objects.create(**validated_data)
        
        for purchase_data in purchases_data:
            Purchases.objects.create(customer=customer, **purchase_data)
        return customer

    def update(self, instance, validated_data):
        salutation = validated_data.get('salutation', instance.salutation)
        if salutation == 'Mrs':
            validated_data['title'] = 1
        elif salutation == 'Mr':
            validated_data['title'] = 2
        return super().update(instance, validated_data)
