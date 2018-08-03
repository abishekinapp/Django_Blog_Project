


from django.conf.urls import url
from accounts import views  # the '.' means it will serch in the project folder and fid out the file
from django.contrib.auth.views import login,logout

urlpatterns =[
    url(r'^login/',login,{'template_name':'accounts/login.html'},name = 'login'),
    url(r'^logout/',logout,{'template_name':'accounts/logout.html'},name ='logout'),
    url(r'^register/', views.register,name='register'),
    url(r'^profile/', views.profile,name='profile'),
    url(r'^editprofile/', views.editprofile,name='profile'),
    url(r'^changepassword/', views.changepassword,name='profile'),
    url(r'firstpage/', views.firstpage,name='firstpage'),
]
