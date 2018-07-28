from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

"""
This file defines the schema of the databases.

"""


# Create your models here.
class Stocks(models.Model):
    trading_name = models.CharField(max_length=10)
    stock_name = models.CharField(max_length=20)

    def __str__(self):
        return self.trading_name


class UserPortfolio(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_id = models.ForeignKey(Stocks, on_delete=models.CASCADE)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_time  = models.DateTimeField(default=datetime.datetime.now)
    no_of_stocks   = models.BigIntegerField(default=10)


    def __str__(self):
        return "{0} {1} {2} {3} {4}".format(self.user_id, self.stock_id, self.purchase_price, self.purchase_time,
                                          self.no_of_stocks)

