"""allauthdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include, handler404

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/start_page', views.start_page, name="account_start_page"),
    path('accounts/secret_page', views.secret_page, name="account_secret_page"),
    path('accounts/secret_store', views.secret_store, name="account_secret_store"),
    path('accounts/secret_view/<int:secret_id>/', views.secret_view, name="account_secret_view"),
    path('accounts/secret_edit/<int:secret_id>/', views.secret_edit, name="account_secret_edit"),
    url(r'^accounts/', include('allauth.urls')),
]

handler404 = views.handler404
