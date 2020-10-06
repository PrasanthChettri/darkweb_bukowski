from django.shortcuts import render
from django.http import HttpResponse

def frontpage(request):
	return render(request ,"home.html")

def getNew(request):
	return render(request , 'new.html')
	
def getStarred(request):
	return render(request ,'starred.html')
