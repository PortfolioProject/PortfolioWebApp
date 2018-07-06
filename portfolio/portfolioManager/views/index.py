from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from portfolioManager.models import UserPortfolio

class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        user_portfolio = UserPortfolio.objects.filter(user_id=request.user.id)
        context = {'user_portfolio': user_portfolio}
        return render(request, 'portfolioManager/index.html', context)