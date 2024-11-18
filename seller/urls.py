from django.urls import path
from . import views


app_name = 'seller'

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('registration/', views.registration, name='registration'),
    path('registrationdone/', views.regdone, name='registerdone'),
    path('portal/', views.portal, name='portal'),
    path('addproducts/', views.addproducts, name='addproducts'),
    path('listedproducts/', views.listedproducts, name='listedproducts'),
    path('ordermanagement/', views.ordermanagement, name='orderManagement'),
    path('analytics/', views.analytics, name='analytics'),
    path('support/', views.support, name='support'),
    path('mystore/', views.mystore, name='mystore'),
    path('payments/', views.payments, name='payments'),
    path('accountsettings/', views.accountsettings, name='accountsettings'),
    
    
]