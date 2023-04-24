from django.contrib import admin
from django.urls import path,include
from .views import *
from django.contrib.auth.views import LogoutView
from . import views



urlpatterns = [
 
 path('userregister/',UserRegisterView.as_view(),name='userregister'),
  path('user_update/<int:pk>',UserUpdateView.as_view(),name='user_update'),
 path('vendorregister/',VendorRegisterView.as_view(),name='vendorregister'),
 path('login/',UserLoginView.as_view(),name='login'),
 path('logout/',LogoutView.as_view(),name='logout'),
 path('user/dashboard/',UserDashBoardView.as_view(),name='user_dashboard'),   
 path('vendor/dashboard/',VendorDashboardView.as_view(),name='vendor_dashboard'),
 path('vendor/details/<int:id>',VendorDetails.as_view(),name='vendor_details'),
 path('user/contact/',Contact.as_view(),name='contact'), 
#  path('user/cart/',Cart.as_view(),name='cart'),
 path('user/checkout/<int:pk>',UserCheckoutView.as_view(),name='checkout'),
 path('user/about.html',About.as_view(),name='about'),
 #cart
 path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
 path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
 path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
 path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
 path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
 path('cart',views.cart_detail,name='cart'),
]