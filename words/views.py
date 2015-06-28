from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render

from datetime import datetime
from words.models import Post
from words.forms import MessageForm

def ask_respond(request):
	if request.method == "POST":
		"""
		Page form was submitted
		"""
		form = MessageForm(request.POST)
		if form.is_valid():
			if "__submit_ask" in request.POST:
				post = Post.objects.create(question=form.cleaned_data['content'],
									answered=False)
				return HttpResponseRedirect("/answer/"+str(post.id)+"/")
			
			if "__submit_answer" in request.POST:
				if request.POST.get('q_id'):
					row = Post.objects.filter(id=request.POST['q_id'])
					row.update(answered=True, answer=form.cleaned_data['content'])
				return HttpResponseRedirect("/ask/")
		else:
			""" invalid form """
			return HttpResponseRedirect("/ask/")
			

	unanswered = Post.objects.filter(answered=False)
	post = unanswered.order_by('?').first()
	
	valid_q = (post!=None)

	"""
	return an http response
	you can either build on from scratch (str)
		return HttpResponse("response str")
	or have Django render one from a template
	"""
	return render(request, 
		"hello_temp.html",
		{'current_time': datetime.now(),
		 'post': post,
		 'valid': valid_q})

def answer_respond(request, q_id):
	try:
		post = Post.objects.get(id=q_id)
	except:
		"""
		No such post Error handling
		"""
		raise Http404("Question not found")
	return render(request, "answer_temp.html",
		{'post': post })

def watcher(request):
	return render(request, "watcher.html",
		{ 'post_list': Post.objects.all() })
