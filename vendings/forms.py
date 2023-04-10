from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Counter

class CounterForm(forms.ModelForm):
    class Meta:
        model = Counter
        fields = ['counter_value']
        widgets = {
            'counter_value': forms.TextInput(attrs={'class': 'form-control'}),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))