from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from .models import PostModel , validations
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from collections import defaultdict 
from django.db.models import Count


def frontpage(request):
	#posts in a page 
	post_count = 10

	if 'page' in request.GET : 
		page_number = request.GET.get('page') - 1 
	else : 
		page_number = 0 

	posts = PostModel.objects.order_by('-date_c').all()[page_number*post_count:(page_number + 1)*post_count]

	post_validations = defaultdict(lambda : {'objects' : None, 'total_no' : 0})
	for post in posts:
		all_valid = validations.objects.filter(submission = post)
		post_validations[post]['objects'] = all_valid
		post_validations[post]['total_no'] = len(all_valid) 

	return render(request , "index/home.html" , context = {'post_validations' : dict(post_validations)})

def TopLiteratureView(request):
	annotated = validations.objects.annotate(Count('submission'))
	return render(request , "index/home.html" , context = {'posts' : PostModel.objects.all().order_by('-date_c')})

@csrf_exempt
def updatevalidate(request):
	if request.method == "POST":
		post_id = request.POST.get('post_id')
		post = PostModel(id = post_id)
		is_liked = False
		if validation_instance := validations.objects.filter(user= request.user , submission = post):
			validation_instance.delete()
		else : 
			validation_instance = validations(user = request.user , submission = post)
			validation_instance.save()
			is_liked  = True 
		return JsonResponse({'liked' : is_liked , 'post_id'  : post_id})
	return HttpResponse("Be Tolstoy not Snowden")


def getStarred(request):
	return render(request ,'index/starred.html')
