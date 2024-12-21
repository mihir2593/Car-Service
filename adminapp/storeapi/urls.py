from django.contrib import admin
from django.urls import path,include
from storeapi import views
from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    path("addcategory/",views.addcategory),
    path("managecategory/", views.managecategory),
    path('updatecategory/<int:id>/', views.updatecategory),
    path('deletecategory/<int:id>/delete/', views.deletecategory),

    path("addusecategory/", views.addusecategory),
    path("manageusecategory/", views.manageusecategory),
    path("updateusecategory/<int:id>/",views.updateusecategory),
    path('deleteusecategory/<int:id>/delete/', views.deleteusecategory),

    path("addproduct/", views.addproduct),
    path("manageproduct/", views.manageproduct),
    path("updateproduct/<int:id>/", views.updateproduct),
    path('deleteproduct/<int:id>/delete/', views.deleteproduct),

    path("addstore/", views.addstore),
    path("managestore/",views.managestore),
    path("updatestore/<int:id>/", views.updatestore),
    path('deletestore/<int:id>/delete/', views.deletestore),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)