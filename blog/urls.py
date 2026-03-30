from django.urls import path 
from .views import get_posts ,post_detail

urlpatterns = [
    path('posts/',get_posts),
    path('posts/<int:id>/',post_detail),
]