from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('search',views.search,name='search'),
    path('userdash',views.userdash,name='userdash'),
    path('jobpage',views.jobpage,name='jobpage'),
    path('jobapply',views.jobapply,name='jobapply'),
    path('logout',views.logout,name='logout'),
    path('deletejob2', views.deletejob2, name='deletejob2'),






]