
from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('search',views.search,name='search'),
    path('login2',views.login,name='login2'),
    path('signup2',views.signup,name='signup2'),



]