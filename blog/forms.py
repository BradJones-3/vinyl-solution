from django import forms
from .widgets import CustomClearableFileInput
from .models import BlogPost, BlogComment


class BlogForm(forms.ModelForm):
    """ Creates a Form to allow users to add Blog Posts """

    class Meta:
        model = BlogPost
        fields = (
            'blog_title',
            'blog_preview',
            'blog_body',
            'image_url',
            'image',
        )

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)


class CommentForm(forms.ModelForm):
    """ Create comment form for blog posts """

    class Meta:
        model = BlogComment
        fields = (
            'comment_title',
            'comment',
        )
