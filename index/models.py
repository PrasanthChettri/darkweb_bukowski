from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


#TODO : make database more robust and scalable
class PostModel(models.Model):
    User = models.ForeignKey(to = User ,on_delete = models.CASCADE , default = 1 , related_name = "PostModel")
    title = models.CharField(max_length = 50 , default = '')
    writeup = models.CharField(max_length = 550)
    date_c = models.DateTimeField(default = timezone.now)
    def __str__(self):
    	return str(self.writeup)

class CommentModel(models.Model):
	comment_by = models.ForeignKey(to = User , on_delete = models.CASCADE , related_name='comment_by' , default = None)
	comment_to = models.ForeignKey(to = PostModel , on_delete = models.CASCADE , related_name='comment_to' , default = None)
	comment_dat = models.CharField(max_length = 100)
	def __str__(self):
		return str(self.comment_dat)

class validations(models.Model):
	#user that Validated
	user = models.ForeignKey(to = User,  on_delete = models.CASCADE , related_name = "User")
	#submissions that were validated
	submission = models.ForeignKey(to = PostModel,  on_delete = models.CASCADE , related_name = "submission")