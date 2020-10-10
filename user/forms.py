from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'alias'
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

