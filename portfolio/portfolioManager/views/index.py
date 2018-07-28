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
        user_portfolio = UserPortfolio.objects.filter(user_id=request.user.id)
        context = {'user_portfolio': user_portfolio,
                   'error_message': error_message,
                   'add_stock_form': stock_forms.AddStockForm()}
        return render(request, 'portfolioManager/index.html', context)