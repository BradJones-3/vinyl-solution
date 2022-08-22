from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import BlogPost, BlogComment
from .forms import BlogForm, CommentForm


def blog(request):
    """ Displays All Blog Posts """

    blogposts = BlogPost.objects.all()

    context = {
        'blogposts': blogposts,
    }

    return render(request, 'blog/blog.html', context)

@login_required
def add_blogpost(request):
    """ Adds a new Post in the Blog section """

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you need to be\
            registered to add a new post!')
        return redirect(reverse('blog'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost = form.save()
            messages.success(request, 'Your Post Has Been Added Successfully!')
            return redirect(reverse('blog_detail', args=[blogpost.id]))
        else:
            messages.error(request, 'Error! Your Post Was Not Added!\
                Please Ensure The Post Is Valid')
    else:
        form = BlogForm()
    template = 'blog/add_blogpost.html'
    context = {
        'form': form
    }

    return render(request, template, context)


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
def delete_blogpost(request, blogpost_id):
    """ Deletes Blog Post from Database """

    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)

    if request.user == blogpost.author or request.user.is_superuser:
        blogpost.delete()
        messages.info(request, "Blog Post Has Successfully Been Deleted")
        return redirect(reverse('blog'))
    else:
        messages.error(
            request, "Sorry You Didn't Create This Post \
                So You Are Not Authorised To Delete It.")
        return redirect(reverse('blog'))


@login_required
def edit_blogpost(request, blogpost_id):
    """ Allows the creator or superuser to edit A Blogpost """

    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)

    if request.user == blogpost.author or request.user.is_superuser:
        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES, instance=blogpost)
            if form.is_valid():
                form.save()
                messages.info(request, 'Successfully Edited Blog Post!')
                return redirect(reverse('blog_detail', args=[blogpost.id]))
            else:
                messages.error(request, 'Blog Post Failed To Update \
                    Please Make Sure The Form Is Valid.')
        else:
            form = BlogForm(instance=blogpost)
    else:
        messages.error(request, 'Only The Author And \
            Admin Can Edit This Blog Post')
        return redirect(reverse('home'))

    template = 'blog/edit_blogpost.html'
    context = {
        'form': form,
        'blogpost': blogpost
    }

    return render(request, template, context)















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
            messages.success(request, f'Thank you for your comment on\
                {blogpost.blog_title}')
            return redirect(reverse('blog_detail', args=[blogpost.id]))
        else:
            messages.error(request,
                           "Sorry your comment couldn't be added!\
                               Please Try Again")
    else:
        form = CommentForm(instance=blogpost)
    template = 'blog/add_blogcomment.html'
    context = {
        'form': form,
        'blogpost': blogpost,
    }

    return render(request, template, context)



