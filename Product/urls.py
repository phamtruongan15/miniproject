from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:pk>/', views.ProductListView.as_view(), name='create-product'),
    path('create/', views.ProductCreateView.as_view(), name='create-product'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete-product'),
    path('update/<int:pk>/', views.ProductUpdateView.as_view(), name='update-product'),
    path('rating/<int:pk>/', views.RatingCreateView.as_view(), name='rating-product'),
    path('upload/', views.ImgeView.as_view(), name='upload'),
    path('employee/', views.EmployeeCountView.as_view(), name='employee'),
    path('list/', views.ProductSearchView.as_view(), name='search'),
]