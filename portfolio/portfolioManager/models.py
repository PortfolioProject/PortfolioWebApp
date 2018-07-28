from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
"""
This file defines the schema of the databases.

"""

# Create your models here.
class Stocks(models.Model):
    trading_name = models.CharField(max_length=10)
    stock_name   = models.CharField(max_length=20)
    def __str__(self):
        return self.trading_name

class UserPortfolio(models.Model):
    user_id        = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_id       = models.ForeignKey(Stocks, on_delete=models.CASCADE)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_time  = models.DateTimeField(default=timezone.now)
    no_of_stocks   = models.BigIntegerField(default=0)


    def __str__(self):
        return "{} {} {} {}".format(self.user_id, self.stock_id, self.purchase_price, self.current_price)