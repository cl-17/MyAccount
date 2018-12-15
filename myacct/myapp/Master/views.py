import django_filters
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, filters
from .models import Classification
from .serializer import ClassificationSerializer,UserSerializer

# Create your views here.
def master_main(request):
    return render(request, 'master_main.html')

def master_action(request, master_type):
    return render(request, 'master_action.html')

def master_list(request, master_type):
    return render(request, 'master_list.html')

def master_maintenance(request, master_type):
    return render(request, 'master_maintenance.html')

class ClassificationViewSet(viewsets.ModelViewSet):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer
    filter_fields = ('ClassificationCode','CreateUser')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = ('username',)






