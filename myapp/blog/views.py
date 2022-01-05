from django.shortcuts import render, HttpResponse
from .models import Post
# Create your views here.


def posts(request):
    posts = Post.objects.all()
    return HttpResponse(posts)


def post(request, id):
    post = Post.objects.get(id=id)
    content = f"{post.title} - {post.description}"
    return HttpResponse(content)
