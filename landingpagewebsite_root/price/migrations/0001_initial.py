# Generated by Django 4.2.7 on 2023-12-19 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_card_value', models.CharField(max_length=20, verbose_name='Price')),
                ('price_card_description', models.CharField(max_length=200, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Price',
                'verbose_name_plural': 'Prices',
            },
        ),
        migrations.CreateModel(
            name='PriceTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_table_title', models.CharField(max_length=20, verbose_name='Item')),
                ('price_table_old_price', models.CharField(max_length=200, verbose_name='Old price')),
                ('price_table_new_price', models.CharField(max_length=200, verbose_name='New price')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
            },
        ),
    ]
