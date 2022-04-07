# Generated by Django 4.0.3 on 2022-03-19 19:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField(max_length=10)),
                ('email', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zipCode', models.IntegerField(max_length=5)),
            ],
        ),
    ]
