from django.shortcuts import render
from django.http import HttpResponse

def frontpage(request):
	return render(request ,"home.html")

def getpopular(request):
	return HttpResponse('popular', )

def getnew(request):
	return HttpResponse('popular')
