from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
import sys

if 'makemigrations' not in sys.argv and 'migrate' not in sys.argv:
    from portfolioManager.forms import user_reg_form, login_form


class Registration(View):
    def get(self, request):
        context = {
            'add_user_form': user_reg_form.UserRegistrationForm()
        }
        return render(request, 'portfolioManager/user_registration.html', context)

    def post(self, request):
        form = user_reg_form.UserRegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password_conf = form.cleaned_data['password_conf']
            if password and password_conf and password != password_conf:
                return render(request, 'portfolioManager/user_registration.html', {
                    'error_message': 'Passwords Mismatch', 'add_user_form': user_reg_form.UserRegistrationForm()})
            else:
                user = User.objects.create_user(username, email, password)
                return render(request, 'portfolioManager/login.html',
                              {'error_message': 'Registration Successful', 'login_form': login_form.LoginForm()})

