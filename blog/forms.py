from django import forms
from .models import BlogComment


class CommentForm(forms.ModelForm):
    """ Create comment form for blog posts """

    class Meta:
        model = BlogComment
        fields = (
            'comment_title',
            'comment',
        )
