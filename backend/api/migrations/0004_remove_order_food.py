# Generated by Django 5.0.6 on 2024-06-28 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_quantity_order_price_alter_order_food'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='food',
        ),
    ]
