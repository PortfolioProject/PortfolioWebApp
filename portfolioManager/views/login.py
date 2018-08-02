from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
import sys
if 'makemigrations' not in sys.argv and 'migrate' not in sys.argv:
    from portfolioManager.forms import login_form


class LoginView(View):
    def get(self, request):
        """
        :param get request:
        :return: A HTML page to render
        """
        return render(request, 'portfolioManager/login.html', {'login_form': login_form.LoginForm()})

    def post(self, request):
        """
        :param request:
        :return: A web page displaying the user's homepage or the invalid login page
        """
        form = login_form.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
        else:
            return render(request, 'portfolioManager/login.html',
                          {'error_message': 'Check Input Data', 'login_form': login_form.LoginForm()})

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'portfolioManager/login.html',
                          {'error_message': 'Invalid Credentials', 'login_form': login_form.LoginForm()})


class LogoutView(LoginRequiredMixin, View):
    """
    To logff the user.
    """
    def get(self, request):
        logout(request)
        return redirect('/login')
