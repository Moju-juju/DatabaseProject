# Generated by Django 3.2.7 on 2022-04-10 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PmjoStore', '0007_stocklist_store_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stocklist',
            name='bike_prod_id',
        ),
        migrations.AddField(
            model_name='stocklist',
            name='bike_prod_id',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='PmjoStore.bikeproducts'),
        ),
        migrations.AlterField(
            model_name='stocklist',
            name='store_id',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='PmjoStore.store'),
        ),
    ]
