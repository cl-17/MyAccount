import django_filters
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, filters
from .models import Classification, Purpose
from .serializer import ClassificationSerializer, PurposeSerializer, UserSerializer

# Create your views here.
def master_main(request):
    title = 'マスタメンテナンス'
    d = {
        'title': title,
    }
    return render(request, 'master_main.html', d)


def master_action(request, master_type):
    if master_type == 'classification':
        title = '分類マスタ（classification）'
    elif master_type == 'purpose':
        title = '用途マスタ（purpose）'
    d = {
        'title': title,
        'master_type': master_type,
    }
    return render(request, 'master_action.html', d)


def master_list(request, master_type):
    if master_type == 'classification':
        models = Classification.objects.all
        title = '分類マスタ一覧'
    elif master_type == 'purpose':
        models = Purpose.objects.all
        title = '用途マスタ一覧'
    d = {
        'title': title,
        'master_type': master_type,
        'models': models,
    }
    return render(request, 'master_list.html', d)


def master_maintenance(request, master_type, primary_key=''):
    if master_type == 'classification':
        if primary_key != '':
            model = Classification.objects.get(c_id=primary_key)
            title = '分類マスタ（更新）'
        else:
            model = Classification
            title = '分類マスタ（登録）'
    elif master_type == 'purpose':
        if primary_key != '':
            model = Purpose.objects.get(p_id=primary_key)
            title = '用途マスタ（更新）'
        else:
            model = Purpose
            title = '用途マスタ（登録）'
    d = {
        'title': title,
        'master_type': master_type,
        'primary_key': primary_key,
        'model': model,
    }
    return render(request, 'master_maintenance.html', d)


class ClassificationViewSet(viewsets.ModelViewSet):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer
    filter_fields = (
        'c_id',
        'c_create_user',
    )


class PurposeViewSet(viewsets.ModelViewSet):
    queryset = Purpose.objects.all()
    serializer_class = PurposeSerializer
    filter_fields = (
        'p_id',
        'c_id',
        'p_create_user',
    )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = (
        'user_name',
    )
    
