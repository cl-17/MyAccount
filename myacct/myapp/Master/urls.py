from django.urls import path, include
from rest_framework import routers

from Master import views
from Master.views import ClassificationViewSet, PurposeViewSet

router= routers.DefaultRouter()
router.register('classification', ClassificationViewSet)
router.register('purpose', PurposeViewSet)

urlpatterns = [
    path(r'', views.master_main, name='main_master'),
    path(r'router/', include(router.urls)),
    path(r'<str:master_type>', views.master_action),
    path(r'<str:master_type>/list', views.master_list),
    path(r'<str:master_type>/maintenance/', views.master_maintenance),
    path(r'<str:master_type>/maintenance/<str:primary_key>', views.master_maintenance),
]


