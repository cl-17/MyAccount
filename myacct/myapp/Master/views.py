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

    dict = {
        'master_type': master_type,
    }

    return render(request, 'master_action.html', dict)


def master_list(request, master_type):

    models = Classification.objects.all

    dict = {
        'models': models,
        'master_type': master_type,
    }

    return render(request, 'master_list.html', dict)


def master_maintenance(request, master_type, primary_key=''):

    if primary_key != '':
        model = Classification.objects.get(ClassificationCode=primary_key)
    else:
        model = Classification

    dict = {
        'master_type': master_type,
        'primary_key': primary_key,
        'model': model,
    }

    return render(request, 'master_maintenance.html', dict)


class ClassificationViewSet(viewsets.ModelViewSet):

    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer
    filter_fields = ('ClassificationCode','CreateUser')


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = ('username',)






