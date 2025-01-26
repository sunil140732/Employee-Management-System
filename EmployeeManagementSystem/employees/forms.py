from django import forms
from django.forms.widgets import DateInput
from .models import Employee

class EmployeeForm(forms.ModelForm):
    department = forms.ChoiceField(
        choices=[
            ('HR', 'Human Resources'),
            ('IT', 'Information Technology'),
            ('Sales', 'Sales'),
            ('Marketing', 'Marketing'),
            ('Finance', 'Finance'),
            ('Operations', 'Operations'),
            ('Engineering', 'Engineering'),
            ('Customer Support', 'Customer Support'),
        ],
        required=True,
        widget=forms.Select(attrs={'style': 'margin-top: 10px; margin-bottom: 10px; width: 100%;'}),
    )
    date_of_joining = forms.DateField(
        widget=DateInput(attrs={'type': 'date', 'style': 'margin-top: 10px; margin-bottom: 10px; width: 100%;'}),
        input_formats=['%Y-%m-%d'],
    )
    
    class Meta:
        model = Employee
        fields = ['name', 'email', 'department', 'date_of_joining', 'salary']
        widgets = {
            'name': forms.TextInput(attrs={'style': 'margin-top: 10px; margin-bottom: 10px; width: 100%;'}),
            'email': forms.EmailInput(attrs={'style': 'margin-top: 10px; margin-bottom: 10px; width: 100%;'}),
            'salary': forms.NumberInput(attrs={'style': 'margin-top: 10px; margin-bottom: 10px; width: 100%;'}),
        }
