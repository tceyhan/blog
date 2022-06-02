from django.shortcuts import render, redirect, HttpResponse

from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserForm, UserProfileForm, UpdateUserForm
# add authenticate and login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    form_user = UserForm()
    if request.method == 'POST':
        form_user = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form_user.save()            
            login(request, user)
            return redirect('post_list')

    context = {
        'form_user': form_user        
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

@login_required(login_url="/users/login/")
def user_profile(request):
    if request.method == 'POST':
        update_form = UpdateUserForm(request.POST, instance=request.user)           
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if update_form.is_valid() and profile_form.is_valid():
            update_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully")
            return redirect('post_list')
    else:
        profile_form = UserProfileForm()
        update_form = UpdateUserForm()
  
    context = {       
        'profile_form': profile_form,
        'update_form': update_form
      
    }
    return render(request, 'users/profile.html', context)

def about(request):
    return render(request, 'users/about.html')
