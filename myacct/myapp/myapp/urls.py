"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from Master.urls import router as master_router

from Master.views import get_classfication
from django.views.generic.base import TemplateView

urlpatterns = [
    path(r'admin/', admin.site.urls, name='admin'),
    path(r'master/', include('Master.urls'), name='master'),
    path(r'master_api/', include(master_router.urls), name='master_router'),
    path(r'^get_classfication/', get_classfication),
    path(r'^.*', TemplateView.as_view(template_name="angular_base.html"), name="angular_base"),
]





