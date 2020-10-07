from django.contrib import admin
from .models import Product, Offer, Kfc


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class KfcAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(Kfc, KfcAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Product,ProductAdmin)





