import sys
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views import View
from django.utils import timezone
import datetime

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

    def get(self, request, user_portfolio_id):
        if UserPortfolio.objects.filter(id=user_portfolio_id).count() > 0:
            user_stocks = UserPortfolio.objects.get(id=user_portfolio_id)
            user = User.objects.get(id=request.user.id)

            if user_stocks.user_id == user:
                logger.info('{0} deleted {1} of {2} stocks bought on {3}'.format(user, user_stocks.stock_id,
                                                                                 user_stocks.no_of_stocks,
                                                                                 user_stocks.purchase_time))
                user_stocks.delete()
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
            stock_id = form.cleaned_data['stock_id']
            user_stock = Stocks.objects.get(id=stock_id)
            purchase_time = request.POST['purchase_time']

            UserPortfolio.objects.create(stock_id=user_stock, user_id=request.user, purchase_price=purchase_price,
                                         purchase_time=purchase_time, no_of_stocks=no_of_stocks)
        return redirect('/')
