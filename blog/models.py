from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    """ Create's A Blog Entry In The Database """

    blog_title = models.CharField(max_length=80, null=True, blank=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField(
        auto_now_add=True, null=True)
    blog_preview = models.CharField(max_length=254, null=True, blank=True)
    blog_body = models.TextField()
    blog_image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.blog_title


class BlogComment(models.Model):
    """ Create blog comment model to database """

    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_date = models.DateField(auto_now_add=True)
    comment_title = models.CharField(max_length=50, null=False, blank=False)
    comment = models.TextField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.comment_title