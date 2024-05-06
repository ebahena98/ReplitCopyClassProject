from django.shortcuts import render
from operator import attrgetter

from post.views import get_post_queryset
from post.models import Post



def home_screen_view(request):
	
	context = {}

	query = ""
	if request.GET:
		query = request.GET['q']
		context['query'] = str(query)
	user_posts = sorted(get_post_queryset(query), key=attrgetter('date_updated'), reverse=True)
	context['user_posts'] = user_posts

	return render(request, "personal/home.html", context)