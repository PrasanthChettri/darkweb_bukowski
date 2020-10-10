from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserModel(models.Model):
    alias = models.CharField(max_length = 20)
    bio =  models.CharField(max_length = 600)
    def __str__(self):
    	return str(self.alias)
