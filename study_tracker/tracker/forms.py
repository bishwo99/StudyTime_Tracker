from django import forms
from . models import StudySession
from django.contrib.auth.models import User

class SessionForm(forms.ModelForm):
    class Meta():
        model = StudySession
        fields = ['subject','hours','date']