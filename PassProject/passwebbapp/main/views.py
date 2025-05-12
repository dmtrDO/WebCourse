from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .models import Users, Settings, GeneratedPasswords, Roles

def index(request):
    return render(request, 'index.html')

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

def home(request):
    email = request.session.get('email')
    if not email:
        return redirect('login')
    return render(request, 'home.html',{'email': email})

def logout(request):
    request.session.flush()
    return redirect('/')

def history(request):
    email = request.session.get('email')
    if not email:
        return redirect('login')
    return render(request, 'history.html', {'email': email})




