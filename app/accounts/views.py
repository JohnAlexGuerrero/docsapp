from django.contrib.auth.models import User

from django.urls import reverse_lazy

from accounts.forms import UserRegistrationForm, UserLoginForm

from django.views.generic import CreateView
from django.views.generic import FormView

class UserCreateView(CreateView):
    model = User
    template_name = "registration/signup.html"
    success_url = reverse_lazy('login')
    form_class = UserRegistrationForm
    
class LoginView(FormView):
    form_class = UserLoginForm
    template_name = 'register/login.html'
    success_url = reverse_lazy('/')
    model = User
