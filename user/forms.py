from django import forms
from django.contrib.auth.forms import UserCreationForm
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
	user = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)
	def is_valid(self , to_validate):
		username = to_validate.get('username')
		password = to_validate.get('password')
		return super().is_valid() and authenticate(username= username , password = password)

class PostCreationForm(forms.Form):
	class Meta():
		model = PostModel
		fields = '__all__'