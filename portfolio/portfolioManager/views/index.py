from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import get_messages
from django.shortcuts import render
from django.views import View
import sys
if 'makemigrations' not in sys.argv and 'migrate' not in sys.argv:
    from portfolioManager.forms import stock_forms
from portfolioManager.models import UserPortfolio


class IndexView(LoginRequiredMixin, View):
    """
    This renders the home page of the user.
    """
    def get(self, request):
        storage = get_messages(request)
        error_message = None
        for message in storage:
            error_message = message

        self.calculate_average(request)
        user_portfolio = UserPortfolio.objects.filter(user_id=request.user.id)
        self.calculate_average(request)
        # different_stocks = UserPortfolio.objects.values("stock_id").distinct()
        # print("Hi there")
        # print(user_portfolio)
        # print(len(user_portfolio))
        context = {'user_portfolio': user_portfolio,
                   'error_message': error_message,
                   'add_stock_form': stock_forms.AddStockForm()}
        return render(request, 'portfolioManager/index.html', context)

    def calculate_average(self, request):
        different_stocks = UserPortfolio.objects.values("stock_id").distinct()
        for dictObj in different_stocks:
            all_stock_entry = UserPortfolio.objects.filter(user_id=request.user.id, stock_id=dictObj['stock_id'])
            print(all_stock_entry)