from django.shortcuts import render,redirect
from typing import Any
from . forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages


def register(request : Any):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(
                username=cd['username'],
                email=cd['email'],
            )
            user.set_password(cd['password'])
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.save()
            messages.success(request, 'Account successfully created.', 'success' )
            return redirect('home')
        return render(request, 'accounts/register.html', {'form': form})

    form = UserRegistrationForm()
    return render(request, 'accounts/register.html' , {'form': form})
