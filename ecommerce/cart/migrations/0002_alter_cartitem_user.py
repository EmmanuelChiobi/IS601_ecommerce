# Generated by Django 5.1.3 on 2024-12-10 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='user',
            field=models.CharField(max_length=50),
        ),
    ]
