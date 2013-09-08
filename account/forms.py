from django import forms

class PasswordForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField()
