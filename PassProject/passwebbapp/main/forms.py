from django.forms import (Form, EmailInput, PasswordInput,
                          CharField, EmailField)

class LoginForm(Form):
    email = EmailField(
                       widget=EmailInput(attrs={
                           'id': 'email',
                           'class': 'form-control',
                           'placeholder': 'Електронна пошта',
                       }))
    password = CharField(
                         widget=PasswordInput(attrs={
                             'id': 'password',
                             'class': 'form-control',
                             'placeholder': 'Пароль',
                         }))

class RegistrationForm(Form):
    email = EmailField(
                      widget=EmailInput(attrs={
                          'id': 'email',
                          'class' : 'form-control',
                          'placeholder': 'Електронна пошта',
                      }))
    password = CharField(
                      widget=PasswordInput(attrs={
                          'id': 'password',
                          'class' : 'form-control',
                          'placeholder': 'Пароль',
                      }))


