from django.shortcuts import render
from .models import Post


def blog(request):
    """ Displays All Blog Posts """

    blogposts = Post.objects.all()

    context = {
        'blogposts': blogposts,
    }

    return render(request, 'blog/blog.html', context)
