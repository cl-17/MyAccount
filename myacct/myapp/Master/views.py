import django_filters
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, filters
from .models import Classification,Purpose
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

    if master_type == 'classification':
        models = Classification.objects.all
    elif master_type == 'purpose':
        models = Purpose.objects.all

    dict = {
        'models': models,
        'master_type': master_type,
    }

    return render(request, 'master_list.html', dict)


def master_maintenance(request, master_type, primary_key=''):

    if master_type == 'classification':
        if primary_key != '':
            model = Classification.objects.get(ClassificationCode=primary_key)
        else:
            model = Classification

    elif master_type == 'purpose':
        if primary_key != '':
            model = Purpose.objects.get(PurposeCode=primary_key)
        else:
            model = Purpose

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






