from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def homepage(request):
    return render(request, 'user_app/homepage.html', {})


# def create_user_view(request):
#     form = UserSignUp(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = UserSignUp()
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'user_app/user_signup.html', context)


def user_profile_view(request):
    form = UserProfile(request.POST or None)
    if form.is_valid():
        form.save()
        form = UserProfile()
        return redirect('/donationview')
    context = {
        'form': form
    }

    return render(request, 'user_app/user_profile.html', context)


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('/profile')
#     else:
#         form = SignUpForm()
#     return render(request, 'user_app/user_signup.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/profile')
    else:
        form = UserCreationForm()
    return render(request, 'user_app/user_signup.html', {'form': form})


def donation_view(request):
    return render(request, 'user_app/donation_view.html')