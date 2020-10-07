
from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='index'),

    path('about',views.about,name='about'),
    path('blog',views.blog,name='blog'),
    path('contact',views.contact,name='contact'),

    path('search',views.search,name='search'),
    path('login2',views.login,name='login2'),
    path('signup2',views.signup,name='signup2'),
    path('userdash',views.userdash,name='userdash'),
    path('jobpage',views.jobpage,name='jobpage'),
    path('jobapply',views.jobapply,name='jobapply'),
    path('loggedin',views.loggedin,name='loggedin')

]