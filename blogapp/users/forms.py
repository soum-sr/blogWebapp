from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # Default:requried = True

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2'] # Form in order


# Model form to work with a specific database model
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField() # Default:requried = True

    class Meta:
        model = User
        fields = ['username', 'email'] # it will update the username and email

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
    