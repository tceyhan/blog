from django.shortcuts import render, redirect, HttpResponse

from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserForm
# add authenticate and login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    form = UserForm()

    if request.method == 'POST':
        # pass in post data when instantiate the form.
        form = UserForm(request.POST, request.FILES)
        # if the form is ok with the info filled:
        if form.is_valid():
            user = form.save()
            
            # want user to login right after registered, import login
            login(request, user)
            # want to redirect to home page, import redirect
            return redirect('post_list')

    context = {
        'form_user': form
    }

    return render(request, "users/register.html", context)

def user_logout(request):
    messages.success(request, "You are Logout!")
    logout(request)
    return redirect('user_login')
    

def user_login(request):

    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
        user = form.get_user()
        if user:
            messages.success(request, "Login successfull")
            login(request, user)
            return redirect('post_list')
    return render(request, 'users/login.html', {"form": form})

def user_profile(request):
    return render(request, 'users/profile.html')

def about(request):
    return render(request, 'users/about.html')
