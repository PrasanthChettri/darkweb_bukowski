from django.db import models
from django.contrib.auth.models import User

class ProfileModel(models.Model):
	user = models.OneToOneField(User , on_delete = models.CASCADE , related_name = 'profile')
	bio = models.CharField(max_length = 200 , default  = "write your bio")
	def username(self):
		return(str(self.user.username))