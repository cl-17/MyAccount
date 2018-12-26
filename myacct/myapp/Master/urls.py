from django.urls import path, include
from rest_framework import routers

from Master import views
from Master.views import ClassificationViewSet, PurposeViewSet

router= routers.DefaultRouter()
router.register('classification', ClassificationViewSet)
router.register('purpose', PurposeViewSet)

urlpatterns = [
    path('', views.master_main, name='main_master'),
    path('router/', include(router.urls)),
    path('<str:master_type>', views.master_action),
    path('<str:master_type>/list', views.master_list),
    path('<str:master_type>/maintenance/', views.master_maintenance),
    path('<str:master_type>/maintenance/<str:primary_key>', views.master_maintenance),
]


