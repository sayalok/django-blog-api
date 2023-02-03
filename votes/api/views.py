from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError

from ..models import Vote
from posts.models import Post
from .serializers import VoteSerializer

class VoteCreate(generics.CreateAPIView):
	serializer_class = VoteSerializer
	permission_classes = [permissions.IsAuthenticated]
 
	def get_queryset(self):
		user = self.request.user
		post = Post.objects.get(pk=self.kwargs['pk'])
  
		return Vote.objects.filter(voter=user, post=post)

	def perform_create(self, serializer):
		if self.get_queryset().exists():
			raise ValidationError('You have already voted for this post')
		serializer.save(voter=self.request.user,post = Post.objects.get(pk=self.kwargs['pk']))

 	