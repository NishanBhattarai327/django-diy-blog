from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog, Blogger


# Create your views here.
def index(request):
    return render(request, 'index.html')

class BlogListView(ListView):
    model = Blog

class BlogDetailView(DetailView):
    model = Blog

class BloggerListView(ListView):
    model = Blogger

class BloggerDetailView(DetailView):
    model = Blogger
