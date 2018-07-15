# Generated by Django 2.0.7 on 2018-07-05 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolioManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPortfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('current_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolioManager.Stocks')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]