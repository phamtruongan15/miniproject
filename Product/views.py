import json
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Product
from .serializers import ProductSerializer, ProductNameSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.pagination import PageNumberPagination
from drf_yasg import openapi
# create
class ProductCreateView(APIView):
    @swagger_auto_schema(

    request_body= ProductNameSerializer
    )
    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#delete
class ProductDeleteView(APIView):
    def delete(self, request, pk, *args, **kwargs):
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return Response({'message': 'Product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        
# update
class ProductUpdateView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return None
        
    @swagger_auto_schema(

        request_body= ProductNameSerializer
        )
    
    def put(self, request, pk, *args, **kwargs):
        product = self.get_object(pk)
        if product is None:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
   
class RatingCreateView(APIView):
    @swagger_auto_schema(

        request_body= ProductNameSerializer
        )
    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# list
class ProductListView(APIView):
   
    def get(self, request, pk):
        # Lấy danh sách khách hàng từ cơ sở dữ liệu
        customers = Product.objects.filter(pk=pk).first()

        # Sử dụng serializer để chuyển đổi danh sách khách hàng thành dữ liệu JSON
        serializer = ProductSerializer(customers, many=False)

        # Trả về response chứa dữ liệu JSON
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# upload imge 
class ImgeView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(
        request_body=ProductNameSerializer,  # Serializer của bạn để mô tả cấu trúc dữ liệu đầu vào
        responses={200: 'OK', 400: 'Bad Request'},
        operation_description="Upload image",
    )
    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# đếm số lượng 
class EmployeeCountView(APIView):
    def get(self, request, *args, **kwargs):
        employee_count = Product.objects.count()
        return Response({'employee_count': employee_count}, status=status.HTTP_200_OK)
    
class ProductSearchView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('product_finish', openapi.IN_QUERY, description="Pagination parameter", type=openapi.TYPE_STRING),
        ],
    )

    def get(self, request, *args, **kwargs):
        # Lấy từ khóa tìm kiếm từ tham số 'name' trong yêu cầu GET
        search_term = request.GET.get('product_finish', '')

        # Thực hiện tìm kiếm sản phẩm
        queryset = None
        if search_term:
            queryset = Product.objects.filter(product_finish=search_term)
        else:
            queryset = Product.objects.all()

        # Serialize dữ liệu
        serializer = ProductSerializer(queryset, many=True)

        return Response(serializer.data)
    
class ProductAPIView(APIView):
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        # Lấy danh sách đối tượng từ cơ sở dữ liệu
        queryset = Product.objects.all()

        # Sử dụng phân trang
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(queryset, request)

        # Serialize dữ liệu
        serializer = ProductSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)
# Create your views here.
