from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('Author', on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"pk": self.pk})

class Author(models.Model):
    name = models.OneToOneField(User, on_delete=models.RESTRICT)
    bio = models.TextField()

    def __str__(self):
        return self.name.username
    
    def get_absolute_url(self):
        return reverse("model-detail", kwargs={"pk": self.pk})

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.RESTRICT)
    post_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.author.username} -  {self.description[:75]}'

