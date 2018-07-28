import sys
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views import View
if 'makemigrations' not in sys.argv and 'migrate' not in sys.argv:
    from portfolioManager.forms import stock_forms
from portfolioManager.models import Stocks
from portfolioManager.models import UserPortfolio
import logging

logger = logging.getLogger(__name__)


class StockView(LoginRequiredMixin, View):
    """
    This class is for removing a particular stock from his/her portfolio

    """

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
    """
    This class is for adding a stock in a user's portfolio

    """

    def post(self, request):
        form = stock_forms.AddStockForm(request.POST)
        if form.is_valid():
            purchase_price = form.cleaned_data['purchase_price']
            no_of_stocks = form.cleaned_data['no_of_stocks']
            id = form.cleaned_data['stock_id']
            stockObj = Stocks.objects.get(id=id)
            purchase_time = request.POST['purchase_time']
            UserPortfolio.objects.create(stock_id=stockObj, user_id=request.user, purchase_price=purchase_price,
                                         purchase_time=purchase_time, no_of_stocks=no_of_stocks)
        return redirect('/')
