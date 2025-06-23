from django.contrib import admin
from .models import  Employee

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'salary', 'level')
    list_filter = ('level',)
    search_fields = ('first_name', 'last_name', 'position')