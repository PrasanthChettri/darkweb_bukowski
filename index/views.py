from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from .models import PostModel , validations , CommentModel
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from collections import defaultdict  
from django.db.models import Count

def frontpage(request , page = 0, direction = "-" ):
	#posts in a page 
	post_count = 10
	
	if direction == '->': page += 1
	elif direction == '<-' : page-= 1
	is_anon = request.user.is_anonymous
	posts = PostModel.objects.order_by('-date_c').all()[page*post_count:(page + 1)*post_count]
	post_validations = defaultdict(lambda : {'objects' : None, 'total_no' : 0 , 'is_liked'  : False})
	for post in posts:
		#O(n * m) 
		all_valid = validations.objects.filter(submission = post)
		if not is_anon and validations.objects.filter(submission = post , user = request.user).exists(): 
			post_validations[post]['is_liked'] = True 
		post_validations[post]['objects'] = all_valid
		post_validations[post]['total_no'] = len(all_valid) 
	context = {
		'post_validations' : dict(post_validations) ,
		'page_no' : page , 
		'is_end' : len(posts) == post_count ,
		'is_anon' : is_anon
		}
	return render(request , "index/home.html" , context = context) 

def TopLiteratureView(request):
	top_n = 10
	valids = validations.objects.values('submission_id').annotate(no_of_likes = Count('submission_id'))[:top_n]
	post_validations = defaultdict(lambda : {'objects' : None, 'total_no' : 0 , 'is_liked'  : False})
	is_anon = request.user.is_anonymous
	for valid in valids :
		post =  PostModel.objects.get(pk = valid['submission_id'])
		if not is_anon and validations.objects.filter(submission = post , user = request.user).exists(): 
			post_validations[post]['is_liked'] = True 
		post_validations[post]['objects'] = None 
		post_validations[post]['total_no'] = valid['no_of_likes']

	context = {
		'post_validations' : dict(post_validations) ,
		'page_no' : 0 , 
		'is_end' : False , 
		'is_anon' : is_anon , 
	}
	return render(request , "index/home.html" , context = context)

@csrf_exempt
def commentview(request  , post_id):
	error = ''
	if request.method == "POST":
		if request.user.is_anonymous : 
			return HttpResponseRedirect(reverse("user:login"))
		post = PostModel(pk = post_id)
		comment = request.POST.get('comment_text')
		if comment != '':
			new_comment =  CommentModel(comment_to = post ,
								 comment_by = request.user ,
								 comment_dat = comment 
								)
			new_comment.save()
		else : 
			error = "Empty Field"

	else : 
		post = PostModel(pk = post_id)
	comments = CommentModel.objects.filter(comment_to = post)
	context = {'comments' : comments , 'post_id' : post_id , 'error' : error}
	return render(request , "index/comment.html" , context = context)

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