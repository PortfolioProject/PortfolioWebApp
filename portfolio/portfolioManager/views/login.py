from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from portfolioManager.forms import login_form


class LoginView(View):
    def get(self, request):
        return render(request, 'portfolioManager/login.html', {'login_form': login_form.LoginForm()})

    def post(self, request):
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
    def get(self, request):
        logout(request)
        return redirect('/login')
