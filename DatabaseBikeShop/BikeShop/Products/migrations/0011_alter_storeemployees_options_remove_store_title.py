# Generated by Django 4.0.3 on 2022-03-20 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0010_alter_bikebrands_options_alter_bikecategory_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='storeemployees',
            options={'verbose_name_plural': 'Products Employees'},
        ),
        migrations.RemoveField(
            model_name='store',
            name='title',
        ),
    ]
