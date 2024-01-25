from django.urls import path
from .views import CustomerGet, CustomerPost, CustomerUpdateView, CustomerDeleteView

urlpatterns = [
    path('detail/<int:pk>', CustomerGet.as_view(), name='customer-list-create'),
    path('create/', CustomerPost.as_view(), name='customer-detail'),
    path('update/<int:pk>/', CustomerUpdateView.as_view(), name='customer-update'),
    path('delete/<int:pk>/', CustomerDeleteView.as_view(), name='customer-delete'),
]