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

#TODO :  make this 
#Probably have to change the model
def TopLiteratureView(request):
	annotated = validations.objects.annotate(Count('submission'))
	return render(request , "index/home.html" , context = {'posts' : PostModel.objects.all().order_by('-date_c')})

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

'''
Stuff to implement if I have time : 
		get_starred = get_favourate literature
		most_validations = literature hall of fame
		strongly linked models =  Can see who commented and their profiles and everything
'''