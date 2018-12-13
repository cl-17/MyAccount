from rest_framework import routers
from django.urls import path
from . import views
from .views import ClassificationViewSet

urlpatterns = [
    path('', views.master, name='master'),
    path('<str:master>/maintenance', views.maintenance),
    path('<str:master>/maintenance/list', views.list),
]

router= routers.DefaultRouter()
router.register('classification', ClassificationViewSet)






