from .models import Student,Department
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = '__all__'
        fields = ('name','mobile','prn_no','department')
        labels = {
            'name': 'Student Name',
            'prn_no' : 'PRN',
            'mobile':'Mobile',
            'department':'Department'

        }

    def __init__(self,*args,**kwargs):
       super(StudentForm, self).__init__(*args,**kwargs)
       self.fields['prn_no'].required =False
       self.fields['department'].empty_label = 'Choose Department'
