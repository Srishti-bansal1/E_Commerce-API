from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action 

from E_commerce_app.models import Product, CartItem
from E_commerce_app.serializers import ProductSerializer, Cart_itemSerializer, Cart_item_detail_Serializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):

    @action(detail=False, methods=["GET"], url_path='show_product')  #apply pagination concept
    def getProduct(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset,many=True) 
        return Response(serializer.data)
    
    @action(detail=True, methods=["GET"], url_path='one_product') 
    def retriveProduct(self, request,pk=None):
        queryset = Product.objects.get(pk=pk)
        serializer = ProductSerializer(queryset) 
        return Response(serializer.data)
    
    @action(detail=False, methods=["POST"], url_path='create_product')
    def add_product(self, request):
        dataReceived = request.data  

        serializer = ProductSerializer(data = dataReceived )
        
        if Product.objects.filter(**dataReceived).exists():
            raise Exception("Duplicate Data")

        if serializer.is_valid():           
            serializer.save()
            serializer_data = serializer.data
            return Response(serializer_data)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(detail=True, methods=['PUT'], url_path='modify_product')
    def update_product(self,request,pk=None):
        queryset = Product.objects.get(pk=pk)
        serializer = ProductSerializer(instance = queryset, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
    @action(detail=True, methods=['DELETE'], url_path='delete_product')
    def remove_product(self,request,pk=None):
        queryset = Product.objects.get(pk=pk)  
        queryset.delete()
        return Response({'message':'data is delete'},status=status.HTTP_202_ACCEPTED)
    
    
class CartViewSet(viewsets.ModelViewSet):

    @action(detail=False, methods=["GET"], url_path='show_item')   #apply pagination concept
    def getCart_item(self, request):
        queryset = CartItem.objects.all()
        serializer = Cart_itemSerializer(queryset,many=True) 
        return Response(serializer.data)
    
    @action(detail=False, methods=["POST"], url_path='create_item')
    def create_Cart_item(self, request):
        dataReceived = request.data 
        serializer = Cart_itemSerializer(data = request.data)

        if CartItem.objects.filter(**dataReceived).exists():
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        if serializer.is_valid():
            serializer.save()
            serializer_data = serializer.data
            return Response(serializer_data)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        
    @action(detail=True, methods=['PUT'], url_path='modify_item')
    def update_item(self,request,pk=None):
        queryset = CartItem.objects.get(pk=pk)
        serializer = Cart_itemSerializer(instance = queryset, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)   
        
    @action(detail=True, methods=['DELETE'], url_path='delete_item')
    def remove_Item(self,request,pk=None):
        queryset = CartItem.objects.get(pk=pk)  
        queryset.delete()
        return Response({'message':'data is delete'}, status=status.HTTP_200_OK)
    


class Product_id_ViewSet(viewsets.ReadOnlyModelViewSet):

    @action(detail=False, methods=["GET"],url_path='show_cart_item')  
    def cart_item_detail(self, request):
        Product_id = int(request.GET['product_id'])
        print(Product_id)
        queryset = CartItem.objects.filter(product_id = Product_id)
        print(queryset)
        serializer = Cart_item_detail_Serializer(queryset, many=True) 
        print(serializer)
        return Response(serializer.data)