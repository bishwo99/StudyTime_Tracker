from django import forms
from . models import StudySession
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SessionForm(forms.ModelForm):
    class Meta():
        model = StudySession
        fields = ['subject','hours','date']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'hours': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']