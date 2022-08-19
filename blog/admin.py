from django.contrib import admin
from .models import BlogPost, BlogComment


class PostAdmin(admin.ModelAdmin):
    """ Changes the display in the admin page """
    list_display = ('blog_title',
                    'author',
                    'blog_body',
                    'date_created')



class BlogCommentAdmin(admin.ModelAdmin):
    """ Creates the admin interface for Blog Comment """

    list_display = (
        'comment_title',
        'comment',
        'blogpost',
        'comment_user',
    )


admin.site.register(BlogPost, PostAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
