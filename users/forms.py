from .models import User, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('username', 'password1', 'password2', 'portfolio', 'profile_pic', 'first_name', 'last_name')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('bio', 'location', 'birth_date',)
        