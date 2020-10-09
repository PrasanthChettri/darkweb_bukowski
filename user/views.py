from django.shortcuts import render
from django.http import HttpResponse as hp , HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def signin(request):
        return render(request , 'user/signin.html')

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
