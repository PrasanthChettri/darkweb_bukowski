from django.shortcuts import render
from django.http import HttpResponse
from .models import PostModel

def frontpage(request):
    return render(request , "home.html" , context = {'posts' : PostModel.objects.all().order_by('-date_c')})

def getNew(request):
	return render(request , 'new.html')
	
def getStarred(request):
	return render(request ,'starred.html')
