from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import logout, login, authenticate
from index.models import PostModel
from crispy_forms.helper import FormHelper

class UserForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.fields['username'].label = 'alias'
		self.helper = FormHelper(self)

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)
	def __init__(self , *args , **kwargs):
		super(UserLoginForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
	def is_valid(self , request):
		username = request.POST.get('username')
		password = request.POST.get('password')
		#Not a good way of doing auth, but default auth is not working for some reason
		user =  User.objects.filter(username = username , password = password)
		if user.exists() and super().is_valid(): 
			return user[0]
		return False 


class PostCreationForm(forms.Form):
	class Meta():
		model = PostModel
		fields = '__all__'