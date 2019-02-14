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
from master.urls import router as master_router
from transaction.urls import router as transaction_router

# angular用に追加
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^admin/', admin.site.urls, name='admin'),
    re_path(r'^master/', include('master.urls'), name='master'),
    re_path(r'^master_api/', include(master_router.urls), name='master_router'),
    re_path(r'^transaction_api/', include(transaction_router.urls), name='transaction_router'),
    re_path(r'^angular/.*', TemplateView.as_view(template_name="angular_base.html")),
]

# staticファイル用
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



