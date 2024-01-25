from django.db import models


class Product(models.Model):
    product_description = models.CharField(max_length=255)
    product_finish = models.CharField(max_length=255)
    standard_price = models.FloatField()
    rating = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    file = models.ImageField(upload_to='images/',blank=True, null=True)
    position = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product_description} - {self.rating}"


# Create your models here.
