from django.db import models

# Create your models here.
class PriceCard(models.Model):
    price_card_value = models.CharField(max_length=20, verbose_name='Price')
    price_card_description = models.CharField(max_length=200, verbose_name='Description')

    def __str__(self):
        return self.price_card_value

    class Meta:
        verbose_name = 'Price'
        verbose_name_plural = 'Prices'


class PriceTable(models.Model):
    price_table_title = models.CharField(max_length=20, verbose_name='Item')
    price_table_old_price = models.CharField(max_length=200, verbose_name='Old price')
    price_table_new_price = models.CharField(max_length=200, verbose_name='New price')

    def __str__(self):
        return self.price_table_title

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
