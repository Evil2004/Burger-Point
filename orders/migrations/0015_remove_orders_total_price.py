# Generated by Django 4.1.5 on 2023-03-14 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_remove_orders_order_date_orders_order_date_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='total_price',
        ),
    ]