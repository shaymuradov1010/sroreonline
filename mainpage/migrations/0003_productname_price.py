# Generated by Django 4.0.4 on 2022-04-18 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_productname'),
    ]

    operations = [
        migrations.AddField(
            model_name='productname',
            name='price',
            field=models.CharField(default=10000, max_length=50),
        ),
    ]