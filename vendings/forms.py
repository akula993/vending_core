from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Counter, Machine


class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['name', 'serial_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "0", }),
        }


class CounterForm(forms.ModelForm):
    # month = forms.DateTimeField(label='Дата снятия счетчика', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'type': 'datetime-local',}))

    class Meta:
        model = Counter
        fields = ['counter_value', ]
        widgets = {
            'counter_value': forms.TextInput(attrs={'class': 'form-control'}),
            'machine': forms.Select(attrs={'class': 'form-control'}),
        }


    def save(self, commit=True):
        counter = super().save(commit=False)
        # counter.month = self.cleaned_data['month']
        if commit:
            counter.save()
        return counter


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
