
from django.urls import path,include
from . import views


urlpatterns = [

    path('',views.home,name='login'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('admin_index',views.index,name='admin_index'),
    path('postjob',views.postjob,name='postjob'),
    path('find',views.find,name='find'),
    path('update',views.update,name='update'),
    path('delete',views.delete,name='delete'),
    path('logout',views.logout,name='logout'),
    path('viewjob',views.viewjob,name='viewjob'),
    path('deletejob',views.deletejob,name='deletejob'),


]