"""
URL configuration for phonemarketplace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
admin.site.site_header="PhoneKart Administration"
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dg-admin/', admin.site.urls),
    path('', views.home, name='home'),


    path('marketplace/', include('marketplace.urls')),
    path('seller/', include('seller.urls')),
    path('admin/', include('customAdmin.urls')),
    path('', include('django.contrib.auth.urls')),
   

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # For production, serve media files through the web server
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
