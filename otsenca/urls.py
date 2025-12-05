from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.review_list, name='review-list'),
    path('reviews/<int:pk>/', views.review_detail, name='review-detail'),
    
    path('products/', views.product_list, name='product-list'),
    path('products/<int:product_id>/', views.product_detail, name='product-detail'),
]