from django.urls import path
from .views import blog_views, blog_single, views_up

app_name = 'blog'

urlpatterns = [
    path('', blog_views, name="blog"),
    path('article/<int:pk>/', blog_single, name="blog-single"),
    path('views_up/<int:pk>/', views_up, name="views_up"),
]