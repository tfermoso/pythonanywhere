# app1/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplica form-control a cada widget
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
