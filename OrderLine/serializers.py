from rest_framework import serializers
from Order.serializers import OrderSerializer
from Product.serializers import ProductSerializer
from .models import OrderLine

class OrderLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderLine
        fields = ['id', 'Order', 'Product', 'quantity', 'price']
        
class OrderLineNameSerializer(serializers.Serializer):
    Order = serializers.IntegerField(required=True)
    Product = serializers.IntegerField(required=True)
    quantity = serializers.CharField(required=True)
    price = serializers.CharField(required=True)
   
    