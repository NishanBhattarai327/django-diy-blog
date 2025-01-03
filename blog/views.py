from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from .models import Blog, Blogger, Comment
from .forms import CommentForm
from django.http import HttpResponseForbidden
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'index.html')

class BlogListView(ListView):
    model = Blog

class BlogDetailView(DetailView):
    model = Blog
    
    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    
class BloggerListView(ListView):
    model = Blogger

class BloggerDetailView(DetailView):
    model = Blogger
