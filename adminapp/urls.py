from django.urls import path, include
from adminapp import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('admin-register/',views.adminregister,name='admin-register'),
    path('admin-login/', views.adminlogin, name='admin-login'),
    path('admin-logout/', views.adminlogout, name='admin-logout'),

]
