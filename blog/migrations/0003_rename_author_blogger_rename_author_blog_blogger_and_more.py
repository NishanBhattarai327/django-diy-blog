# Generated by Django 5.1.4 on 2025-01-02 01:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blog_comments_comment_blog'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='Blogger',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='author',
            new_name='blogger',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='blogger',
        ),
    ]