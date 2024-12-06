# Generated by Django 5.1.3 on 2024-12-05 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('userName', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('PID', models.IntegerField()),
                ('Image', models.CharField(max_length=200)),
                ('Model', models.CharField(max_length=200)),
                ('Category', models.CharField(max_length=200)),
                ('Specifications', models.TextField(max_length=500)),
                ('Price', models.FloatField()),
                ('StockAmount', models.IntegerField()),
            ],
        ),
    ]