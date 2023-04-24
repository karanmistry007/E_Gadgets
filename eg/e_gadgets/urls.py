from django.contrib import admin
from django.urls import path,include
from . import views
from.views import *

urlpatterns = [
    path('sendmail/',views.sendMail,name='sendmail'),


    #Product Class View
    path('addproduct/',ProjectCreationView.as_view(),name='addproduct'),
    path('updateproduct/<int:pk>',ProductUpdateView.as_view(),name ="updateproduct"),
    path('deleteproduct/<int:pk>',ProductDeleteView.as_view(),name='deleteproduct'),
    path('productdetail/<int:pk>,',ProductDetailView.as_view(),name='productdetail'),
    
    #Category Class View
    path('addcategory/',CategoryCreationView.as_view(),name='addcategory'),
    path('updatecategory/<int:pk>',CategoryUpdateView.as_view(),name='updatecategory'),
    path('deletecategory/<int:pk>',CategoryDeleteView.as_view(),name='deletecategory'),
    path('getcategories/',CategoryDetailView.as_view(),name='getcategories'),

    #Category Class View
    path('addbrand/',BrandCreationView.as_view(),name='addbrand'),
    path('updatebrand/<int:pk>',BrandUpdateView.as_view(),name='updatebrand'),
    path('deletebrand/<int:pk>',BrandDeleteView.as_view(),name='deletebrand'),
    path('getbrands/',BrandDetailView.as_view(),name='getbrands'),
    






    #test
    # path('addfile/',AddFileView.as_view(),name='addfile'),
    # path('filelist/',FileListView.as_view(),name='filelist'),


]