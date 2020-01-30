from django import forms
from .models import *

class Employee(forms.ModelForm):
    class Meta:
        model = employee
        fields = ['employee_name','employee_id']

class Client(forms.ModelForm):
    class Meta:
        model = client
        fields = ['client_name', 'client_id']