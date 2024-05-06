from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse

from post.models import Post
from post.forms import CreatePostForm, UpdatePostForm
from account.models import Account


def create_post_view(request):

	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect('must_authenticate')

	form = CreatePostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		author = Account.objects.filter(email=user.email).first()
		obj.author = author
		obj.save()
		form = CreatePostForm()

	context['form'] = form

	return render(request, "post/create_post.html", context)


def detail_post_view(request, slug):

	context = {}

	user_post = get_object_or_404(Post, slug=slug)
	context['user_post'] = user_post

	return render(request, 'post/detail_post.html', context)



def edit_post_view(request, slug):

	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect("must_authenticate")

	user_post = get_object_or_404(Post, slug=slug)

	if user_post.author != user:
		return HttpResponse('You are not the author of that post.')

	if request.POST:
		form = UpdatePostForm(request.POST or None, request.FILES or None, instance=user_post)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			context['success_message'] = "Updated"
			user_post = obj

	form = UpdatePostForm(
			initial = {
					"title": user_post.title,
					"body": user_post.body,
					"image": user_post.image,
			}
		)

	context['form'] = form
	return render(request, 'post/edit_post.html', context)


def get_post_queryset(query=None):
	queryset = []
	queries = query.split(" ") # python install 2019 = [python, install, 2019]
	for q in queries:
		posts = Post.objects.filter(
				Q(title__icontains=q) | 
				Q(body__icontains=q)
			).distinct()

		for post in posts:
			queryset.append(post)

	return list(set(queryset))