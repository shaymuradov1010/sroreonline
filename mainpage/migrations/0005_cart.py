# Generated by Django 4.0.4 on 2022-04-22 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_productname_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_count', models.IntegerField()),
                ('user_id', models.CharField(max_length=100)),
            ],
        ),
    ]
