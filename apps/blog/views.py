from django.shortcuts import render
from .models import Post
from django.views import generic

# Create your views here.
class PostDetail(generic.DetailView):
    model = Post
