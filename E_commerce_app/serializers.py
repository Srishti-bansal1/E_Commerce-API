from .models import  Product, CartItem
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta :
        model = Product
        fields = ('__all__')

class Cart_itemSerializer(serializers.ModelSerializer):
    class Meta :
        model = CartItem
        fields = ('__all__')


class Cart_item_detail_Serializer(serializers.ModelSerializer):
    product_detail = serializers.SerializerMethodField()

    class Meta :
        model = CartItem
        fields = ('product_id','quantity','product_detail')

    def get_product_detail(self,obj): 
        print(obj)
        product_details = Product.objects.get(id=obj.product_id.id)
        print(product_details)
        _serializer = ProductSerializer(product_details)
        return _serializer.data