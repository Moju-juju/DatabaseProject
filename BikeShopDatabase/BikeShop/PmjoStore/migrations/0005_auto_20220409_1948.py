# Generated by Django 3.2.7 on 2022-04-09 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PmjoStore', '0004_auto_20220409_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='item_id',
        ),
        migrations.AddField(
            model_name='cartitems',
            name='order_id',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='PmjoStore.orders'),
        ),
    ]