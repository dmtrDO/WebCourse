from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, GenerateForm
from .models import Users, Settings, GeneratedPasswords, Roles

import secrets
import string

def generate_password(is_numbers, is_special, is_letters, length):
    password = ''
    characters = ''
    shift = 0

    if is_numbers:
        characters += string.digits
        random_character = secrets.choice(string.digits)
        password += random_character
        shift += 1
    if is_letters:
        characters += string.ascii_letters
        random_character = secrets.choice(string.ascii_letters)
        password += random_character
        shift += 1
    if is_special:
        characters += string.punctuation
        random_character = secrets.choice(string.punctuation)
        password += random_character
        shift += 1

    i = 0
    while i < length - shift:
        random_char = secrets.choice(characters)
        password += random_char
        i += 1
    password = list(password)
    secrets.SystemRandom().shuffle(password)
    password = ''.join(password)
    return password


def set_form_values_from_request_session(request, form):
    for key_name in ('is_numbers', 'is_special', 'is_letters', 'length'):
        if request.session.get(key_name) is not None:
            form.fields[key_name].initial = request.session.get(key_name)

def get_input_values_from_request_session(request, form):
    inputs = []
    for key_name in ('is_numbers', 'is_special', 'is_letters', 'length'):
        request.session[key_name] = form.cleaned_data[key_name]
        inputs.append(request.session.get(key_name))
    return tuple(inputs)

def index(request):
    password_output = 'Тут буде ваш пароль'
    if request.method == 'POST':
        form = GenerateForm(request.POST)
        if form.is_valid():
            is_numbers, is_special, is_letters, length = (
                get_input_values_from_request_session(request, form)
            )
            if is_numbers is False and is_special is False and is_letters is False:
                return render(request, 'index.html',{
                    'form': form,
                    'error': 'Виберіть хоча б якісь знаки !',
                    'password': password_output,
                })
            password_output = generate_password(is_numbers, is_special, is_letters, length)
            return render(request, 'index.html', {
                'form': form, 'password': password_output,
            })
    form = GenerateForm()
    set_form_values_from_request_session(request, form)
    return render(request, 'index.html', {
        'form': form, 'password': password_output,
    })

def home(request):
    email = request.session.get('email')
    if not email:
        return redirect('login')
    return render(request, 'home.html',{'email': email})

def registration(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if Users.objects.filter(email=email).exists():
                return render(request, 'registration.html',
                              {'form': form,
                               'error': 'Користувач з такою поштою уже існує'})
            role = Roles(roleName="User")
            role.save()
            user = Users(email=email, role=role)
            user.set_password(password)
            user.save()
            return redirect('/')

    return render(request, 'registration.html',{ 'form': form, })

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if Users.objects.filter(email=email).exists():
                user = Users.objects.get(email=email)
                if user.check_password(password):
                    request.session['email'] = email
                    return redirect('home',)
            return render(request, 'login.html',
                              {'form': form,
                               'error': 'Неправильна пошта або пароль'})

    return render(request, 'login.html',{ 'form': form, })

def logout(request):
    request.session.flush()
    return redirect('/')

def history(request):
    email = request.session.get('email')
    if not email:
        return redirect('login')
    return render(request, 'history.html', {'email': email})





