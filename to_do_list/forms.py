from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'category']  # Include category
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Type your task...'}),
            'category': forms.Select(),
        }
