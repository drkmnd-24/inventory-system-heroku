from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

admin.site.site_header = "Vanj's Inventory Project"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')
    list_filter = ['category']
# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.unregister(Group)
admin.site.register(Order)
