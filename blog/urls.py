from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='all-blog'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('blog/bloggers/', views.BloggerListView.as_view(), name='all-blogger'),
    path('blog/blogger/<int:pk>', views.BloggerDetailView.as_view(), name='blogger-detail'),
]
