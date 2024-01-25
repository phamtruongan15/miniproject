from django.db import models
from Customer.models import Customer

class Order(models.Model):
    # Trường để lưu trữ thông tin sản phẩm đặt hàng
    name = models.CharField(max_length=255)
    # Trường để lưu trữ ngày đặt hàng
    order_date = models.DateField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    complete = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} - {self.product_name} by {self.order_date}"
# Create your models here.
