from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'first_name', 'last_name', 'position',
            'salary', 'level', 'email', 'phone', 'photo', 'date_hired'
        ]
        widgets = {
            'date_hired': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
        }
