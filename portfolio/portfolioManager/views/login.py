from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

class LoginView(View):
    def get(self, request):
        return render(request, 'portfolioManager/login.html')
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('Unsuccessful Login')

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('/login/')
