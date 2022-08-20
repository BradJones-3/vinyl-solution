from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import BlogPost, BlogComment
from .forms import CommentForm


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
    blogcomments = BlogComment.objects.filter(blogpost=blogpost)

    context = {
        'blogpost': blogpost,
        'blogcomments': blogcomments,
    }

    return render(request, 'blog/blog_detail.html', context)


@login_required
def add_blogcomment(request, blogpost_id):
    """ Adds comment and attaches to  post """

    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # Saves comment to database
            blogcomment = form.save(commit=False)
            blogcomment.comment_user = request.user
            blogcomment.blogpost = blogpost
            blogcomment.save()
            messages.success(request, f'Thank you for your comment on {blogpost.blog_title}')
            return redirect(reverse('blog_detail', args=[blogpost.id]))
        else:
            messages.error(request,
                           "Sorry your comment couldn't be added! Please Try Again")
    else:
        form = CommentForm(instance=blogpost)
    template = 'blog/add_blogcomment.html'
    context = {
        'form': form,
        'blogpost': blogpost,
    }

    return render(request, template, context)
