from rest_framework import viewsets # new
from .serializers import PostSerializer

from rest_framework import viewsets # new
from demo.models import Post

class PostViewSet(viewsets.ModelViewSet): # new	
	queryset = Post.objects.all()
	serializer_class = PostSerializer