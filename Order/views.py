from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer, OrderNameSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

class OrderGetView(APIView):
   
    def get(self, request, pk):
        # Lấy danh sách khách hàng từ cơ sở dữ liệu
        customers = Order.objects.filter(pk=pk).first()

        # Sử dụng serializer để chuyển đổi danh sách khách hàng thành dữ liệu JSON
        serializer = OrderSerializer(customers, many=False)

        # Trả về response chứa dữ liệu JSON
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class OrderPostView(APIView):   
    @swagger_auto_schema(

    request_body= OrderNameSerializer
    )
    def post(self, request, *args, **kwargs):
        # Chuyển đổi dữ liệu JSON từ yêu cầu POST thành đối tượng Customer
      
        serializer = OrderSerializer(data=request.data)
       
        # Kiểm tra xem dữ liệu có hợp lệ không
        if serializer.is_valid():
            # Lưu đối tượng Customer vào cơ sở dữ liệu
            serializer.save()

            # Trả về response thành công với đối tượng Customer đã tạo
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Trả về response lỗi nếu dữ liệu không hợp lệ
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class OrderUpdateView(APIView):
    
    @swagger_auto_schema(

    request_body= OrderNameSerializer
    )
   
    def put(self, request, pk, *args, **kwargs):
        # Lấy đối tượng cần cập nhật từ cơ sở dữ liệu
        try:
            instance = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        # Sử dụng serializer để cập nhật đối tượng với dữ liệu từ yêu cầu
        serializer = OrderSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OrderDeleteView(APIView):
    def delete(self, request, pk, *args, **kwargs):
        # Lấy đối tượng cần xóa từ cơ sở dữ liệu
        try:
            instance = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        # Thực hiện xóa đối tượng
        instance.delete()

        return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        