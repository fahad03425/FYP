from django.urls import path
from . import views

app_name = 'marketplace'  

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('marketplace/<int:user_id>/', views.main_marketplace, name='main_marketplace'),
    path('marketplace/', views.main_marketplace, name='main_marketplace'),
    path('product-description/', views.description_page, name='productDescriptionPage.html'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('cart/', views.cart, name='cart'),
    path('bookingform/', views.bookingform, name='bookingform'),
]