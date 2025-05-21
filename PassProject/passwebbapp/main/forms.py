from django.forms import (Form, EmailInput, PasswordInput, IntegerField, NumberInput, TextInput,
                          CharField, EmailField, BooleanField, CheckboxInput, HiddenInput)

class LoginForm(Form):
    email = EmailField(widget=EmailInput(attrs={
        'id': 'email', 'class': 'form-control', 'placeholder': 'Електронна пошта',
    }))
    password = CharField(widget=PasswordInput(attrs={
        'id': 'password', 'class': 'form-control', 'placeholder': 'Пароль',
    }))

class RegistrationForm(Form):
    email = EmailField(widget=EmailInput(attrs={
        'id': 'email', 'class' : 'form-control', 'placeholder': 'Електронна пошта',
    }))
    password = CharField(widget=PasswordInput(attrs={
        'id': 'password', 'class' : 'form-control', 'placeholder': 'Пароль',
    }))

class GenerateForm(Form):
    is_numbers = BooleanField(required=False, initial=True, widget=CheckboxInput())
    is_special = BooleanField(required=False, initial=True, widget=CheckboxInput())
    is_letters = BooleanField(required=False, initial=True, widget=CheckboxInput())
    length = IntegerField(min_value=15, max_value=25, initial=20,
        widget=NumberInput(attrs={'type': 'range', 'step': '1', 'class': 'length-range'})
    )



