from django.urls import path
from .views import OrderGetView, OrderPostView, OrderUpdateView, OrderDeleteView

urlpatterns = [
    path('Order/<int:pk>/', OrderGetView.as_view(), name='modelb-list'),
    path('post/', OrderPostView.as_view(), name='modelb-list'),
    path('update/<int:pk>/', OrderUpdateView.as_view(), name='modelb-list'),
    path('delete/<int:pk>/', OrderDeleteView.as_view(), name='modelb-list'),
    
    # Các URL khác nếu cần
]
