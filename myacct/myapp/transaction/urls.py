from django.urls import path, include
from rest_framework import routers
from transaction.views import ExpenseViewSet

############################################################################

router= routers.DefaultRouter()
router.register('expense', ExpenseViewSet)


############################################################################

