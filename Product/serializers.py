from rest_framework import serializers
from .models import Product
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'product_description', 'product_finish', 'standard_price', 'rating', 'comment', 'file', 'position']
        
class ProductNameSerializer(serializers.Serializer):
    product_description = serializers.CharField(required=True)
    product_finish = serializers.CharField(required=True)
    standard_price = serializers.FloatField(required=True)
    rating = serializers.IntegerField(required=True)
    standacommentrd_price = serializers.CharField(required=True)
    file = serializers.ImageField(required=False)
    position = serializers.CharField(required=True)
    
