from rest_framework import serializers
from Customer.serializers import CustomerSerializer
from .models import Order

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'name', 'order_date', 'customer', 'status', 'complete']
        
class OrderNameSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    order_date = serializers.DateField(required=True)
    customer = serializers.IntegerField(required=True)
    status = serializers.CharField(required=True)
    complete = serializers.CharField(required=True)
    