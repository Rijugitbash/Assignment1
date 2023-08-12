from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm, ApplicationForm
from .models import Application
from django.contrib.auth.decorators import login_required

def home(request):
    login_form = LoginForm()
    register_form = RegistrationForm()

    if request.method == 'POST':
        if 'login_submit' in request.POST:
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect(dashboard)

        elif 'register_submit' in request.POST:
            register_form = RegistrationForm(request.POST)
            if register_form.is_valid():
                username = register_form.cleaned_data['username']
                email = register_form.cleaned_data['email']
                password = register_form.cleaned_data['password']
                new_user = User(username=username, email=email)
                new_user.set_password(password)
                new_user.save()

    context = {'login_form': login_form, 'register_form': register_form}
    return render(request, 'home.html', context)


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def user_profile(request):
    active = "profile"
    context = {
        "active": active
    }
    return render(request, 'profile.html', context)


@login_required
def application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            choice = form.cleaned_data['select_field']
            text_field = form.cleaned_data['text_field']
            file_field = form.cleaned_data['file_field']
            new_application = Application(user=request.user, choice=choice, text_field=text_field, file_field=file_field, status="Not Seen")
            new_application.save()
            return redirect(track_application)

    form = ApplicationForm()
    active = "application"
    context = {
        "active": active,
        "form" : form
    }
    return render(request, 'application.html', context)


@login_required
def track_application(request):
    print(request.user)
    applications = Application.objects.filter(user=request.user)
    active = "track_application"
    context = {
        "active": active,
        "applications": applications
    }
    return render(request, 'track_application.html', context)