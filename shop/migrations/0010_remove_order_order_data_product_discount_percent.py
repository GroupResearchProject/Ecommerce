# Generated by Django 5.0 on 2024-02-18 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_useraddress_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_percent',
            field=models.IntegerField(default=0),
        ),
    ]