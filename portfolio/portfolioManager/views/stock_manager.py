from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views import View
from portfolioManager.forms import stock_forms
from portfolioManager.models import Stocks
from portfolioManager.models import UserPortfolio
from utils import stock as utils_stock


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


class AddStockInUserPortfolio(LoginRequiredMixin, View):
    def post(self, request):
        form = stock_forms.AddStockForm(request.POST)
        if form.is_valid():
            purchase_price = form.cleaned_data['purchase_price']
            id = form.cleaned_data['stock_id']
            userObj = User.objects.get(id=request.user.id)
            stockObj = Stocks.objects.get(id=id)
            stock_symbol = stockObj.trading_name
            UserPortfolio.objects.create(stock_id=stockObj, user_id=request.user, purchase_price=purchase_price,
                                         current_price=utils_stock.get(stock_symbol)['last_price'])
        return redirect('/')
