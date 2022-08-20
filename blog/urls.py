from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:blogpost_id>/', views.blog_detail, name='blog_detail'),
    path('add_blogcomment/<int:blogpost_id>', views.add_blogcomment, name='add_blogcomment')
]
