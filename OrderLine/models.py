from django.db import models
from Order.models import Order
from Product.models import Product

class OrderLine(models.Model):
    # Trường để lưu trữ thông tin sản phẩm đặt hàng
    Order = models.ForeignKey(Order, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)   
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def total_price(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.id}"
# Create your models here.
