from django.contrib import admin

from Shop.models import Category, Customer
from Shop.models import Product
class Categoryinfo(admin.ModelAdmin):
    list_display = ['Name']

class Productinfo(admin.ModelAdmin):
    list_display = ['Name','Category','Price']
class Customerinfo(admin.ModelAdmin):
    list_display = ['First_Name','Last_Name','Email','Phone','Password']
# Register your models here.
admin.site.register(Product,Productinfo)
admin.site.register(Category,Categoryinfo)
admin.site.register(Customer,Customerinfo)
