from django.db import models

class Customers(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.IntegerField() # male / female
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique = True)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return self.last_name + ',' + self.first_name
    
    
class Purchases(models.Model):
    customer =  models.ForeignKey('Customers', related_name='purchases', on_delete=models.CASCADE)
    product_id = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)   
    quantity = models.PositiveIntegerField()
    purchase_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product_id
