from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import get_messages
from django.shortcuts import render
from django.views import View
from portfolioManager.models import UserPortfolio, Stocks
from utils import stock as st

import sys

if 'makemigrations' not in sys.argv and 'migrate' not in sys.argv:
    from portfolioManager.forms import stock_forms


class IndexView(LoginRequiredMixin, View):
    """
    This renders the home page of the user.
    """

    def get(self, request):
        storage = get_messages(request)
        error_message = None
        for message in storage:
            error_message = message
        user_portfolio = self.calculate_average(request)
        context = {'user_portfolio': user_portfolio,
                   'error_message': error_message,
                   'add_stock_form': stock_forms.AddStockForm()}
        return render(request, 'portfolioManager/index.html', context)

    def calculate_average(self, request):
        different_stocks = UserPortfolio.objects.values("stock_id").distinct()
        user_portfolio = []
        for stock in different_stocks:
            all_stock_entry = UserPortfolio.objects.filter(user_id=request.user.id, stock_id=stock['stock_id'])
            stock_name = Stocks.objects.get(id=stock['stock_id'])
            number_of_stocks = 0
            total_value = 0
            for stock_entry in all_stock_entry:
                number_of_stocks += stock_entry.no_of_stocks
                total_value += stock_entry.purchase_price * stock_entry.no_of_stocks
            user_portfolio.append(
                {'stock_id': stock['stock_id'], 'stock_name': stock_name, 'no_of_stocks': number_of_stocks,
                 'user_id': request.user.id,
                 'purchase_price': (total_value / number_of_stocks), 'current_price': st.get(stock_name)['last_price']})
        return user_portfolio
