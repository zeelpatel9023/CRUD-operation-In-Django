from .models import Customer
from django import forms

class CustomerForm(forms.ModelForm):
        class Meta:
            model = Customer
            fields = ('name','mobile','address','product_name')

            labels = {
                  'name':'Customer Name',
                  'address': "Address",
                  'product_name': "Product Name"
            }