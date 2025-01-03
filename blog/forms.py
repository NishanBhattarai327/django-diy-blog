from django import forms
from .models import Comment

'''
class Comment(models.Model):
    commentor = models.ForeignKey(User, on_delete=models.RESTRICT)
    post_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['post_date']

    def __str__(self):
        return f'{self.commentor.username} -  {self.description[:75]}'
'''

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('description', )