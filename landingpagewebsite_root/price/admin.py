from django.contrib import admin

# Register your models here.
from .models import PriceCard,PriceTable

admin.site.register(PriceTable)
admin.site.register(PriceCard)