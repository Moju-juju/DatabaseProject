# Generated by Django 4.0.3 on 2022-03-20 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0017_remove_cartitems_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='item_id',
            field=models.ManyToManyField(blank=True, to='Products.cartitems'),
        ),
    ]
