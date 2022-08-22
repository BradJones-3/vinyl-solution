from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('add_blogpost/', views.add_blogpost, name='add_blogpost'),
    path('<int:blogpost_id>/', views.blog_detail, name='blog_detail'),
    path('edit_blogpost/<int:blogpost_id>',
         views.edit_blogpost, name='edit_blogpost'),
    path('delete_blogpost/<int:blogpost_id>',
         views.delete_blogpost, name='delete_blogpost'),
    path('add_blogcomment/<int:blogpost_id>',
         views.add_blogcomment, name='add_blogcomment'),
    path('edit_blogcomment/<int:blogpost_id>',
         views.edit_blogcomment, name='edit_blogcomment'),
]
