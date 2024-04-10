from .models import Employee
from django import forms


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = '__all__'
        fields = ('fullname','mobile','emp_code','position')

        labels = {
            'fullname' : 'Full Name',
            'emp_code' : 'Employee Code',
        }

    def __init__(self,*args,**kwargs) :
            super(EmployeeForm, self).__init__(*args,**kwargs)
            self.fields['position'].empty_label = "Select your Position"
            self.fields['emp_code'].required = False