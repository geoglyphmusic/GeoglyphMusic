from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404

def blog(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/blog.html', context)

def post(request, post_title):
    post = get_object_or_404(Post, title=post_title)
    context = {
        'post': post
    }
    return render(request, 'blog/post.html', context)
