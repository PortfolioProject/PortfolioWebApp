from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from portfolioManager.models import UserPortfolio

class StockView(LoginRequiredMixin, View):
    def get(self, request, id):
        return HttpResponse(id)