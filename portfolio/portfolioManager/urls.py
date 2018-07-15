from django.urls import path

from portfolioManager.views import index
from portfolioManager.views import login
from portfolioManager.views import stock_manager

app_name = 'portfolioManager'
urlpatterns = [
    path('', index.IndexView.as_view(), name='index'),
    path('delete/<int:id>', stock_manager.StockView.as_view(), name='index'),
    path('login/', login.LoginView.as_view(), name='login'),
    path('logout/', login.LogoutView.as_view(), name='logout'),
    path('stock/', stock_manager.AddStockInUserPortfolio.as_view(), name='price_fetch')
]