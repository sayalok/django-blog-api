from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError

from ..models import Post
from .serializers import PostSerializer
# Create your views here.
class PostList(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
 
	def perform_create(self, serializer):
		serializer.save(author=self.request.user)
  
class PostRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def delete(self, request, *args, **kwargs):
        post = Post.objects.filter(pk=kwargs['pk'], author=self.request.user)
        if post.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('You dont have permission to delete this post')