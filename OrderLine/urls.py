from django.urls import path
from .views import OrderLineList, OrderLineCreate

urlpatterns = [
    path('list/<int:pk>', OrderLineList.as_view(), name='modelb-list'),
    path('create/', OrderLineCreate.as_view(), name='modelb-list'),
]
