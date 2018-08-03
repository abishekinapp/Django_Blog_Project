
from django.conf.urls import url
from home.views import HomeView
from home import views


urlpatterns =[

    url(r'^$',HomeView.as_view(),name ='home'),
    #url(r'^<int:pk>/',views.post_detail, name='post_detail'),
    url(r'^postlist/',views.postlist,name ='postlist'),
    url(r'post_detail/(?P<pk>\d+)/', views.post_detail, name='post_detail'),
    url(r'add_comment/', views.add_comment, name='add_comment'),
    url(r'post_edit/(?P<pk>\d+)/', views.post_edit, name='post_edit'),
    url(r'post_remove/(?P<pk>\d+)/', views.post_remove, name='post_remove'),
    url(r'^post_like/(?P<pk>\d+)/', views.like, name = 'like'),

]
