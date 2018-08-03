from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
        title = models.CharField(max_length=500,default="TITLE")
    	post = models.TextField(max_length=500,default="POST")
        user = models.ForeignKey(User)
        date = models.DateTimeField(auto_now=True)
        likes = models.IntegerField(default = 0)

        
        def __str__(self):
            return self.title


class Comment(models.Model):
    #post = models.ForeignKey('home.Post', on_delete=models.CASCADE, related_name='comments')
    author=models.CharField(max_length=300)
    comment=models.CharField(max_length=300)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment


class Addlikes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default='xxxxx')
    liketime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post
