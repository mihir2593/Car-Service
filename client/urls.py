from django.urls import path, include
from client import views

urlpatterns = [
    path('clientindex/', views.clientindex, name='clientindex'),
    path('clientabout/', views.clientabout, name='clientabout'),
    path('clientcontact/', views.clientcontact, name='cliencontact'),
    path('clientservice/', views.clientservice, name='clientservice'),
    path('client-register/', views.clientregister, name='client-register'),
    path('client-login/', views.clientlogin, name='client-login'),
    path('client-logout/', views.clientlogout, name='client-logout'),
    path('myprofile/',views.myprofile,name='myprofile'),
    path('product/', views.storeproduct, name='cl-product'),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),
    path('storelist/',views.storelist,name='storelist'),
    path('servicerequest/<int:id>/',views.requestservice,name='servicerequest'),
    path('myservice/',views.myservices,name='myservice'),
    path('myorder/',views.myorder,name='myorder'),
    path('confirmorder/',views.confirmorder,name='confirmorder'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('productinvoice/<int:id>/', views.productinvoice, name='productinvoice'),
    path('download-invoice/<int:order_id>/', views.download_invoice_pdf, name='download_invoice_pdf'),
]
