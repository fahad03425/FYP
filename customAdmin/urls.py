from django.urls import path
from . import views


app_name = 'customAdmin'

urlpatterns = [
    path('', views.adminlogin, name='customAdmin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('registeredsellers/', views.registeredSellers, name='registeredSellers'),
    path('registeredsellerdetail/<int:shopID>/', views.registeredsellerdetails, name='registeredsellerdetail'),

  
    path('newsellers/', views.newsellers, name='newsellers'),
    path('newsellerdetail/<int:shopID>/', views.newsellerdetail, name='newsellerdetail'),



    path('addphone/', views.addphone, name='addphone'),

    path('addcategory/', views.category, name='category'),
    path('addbrand/', views.brand, name='brand'),
    path('addmodel/', views.model, name='model'),
    path('specification/', views.specification, name='specification'),
    path('adminsettings/', views.adminsettings, name='adminsettings'),

    
    
]