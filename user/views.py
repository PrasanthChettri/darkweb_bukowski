from django.shortcuts import render
from django.http import HttpResponse as hp , HttpResponseRedirect
from django.urls import reverse
from .forms import UserForm
from .models import Profile
from django.contrib import messages


# Create your views here.
def signin(request):
	#TODO : show error messages
	if request.method == 'POST' :
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save() 
			user.set_password(user.password)
			user.save()
			profile = Profile(user = user)
			profile.save()
			user = authenticate(username=request.POST['username'],
	                                password=request.POST['password'])
			login(request ,user) 
			return HttpResponseRedirect(reverse('home:feed'))
	form = UserForm()
	return render(request , 'user/signin.html' , {'form' : form})

def login(request):
    return hp("YO")

def logout(request):
    return hp("YO")

def signauth(request):
    return hp("YO")

def profile(request):
    return hp("YO")

def account(request):
    if 'id' in request.GET :
        return HttpResponseRedirect(reverse('user:profile'))
    else:
        return HttpResponseRedirect(reverse('user:signin'))
