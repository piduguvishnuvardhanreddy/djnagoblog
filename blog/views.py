from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework import status 
from .serializers import PostSerializer 
from .models import Post 
from django.shortcuts import get_object_or_404 
from rest_framework.permissions import IsAuthenticated 
from rest_framework.decorators import permission_classes 

@api_view(['GET','POST']) 
@permission_classes([IsAuthenticated])
def get_posts(request):
    if request.method == 'GET':
        posts = Post.objects.all() 
        serializer = PostSerializer(posts, many=True) 
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE']) 
@permission_classes([IsAuthenticated])
def post_detail(request,id):
    post = get_object_or_404(Post,id = id)
    if request.method == 'GET':
        posts = Post.objects.filter(user = request.user)
        serializer = PostSerializer(posts, many=True) 
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostSerializer(post,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors,status=400) 
    elif request.method == 'DELETE':
        post.delete()
        return Response(status = 204) 