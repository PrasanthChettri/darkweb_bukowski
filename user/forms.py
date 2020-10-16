from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import logout, login, authenticate
from index.models import PostModel

class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'alias'
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)
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