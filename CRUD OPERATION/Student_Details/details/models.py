from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) :
        return self.name
    



class Student(models.Model):
    name = models.CharField(max_length=100)
    prn_no = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self) :
        return self.name