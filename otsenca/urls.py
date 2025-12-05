from django.urls import path
from . import views

urlpatterns = [
    path('comments/', views.comment_list, name='comment-list'),
    path('comments/<int:pk>/', views.comment_detail, name='comment-detail'),
    
    path('articles/', views.article_list, name='article-list'),
    path('articles/<int:pk>/', views.article_detail, name='article-detail'),
]