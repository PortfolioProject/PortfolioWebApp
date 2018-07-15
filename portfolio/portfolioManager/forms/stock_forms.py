from django import forms
from portfolioManager.models import Stocks

class AddStockForm(forms.Form):
    available_stocks = Stocks.objects.all()
    tuple_list = [(stock.id, stock.trading_name) for stock in available_stocks]
    stock_id = forms.ChoiceField(label='Stocks', choices=tuple_list)
    purchase_price = forms.DecimalField(label="Price $", min_value=0.0, decimal_places=2)
