from .models import UserModel
from django import forms

class UserForm(forms.Form):
    alias = forms.CharField()
    bio = forms.CharField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=32, widget=forms.PasswordInput)
    class Meta:
        model = UserModel
        fields = '__all__'
