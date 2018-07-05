from django.db import models

# Create your models here.
class Stocks(models.Model):
    trading_name = models.CharField(max_length=10)
    stock_name   = models.CharField(max_length=20)
