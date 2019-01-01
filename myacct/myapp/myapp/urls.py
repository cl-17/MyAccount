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
from django.urls import include, re_path
from Master.urls import router as master_router

# angular用に追加
from Master.views import get_classification
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^admin/', admin.site.urls, name='admin'),
    re_path(r'^master/', include('Master.urls'), name='master'),
    re_path(r'^master_api/', include(master_router.urls), name='master_router'),
    re_path(r'^angular/.*', TemplateView.as_view(template_name="angular_base.html")),
    re_path(r'^get_classification/', get_classification),
]

# staticファイル用
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



