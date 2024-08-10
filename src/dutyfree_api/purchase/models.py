from django.db import models



class Customers(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.IntegerField(null=True) # male / female
    salutation = models.CharField(max_length=10, default=None, null=True)
    firstname = models.CharField(max_length=50, null=True, blank=True)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique = True, null=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.lastname + ',' + self.firstname
    
    
class Purchases(models.Model):
    customer =  models.ForeignKey('Customers', related_name='purchases', on_delete=models.CASCADE)
    product_id = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=20)   
    quantity = models.PositiveIntegerField()
    purchased_date = models.DateTimeField(default=None, null=True)
    
    def __str__(self):
        return self.product_id
