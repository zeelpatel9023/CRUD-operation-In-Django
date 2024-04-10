from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10, unique=True)
    address = models.CharField(max_length=100)
    product_name = models.CharField(max_length=50)
   
 
    def __str__(self) :
        return self.name








