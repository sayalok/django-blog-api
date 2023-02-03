from django.shortcuts import render
from rest_framework import generics, permissions, mixins, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from ..models import Vote
from posts.models import Post
from .serializers import VoteSerializer

class VoteCreate(generics.CreateAPIView, mixins.DestroyModelMixin):
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

	def delete(self, request, *args, **kwargs):
		if self.get_queryset().exists():
			self.get_queryset().delete()
			return Response(status=status.HTTP_204_NO_CONTENT)

		raise ValidationError('You have not voted for this post')