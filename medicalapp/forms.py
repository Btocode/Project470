from django import forms
from django.db.models import fields
from .models import Doctor

# Create your forms here.

class NewUserForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = []