from django.urls import reverse,reverse_lazy
from django.views.generic.edit import UpdateView
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PostForm, CommentForm
from .models import Post, Comment 

# Create your views here.
# POST
def home(request):
	posts_instances = Post.objects.all()

	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form = form.save(commit=False)
			form.user = request.user
			form.save()
			return redirect('/')
	else:
		form = PostForm()

	context = {
		'posts': posts_instances,
		'form': form
	}
	return render(request, "posts/home.html", context)

def post_detail(request, pk):
	post_instance = get_object_or_404(Post, pk=pk)

	if request.method == 'POST':
		comment = CommentForm(request.POST)
		if comment.is_valid():
			comment = comment.save(commit=False)
			comment.user = request.user
			comment.post = post_instance
			comment.save()
			return redirect('detail-post', pk=pk)
	else:
		comment = CommentForm()

	context = {
		"post": post_instance,
		"commentForm": comment
	}

	return render(request, "posts/detail_post.html", context)

def post_update(request, pk):
	post_instance = get_object_or_404(Post, pk=pk)

	if request.method == "POST":
		form = PostForm(request.POST, request.FILES, instance=post_instance)
		if form.is_valid():
			form.save()
			return redirect('detail-post', pk=pk)
	else:
		form = PostForm(instance=post_instance)

	context = {
		'form': form
	}
	return render(request, "posts/post_update.html", context)

def post_delete(request, pk):
	post_instance = get_object_or_404(Post, pk=pk)
	user_instance = request.user.pk

	if request.method == "POST":
		post_instance.delete()
		return redirect('profile')

	context = {
		'post': post_instance, 
	}

	return render(request, "posts/delete_post.html", context)

# COMMENT
def comment_update(request, pk):
	comment_instance = get_object_or_404(Comment, pk=pk)
	
	if request.method == "POST":
		form = CommentForm(request.POST, instance=comment_instance)
		if form.is_valid():
			form.save()
			return redirect('detail-post', pk=comment_instance.post.pk)
	else:
		form = CommentForm(instance=comment_instance)

	context = {
		'form':form 
	}
	return render(request, "posts/comment_update.html", context)

def comment_delete(request, pk):
	comment_instance = get_object_or_404(Comment, pk=pk)

	if request.method == "POST":
		comment_instance.delete()
		return redirect('detail-post', pk=comment_instance.post.pk)

	return render(request, "posts/comment_delete.html")