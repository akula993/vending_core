from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Counter, Machine


class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['name', 'serial_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "0",}),
        }



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
