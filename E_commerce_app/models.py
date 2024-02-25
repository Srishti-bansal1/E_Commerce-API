from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='Item_Image', null=True, blank=True)

class CartItem(models.Model):
    product_id = models.ForeignKey(Product, default = None,  on_delete = models.CASCADE, related_name='product')
    quantity = models.IntegerField()