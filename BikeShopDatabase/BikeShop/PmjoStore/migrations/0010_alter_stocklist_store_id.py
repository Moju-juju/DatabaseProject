# Generated by Django 3.2.7 on 2022-04-10 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PmjoStore', '0009_alter_stocklist_bike_prod_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocklist',
            name='store_id',
            field=models.OneToOneField(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='PmjoStore.store'),
        ),
    ]
