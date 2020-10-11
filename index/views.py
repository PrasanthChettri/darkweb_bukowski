from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from .models import PostModel , validations
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def frontpage(request):
    return render(request , "index/home.html" , context = {'posts' : PostModel.objects.all().order_by('-date_c')})

def TopLiteratureView(request):
    return render(request , "index/home.html" , context = {'posts' : PostModel.objects.all().order_by('-date_c')})

@csrf_exempt
def updatevalidate(request):
	if request.method == "POST":
		post_id = request.POST.get('post_id')
		post = PostModel(id = post_id)
		is_liked =  False 
		if validation_instance := validations.objects.filter(user= request.user , submission = post):
			validation_instance.delete()
		else : 
			validation_instance = validations(user = request.user , submission = post)
			validation_instance.save()
			is_liked  = True 
		return JsonResponse({'liked' : is_liked})
	return HttpResponse("Post stuff don't try to be a hacker")


def getStarred(request):
	return render(request ,'index/starred.html')
