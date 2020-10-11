from django.shortcuts import render
from django.http import HttpResponse as hp , HttpResponseRedirect
from django.urls import reverse
from .forms import UserForm
from .models import ProfileModel
from django.contrib import messages
from django.contrib.auth import logout, login as authlogin, authenticate
from .forms import UserLoginForm 
from django.contrib.auth.models import User


# Create your views here.
def signin(request):
	#TODO : show error messages
	if request.method == 'POST' :
		form = UserForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = User(username = username , password = password)
			user.save()
			profile = ProfileModel(user = user)
			profile.save()
			authlogin(request , user) 
			return HttpResponseRedirect(reverse('home:feed'))
	form = UserForm()
	return render(request , 'user/signin.html' , {'form' : form})

def login(request):
	error = '' 
	if request.method =='POST':
		form = UserLoginForm(request.POST)
		if (user := form.is_valid(request.POST)):
				authlogin(request ,user)
				HttpResponseRedirect(reverse('home:'))
		else :
			error = 'incorrect password or username'

	return render( request , 'user/login.html' , 
				{'form' : UserLoginForm() ,
				 'error' : error })

def logoutview(request):
	logout(request)
	return HttpResponseRedirect(reverse('home:feed'))

def signauth(request):
    return hp("YO")

def profile(request):
	user_profile = request.user.profile
	if request.method == 'GET':
		user_profile.bio = request.GET.get('new_bio')
		user_profile.save()
	return render(request , 'user/profile.html' , {'profile' : user_profile} )

def account(request):
    if request.user.is_authenticated :
        return HttpResponseRedirect(reverse('user:profile'))
    else:
        return HttpResponseRedirect(reverse('user:signin'))
