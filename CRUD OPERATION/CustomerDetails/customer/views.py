from django.shortcuts import render,redirect
from .forms import CustomerForm
from .models import Customer
# Create your views here.
def customer_form(request,id=0):
 
    if request.method == 'GET':
        if id ==0:
            form = CustomerForm()
        else:
            customer =Customer.objects.get(pk=id)
            form = CustomerForm(instance=customer)    
        return render(request,'customer_form.html',{'form':form})
    else:
        if id == 0:
            form = CustomerForm(request.POST)   # request.POST is simply the data that was sent when the form was submitted
        else :
            customer =Customer.objects.get(pk=id)
            form = CustomerForm(request.POST,instance=customer) 
        if form.is_valid():
           form.save()
        return redirect('/list/')

def customer_list(request):
    customer = Customer.objects.all()

    return render(request,'customer_list.html',{'customer_list':customer})


def customer_delete(request,id):
    customer =Customer.objects.get(pk=id)
    customer.delete()
    return render(request,'customer_list.html')
