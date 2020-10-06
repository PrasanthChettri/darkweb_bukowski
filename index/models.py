from django.db import models
from django.utils import timezone

class UserModel(models.Model):
    alias = models.CharField(max_length = 20)
    password = models.CharField(max_length = 10)
    bio =  models.CharField(max_length = 600)

class PostModel(models.Model):
    User = models.ForeignKey(to = UserModel ,on_delete = models.CASCADE , default = 1 , related_name = "PostModel")
    writeup = models.CharField(max_length = 600)
    validations = models.IntegerField(default = 1)
    date_c = models.DateTimeField(default = timezone.now)

class CommentModel(models.Model):
    comment_to = models.ForeignKey(to = PostModel , on_delete = models.CASCADE , related_name='comments')
    comment_dat = models.CharField(max_length = 100)
    def __str__(self):
        return str(self.comment_dat)