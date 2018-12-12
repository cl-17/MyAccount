from django.urls import path
from . import views

urlpatterns = [
    path('', views.master, name='master'),
    path('classification/', views.classification, name='classification')
]
