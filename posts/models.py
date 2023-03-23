from django.db import models

# Create your models here.

class Post(models.Model):
    '''a post'''
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.IntegerField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    '''A comment on a post'''
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.IntegerField()
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text