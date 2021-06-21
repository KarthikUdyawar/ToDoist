from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'
        widgets = {
            'complete' : forms.CheckboxInput(attrs={'class': 'btn-check', 'id': 'btn-check-outlined', "autocomplete": "off"},)
        }