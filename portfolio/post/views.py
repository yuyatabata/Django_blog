from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    posts = Post.objects.order_by('-published')
    return render(request, 'post/index.html',{'posts': posts})

