# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.mixins import LoginRequiredMixin
# from portfolioManager.models import UserPortfolio
# from django.contrib.messages import get_messages
# from django.contrib import messages
import requests
import json
#
# class FetchPriceView(LoginRequiredMixin, View):
#     def get(self, request, symbol):
#         url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + symbol + '&interval=1min&apikey=KMVGVC8ECNLDJQVE'
#         response = requests.get(url)
#         if response == {}:
#             messages.add_message(request, messages.INFO, "Request unsuccessful")
#
#         else:
#             pass

def get(symbol):
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + symbol + '&interval=1min&apikey=KMVGVC8ECNLDJQVE'
        response = requests.get(url)
        if response == {}:
            pass
            # messages.add_message(request, messages.INFO, "Request unsuccessful")




if __name__ == '__main__':

    # fetchpriceviewObj = FetchPriceView(None, None)

    json.loads()






