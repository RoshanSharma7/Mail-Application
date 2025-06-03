from django import forms
from django.contrib.auth.models import User
from .models import SMTPSetting

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class SMTPForm(forms.ModelForm):
    class Meta:
        model = SMTPSetting
        exclude = ['user']

class EmailForm(forms.Form):
    to_email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
