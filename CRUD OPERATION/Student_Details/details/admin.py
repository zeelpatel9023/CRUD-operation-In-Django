from django.contrib import admin
from .models import Student,Department
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display =('name','mobile','prn_no','department')
admin.site.register(Student,StudentAdmin)



class DepartmentAdmin(admin.ModelAdmin):
    list_display =('name',)
admin.site.register(Department,DepartmentAdmin)