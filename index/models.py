from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

#TODO : make more robust and scalable
class UserModel(models.Model):
    alias = models.CharField(max_length = 20)
    bio =  models.CharField(max_length = 600)
    USERNAME_FEILD = 'alias'
    REQUIRED_FEILDS = ['alias' , 'bio']
    def __str__(self):
    	return str(self.alias)


class PostModel(models.Model):
    User = models.ForeignKey(to = UserModel ,on_delete = models.CASCADE , default = 1 , related_name = "PostModel")
    writeup = models.CharField(max_length = 600)
    date_c = models.DateTimeField(default = timezone.now)
    def __str__(self):
    	return str(self.writeup)

class CommentModel(models.Model):
	comment_by = models.ForeignKey(to = UserModel , on_delete = models.CASCADE , related_name='comment_by' , default = None)
	comment_to = models.ForeignKey(to = PostModel , on_delete = models.CASCADE , related_name='comment_to' , default = None)
	comment_dat = models.CharField(max_length = 100)
	def __str__(self):
		return str(self.comment_dat)

class validations(models.Model):
	#user that Validated
    user = models.ForeignKey(to = UserModel,  on_delete = models.CASCADE , related_name = "User")
	#submissions that were validated
    submission = models.ForeignKey(to = PostModel,  on_delete = models.CASCADE , related_name = "submission")

    @classmethod
    def validate(submission : PostModel ,  user : UserModel):
    	is_validated = validations.objects.filter(user = user , submission = submission)
    	#if zero object not there so make else object there so delete
    	if is_validated.exists() : 
    		is_validated[0].delete()
    	else :
    		new_validate = validate(user = user , submission = submission)
    		new_validate.save()
