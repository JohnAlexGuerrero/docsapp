from django.forms import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserRegistrationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fileds = ['email','password']