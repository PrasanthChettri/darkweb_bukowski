from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from .models import PostModel , validations
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from collections import defaultdict 
from django.db.models import Count


def frontpage(request , page = 0, direction = "-" ):
	#posts in a page 
	post_count = 10
	page += {'-' : 0 , '->' : 1 , '<-' : -1}[direction]
	posts = PostModel.objects.order_by('-date_c').all()[page*post_count:(page + 1)*post_count]
	post_validations = defaultdict(lambda : {'objects' : None, 'total_no' : 0})
	for post in posts:
		all_valid = validations.objects.filter(submission = post)
		post_validations[post]['objects'] = all_valid
		post_validations[post]['total_no'] = len(all_valid) 
		context = {'post_validations' : dict(post_validations) , 'page_no' : page , 'is_end' : len(posts) == post_count }
	return render(request , "index/home.html" , context = context) 

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


def getnew(request):
	return HttpResponseRedirect(reverse("user:new_post"))

'''
IF THIS SHIT TAKES OFF : get_starred = get_favourate literature
						most_validations = literature hall of fame
						strongly linked models =  Can see who commented and their profiles and everything
'''