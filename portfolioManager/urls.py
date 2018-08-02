from django.urls import path

from portfolioManager.views import index
from portfolioManager.views import login
from portfolioManager.views import stock_manager
from portfolioManager.views import user_profile

app_name = 'portfolioManager'
urlpatterns = [
    path('', index.IndexView.as_view(), name='index'),
    path('delete/<int:stock_id>/<int:user_portfolio_id>', stock_manager.DeleteStockFromUserPortfolio.as_view(),
         name='delete_stock'),
    path('delete/<int:stock_id>', stock_manager.DeleteAllStocksFromUserPortfolio.as_view(), name='delete_all_stocks'),
    path('login/', login.LoginView.as_view(), name='login'),
    path('logout/', login.LogoutView.as_view(), name='logout'),
    path('stock/', stock_manager.AddStockInUserPortfolio.as_view(), name='price_fetch'),
    path('stocks/<int:user_id>/<int:stock_id>', stock_manager.StocksView.as_view(), name='stock_details'),
    path('user_registration/', user_profile.Registration.as_view(), name='user_registration')
]