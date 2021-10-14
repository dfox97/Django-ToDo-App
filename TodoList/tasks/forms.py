from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
    task_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add a task...','class' : 'mycalss'}))
    class Meta:
        model=Task
        fields='__all__'
       
    