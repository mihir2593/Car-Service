from django.urls import path, include
from storesapp import views

urlpatterns = [
    path('store-index/', views.storeindex, name='store-index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='services'),
    path('store-register/', views.storeregister, name='store-register'),
    path('store-login/', views.storelogin, name='store-login'),
    path('store-logout/', views.storelogout, name='store-logout'),
    path('addproduct/', views.addproduct, name='add-product'),
    path('addcategory/', views.addcategory,name='add_category'),
    path('addusecategory/', views.addusecategory,name='add-usecate'),
    path('manageusecategory/', views.manageusecate, name='manage-usecate'),
    path('managecategory/', views.managecategory, name='manage-category'),
    path('createinvoice/',views.createinvoice,name='createinvioice'),
    path('manageinvoice/',views.manageinvoice,name='manageinvoice'),
    path('manageproduct/',views.manageproduct,name='manageproduct'),
    path('deleteproduct/<int:id>/', views.deleteproduct, name='deleteproduct'),
    path('deletecategory/<int:id>/', views.deletecategory, name='deletecategory'),
    path('deleteusecate/<int:id>/', views.deleteusecate, name='deleteusecate'),
    path('editproduct/<int:id>/', views.editproduct, name='editproduct'),
    path('editcategory/<int:id>/', views.editcategory, name='editcategory'),
    path('editusecate/<int:id>/', views.editusecate, name='editusecate'),
    path('updateproduct/<int:id>/', views.updateproduct, name='updateproduct'),
    path('updatecategory/<int:id>/', views.updatecategory, name='updatecategory'),
    path('updateusecate/<int:id>/', views.updateusecate, name='updateusecate'),



# ---------For Services-----------------
    path('addstore/', views.addstore, name='addstore'),
    path('managestore/', views.managestore, name='managestore'),
    path('deletestore/<int:id>/', views.deletestore, name='deletestore'),
    path('editstore/<int:id>/', views.editstore, name='editstore'),
    path('updatestore/<int:id>/', views.updatestore, name='updatestore'),
    path('manageservicerequest/', views.manageservicerequest, name='manageservicerequest'),

    path('allorderlist/',views.allorderlist,name='allorderlist'),
    path('acceptservice/<int:id>/', views.acceptservice, name='acceptservice'),
    path('rejectservice/<int:id>/', views.rejectservice, name='rejectservice'),


]
