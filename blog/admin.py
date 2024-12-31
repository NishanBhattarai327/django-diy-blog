from django.contrib import admin

from .models import Blog, Comment, Author


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'post_date')
    inlines = [CommentInline]

# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
admin.site.register(Author)
