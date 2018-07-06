from django.urls import path

from portfolioManager.views import index
from portfolioManager.views import login

app_name = 'portfolioManager'
urlpatterns = [
    path('', index.IndexView.as_view(), name='index'),
    path('login/', login.LoginView.as_view(), name='login'),
    path('logout/', login.LogoutView.as_view(), name='logout')
]