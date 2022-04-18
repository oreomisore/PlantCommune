from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Carousel, Item, OrderItem, Order

admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Carousel)