from django.urls import path

from Shop import views

urlpatterns=[
     path('',views.home),
     path('signup',views.signup,name='signup'),
     path('login',views.login,name='login')
     ]