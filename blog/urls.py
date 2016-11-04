from django.conf.urls import url
from  .import views

urlpatterns =    [

    url(r'^$', views.post_list),

    url(r'^(?P<id>\d+)/$', views.post_details, name='post_detail'),

    url(r'^post/new/$', views.new_post, name='new_post'),


    url(r'^(?P<id>\d+)/edit$', views.edit_post),

    # url(r'^blog/$',views.blog_posts,name='blog_posts'),
    # url(r'^blog/(?P<id>\d+)/$',views.post_detail),
    # url(r'^blog/post/new/$',views.new_post, name='new_post'),
]