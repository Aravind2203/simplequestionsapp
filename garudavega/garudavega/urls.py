"""garudavega URL Configuration

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
from garudavegaapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('detail/<int:pk>',detail,name='detail'),
    path('login/',login_user,name='login'),
    path('logout/',logout_user,name='logout'),
    path('anser/<str:args>/<int:pk>',answer,name='a'),
    path('register/',rergister_user,name='register'),
    path('addanswer/<str:args>/<int:pk>',answer_to_be_added,name='answera'),
    path('create/<str:args>',create_post,name='createpost'),
]
