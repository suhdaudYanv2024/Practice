from django.urls import path
from .views import AuthorListCreate, AuthorDetail, CategoryListCreate, CategoryDetail, PostListCreate, PostDetail

urlpatterns = [
    path('authors/', AuthorListCreate.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),


]