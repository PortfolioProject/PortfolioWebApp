from django import forms
from portfolioManager.models import Stocks


class AddStockForm(forms.Form):
    """
    This form is the backend of the form which gets displayed in the frontend.
    """
    available_stocks = Stocks.objects.all()
    tuple_list = [(stock.id, stock.trading_name) for stock in available_stocks]
    stock_id = forms.ChoiceField(label='Stocks', choices=tuple_list)
    purchase_price = forms.DecimalField(label="Price $", min_value=0.0, decimal_places=2)
    no_of_stocks   = forms.IntegerField(label='No. of Stocks', min_value=0)
