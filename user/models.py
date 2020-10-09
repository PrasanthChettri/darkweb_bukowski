from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserModel(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    alias = models.CharField(max_length = 20)
    bio =  models.CharField(max_length = 600)
    USERNAME_FEILD = 'alias'
    REQUIRED_FEILDS = ['alias' , 'bio', 'password']
    def __str__(self):
    	return str(self.alias)
