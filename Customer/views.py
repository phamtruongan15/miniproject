from django.shortcuts import render
from rest_framework.views import APIView
from drf_yasg import openapi
from rest_framework.response import Response
from rest_framework import status
from .models import Customer
from .serializers import CustomerSerializer,CustomerNameSerializer
from drf_yasg.utils import swagger_auto_schema




class CustomerGet(APIView):
   
    def get(self, request, pk):
        # Lấy danh sách khách hàng từ cơ sở dữ liệu
        customers = Customer.objects.filter(pk=pk).first()

        # Sử dụng serializer để chuyển đổi danh sách khách hàng thành dữ liệu JSON
        serializer = CustomerSerializer(customers, many=False)

        # Trả về response chứa dữ liệu JSON
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CustomerPost(APIView):   
    @swagger_auto_schema(

    request_body= CustomerNameSerializer
    )
    def post(self, request, *args, **kwargs):
        # Chuyển đổi dữ liệu JSON từ yêu cầu POST thành đối tượng Customer
        serializer = CustomerSerializer(data=request.data)

        # Kiểm tra xem dữ liệu có hợp lệ không
        if serializer.is_valid():
            # Lưu đối tượng Customer vào cơ sở dữ liệu
            serializer.save()

            # Trả về response thành công với đối tượng Customer đã tạo
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Trả về response lỗi nếu dữ liệu không hợp lệ
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CustomerUpdateView(APIView):
    
    @swagger_auto_schema(

    request_body= CustomerNameSerializer
    )
   
    def put(self, request, pk, *args, **kwargs):
        # Lấy đối tượng cần cập nhật từ cơ sở dữ liệu
        try:
            instance = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        # Sử dụng serializer để cập nhật đối tượng với dữ liệu từ yêu cầu
        serializer = CustomerSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class CustomerDeleteView(APIView):
    def delete(self, request, pk, *args, **kwargs):
        # Lấy đối tượng cần xóa từ cơ sở dữ liệu
        try:
            instance = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        # Thực hiện xóa đối tượng
        instance.delete()

        return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
# Create your views here.
