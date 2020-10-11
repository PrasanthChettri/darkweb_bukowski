from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from .models import PostModel
from django.urls import reverse

def frontpage(request):
    return render(request , "index/home.html" , context = {'posts' : PostModel.objects.all().order_by('-date_c')})

def TopLiteratureView(request):
    return render(request , "index/home.html" , context = {'posts' : PostModel.objects.all().order_by('-date_c')})

def updatevalidate(request):
	return render(request ,'index/starred.html')

def getStarred(request):
	return render(request ,'index/starred.html')
