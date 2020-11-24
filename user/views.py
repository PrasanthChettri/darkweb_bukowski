from django.shortcuts import render
from django.http import HttpResponse as hp , HttpResponseRedirect , HttpResponseBadRequest
from django.urls import reverse
from .forms import UserForm
from .models import ProfileModel
from django.contrib import messages
from django.contrib.auth import logout, login as authlogin, authenticate
from .forms import UserLoginForm 
from django.contrib.auth.models import User
from index.models import PostModel , validations
import datetime
import pytz

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
	else : 
		form = UserForm()
	return render(request , 'user/signin.html' , {'form' : form})

def login(request):
	error = '' 
	if request.method =='POST':
		form = UserLoginForm(request.POST)
		if (user := form.is_valid(request)):
				authlogin(request ,user)
				return HttpResponseRedirect(reverse('home:feed'))
		else : 
			error = "incorrect password or username "
	return render(request , 'user/login.html' , 
				{'form' : UserLoginForm() , 'error' : error})

def logoutview(request):
	if request.user.is_anonymous : 
		return HttpResponseBadRequest("User not logged in")
	logout(request)
	return HttpResponseRedirect(reverse('home:feed'))

def profile(request):
	user_profile = request.user.profile
	posts  = PostModel.objects.filter(User = request.user)
	post_validations = {}
	for post in posts:
		valid_no = len(validations.objects.filter(submission = post))
		post_validations[post] = valid_no
	if request.method == 'POST':
		user_profile.bio = request.POST.get('new_bio')
		user_profile.save()
	return render(request , 'user/profile.html' , {'profile' : user_profile , 'post_validations' : post_validations})

def account(request):
    if request.user.is_authenticated :
        return HttpResponseRedirect(reverse('user:profile'))
    return HttpResponseRedirect(reverse('user:signin'))

def NewPostView(request):
	if request.user.is_anonymous : 
		return HttpResponseRedirect(reverse('user:signin'))
	error = ''
	if request.method == 'POST':
		post = PostModel()
		post.title = request.POST.get('post_title')
		if post.title == '' : 
			return render(request , 'user/new_post.html' , context = {'error' : 'Title not added'})

		post.writeup = request.POST.get('post_content')
		if post.writeup == '' :
			return render(request , 'user/new_post.html' , context = {'error' : 'Empty Submission'})
		post.date_c = datetime.datetime.now()
		post.User = request.user
		post.save()
		if error == '': 
			return HttpResponseRedirect(reverse('user:profile'))
	return render(request , 'user/new_post.html') 
