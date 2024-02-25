from django.contrib import admin

# Register your models here.
from .models import Product, CartItem

class ProductFields(admin.ModelAdmin):
    fields = ['name','description','price','image']   
    search_fields = ['name']
    list_display = ('id','name','description','price','image') 
    list_filter = ('name', )
    
# registering the Question model
admin.site.register(Product, ProductFields)

class Cart_item_Fields(admin.ModelAdmin):
    fields = ['product_id', 'quantity' ]   
    search_fields = ['product_id']
    list_display = ('product_id', 'quantity') 
    list_filter = ('quantity', )
    
admin.site.register(CartItem, Cart_item_Fields)