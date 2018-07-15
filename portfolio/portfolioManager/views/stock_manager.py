from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from portfolioManager.models import UserPortfolio
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.models import User

class StockView(LoginRequiredMixin, View):
    def get(self, request, id):
        if UserPortfolio.objects.filter(id=id).count() > 0:
            stockUserObj = UserPortfolio.objects.get(id=id)

            userObj = User.objects.get(id=request.user.id)

            if stockUserObj.user_id == userObj:
                stockUserObj.delete()
        else:
            messages.add_message(request, messages.INFO, "Mind your own fuc*** business")

        return redirect('/')

