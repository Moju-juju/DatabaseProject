# Generated by Django 3.2.7 on 2022-04-27 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PmjoStore', '0011_auto_20220410_1505'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='stocklist',
            unique_together={('store_id', 'bike_prod_id')},
        ),
    ]
