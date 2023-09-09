"""event URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from eventapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.base,name='base'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('charity',views.charity,name='charity'),
    path('bookevent',views.bookevent,name='bookevent'),
    path('buisness',views.buisness,name='buisness'),
    path('contact',views.contact,name='contact'),
    path('culture',views.culture,name='culture'),
    path('family',views.family,name='family'),
    path('user_cart',views.user_cart,name='user_cart'),
    path('about',views.about,name='about'),
]


urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)