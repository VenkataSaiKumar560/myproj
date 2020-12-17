"""myproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.register,name='register'),

    path('home/',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('edit/<str:num>/',views.edit,name='edit'),
    path('seek/',views.seek,name='seek'),
    path('help/',views.help,name='help'),
    path('another/<str:ma>/',views.another,name='another'),
    path('help2/<int:num>/',views.help2,name='help2'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),



]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


