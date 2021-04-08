from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.

from .models import Post

from .forms import PostForm

from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

class Postindex(TemplateView):
	template_name = "index.html"

class PostListView(ListView):
	model = Post
	template_name = 'list.html'


class PostDetailView(DetailView):
	model = Post
	template_name = 'detail.html'

class PostCreateView(CreateView):
	model = Post
	template_name = 'create.html'
	form_class = PostForm


class PostDeleteView(DeleteView):
	model = Post
	template_name = 'author_confirm_delete.html'
	success_url = reverse_lazy('PostListView')




class PostUpdateView(UpdateView):
	model = Post
	template_name = 'edit.html'
	form_class = PostForm