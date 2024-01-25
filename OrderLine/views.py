from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics
from .models import OrderLine
from .serializers import OrderLineSerializer, OrderLineNameSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

class OrderLineList(APIView):
    def get(self, request, *args, **kwargs):
        order_lines = OrderLine.objects.all()
        serializer = OrderLineSerializer(order_lines, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class OrderLineCreate(APIView):
    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(
        request_body=OrderLineNameSerializer,  # Serializer của bạn để mô tả cấu trúc dữ liệu đầu vào
        responses={200: 'OK', 400: 'Bad Request'},
    )
    def post(self, request, *args, **kwargs):
        serializer = OrderLineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
