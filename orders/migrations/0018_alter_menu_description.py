# Generated by Django 4.1.5 on 2023-03-23 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_remove_orders_order_date_time_orders_order_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='description',
            field=models.TextField(default=None),
        ),
    ]