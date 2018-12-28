from django.urls import path, include
#from rest_framework import routers
from Master import views
#from Master.views import ClassificationViewSet, PurposeViewSet
from Master.views import Test_c, Test_u

############################################################################

#router= routers.DefaultRouter()
#router.register('classification', ClassificationViewSet)
#router.register('purpose', PurposeViewSet)

############################################################################

urlpatterns = [
    path(r'', views.master_main, name='main'),
    path(r'<str:master_type>', views.master_action, name='action'),
    path(r'<str:master_type>/list', views.master_list, name='list'),
    path(r'<str:master_type>/maintenance', Test_c.as_view(), name='new'),
    path(r'<str:master_type>/maintenance/<str:primary_key>', Test_u.as_view(), name='update'),
    #path(r'<str:master_type>/maintenance', views.master_maintenance, name='new'),
    #path(r'<str:master_type>/maintenance/<str:primary_key>', views.master_maintenance, name='update'),
]

############################################################################

