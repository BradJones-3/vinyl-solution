from django.shortcuts import render, get_object_or_404

from .models import BlogPost, BlogComment


def blog(request):
    """ Displays All Blog Posts """

    blogposts = BlogPost.objects.all()

    context = {
        'blogposts': blogposts,
    }

    return render(request, 'blog/blog.html', context)


def blog_detail(request, blogpost_id):
    """ A view to display blog detail page """
    
    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    blog_comments = BlogComment.objects.filter(blogpost=blogpost)

    context = {
        'blogpost': blogpost,
        'blogcomments': blogcomments,
    }

    return render(request, 'blog/blog_detail.html', context)