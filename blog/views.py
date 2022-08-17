from django.shortcuts import render
from .models import BlogPost


def blog(request):
    """ Displays All Blog Posts """

    blogposts = BlogPost.objects.all()

    context = {
        'blogposts': blogposts,
    }

    return render(request, 'blog/blog.html', context)
