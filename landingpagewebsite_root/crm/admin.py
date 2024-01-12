from django.contrib import admin
from .models import Order, StatusCrm, CommentCrm

# Register your models here.

class OrderAmd(admin.ModelAdmin):
    list_display = ('id','order_status','order_name','order_phone','order_dt')
    list_display_links = ('id','order_name')
    search_fields = ('id','order_status','order_name','order_phone','order_dt')
    list_filter = ('order_status',)


admin.site.register(Order, OrderAmd)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)




