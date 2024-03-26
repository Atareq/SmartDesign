from django import forms
from django.contrib.auth.models import User

class CustomSignupForm(forms.Form):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
