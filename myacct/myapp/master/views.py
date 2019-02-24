from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from master.models import Classification, Purpose
from master.forms import ClassificationForm_c, ClassificationForm_u, PurposeForm_c, PurposeForm_u
from master.serializer import ClassificationSerializer, PurposeSerializer, UserSerializer

# 以下、Angular用に追加
from rest_framework.response import Response
from rest_framework.decorators import list_route
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Max
from django.db import connection
from django.core import serializers
import json

# 以下、Debug用に追加
import logging

############################################################################

class ClassificationViewSet(viewsets.ModelViewSet):
    queryset = Classification.objects.all().order_by('id')
    serializer_class = ClassificationSerializer
    filter_fields = (
        'id',
        'name',
        'create_user',
    )

    @list_route(url_path='get-all')
    def get_all(self, request):
        data = Classification.objects.all().order_by('id')
        serializer = ClassificationSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

    @list_route(url_path='get-next-key')
    def get_next_key(self, request):
        return_value = {}
        strSQL = 'SELECT TO_CHAR(TO_NUMBER(COALESCE(MAX(id), \'00\'), \'99\') + 1, \'FM00\') AS next_key FROM master_classification'
        with connection.cursor() as cursor:
            cursor.execute(strSQL)
            row = cursor.fetchone()
        return_value['next_key'] = row[0]
        return JsonResponse(return_value)

############################################################################

class PurposeViewSet(viewsets.ModelViewSet):
    queryset = Purpose.objects.all().order_by('id')
    serializer_class = PurposeSerializer
    filter_fields = (
        'id',
        'name',
        'classification',
        'create_user',
    )

    @list_route(url_path='get-all')
    def get_all(self, request):
        data = Purpose.objects.all().order_by('id')
        serializer = PurposeSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

    @list_route(url_path='get-next-key/(?P<c_id>[0-9][0-9])')
    def get_next_key(self, request, c_id):
        return_value = {}
        strSQL = 'SELECT TO_CHAR(TO_NUMBER(COALESCE(MAX(sub_id), \'00\'), \'99\') + 1, \'FM00\') AS next_key FROM master_purpose WHERE classification_id = \'' + c_id + '\' AND NOT sub_id = \'99\''
        with connection.cursor() as cursor:
            cursor.execute(strSQL)
            row = cursor.fetchone()
        return_value['next_key'] = row[0]
        return JsonResponse(return_value)

    @list_route(url_path='get-all-sub/(?P<c_id>[0-9][0-9])')
    def get_all_sub(self, request, c_id):
        data = Purpose.objects.filter(classification=c_id).order_by('sub_id')
        serializer = PurposeSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

############################################################################

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = (
        'username',
    )

    @list_route(url_path='get-user')
    # 仮
    def get_user(self, request):
        return_value = {}
        user = User.objects.get(id=3)
        return_value['id'] = user.id
        return_value['username'] = user.username
        return JsonResponse(return_value)

############################################################################

# TODO ★大体一緒だから、登録と更新で共通化したい
# TODO ★用途マスタも対応して、なるべく共通化したい（分類マスタごとに絞りこみたい）
# TODO 　※画面の追加は面倒だし、２段階構成にするか？
# TODO 分類コード登録時に用途コード99を登録したい（名称はその他で固定）
# TODO →用途コードの99は一覧から除外する？
class Test_c(CreateView):
    model = Classification
    form_class = ClassificationForm_c
    template_name = 'master_maintenance.html'
    master_type = 'classification'

    def get_context_data(self, **kwargs):
        context = super(Test_c, self).get_context_data(**kwargs)
        context['title'] = '分類マスタ（登録）'
        context['master_type'] = self.master_type
        context['primary_key'] = ''
        return context

    def form_valid(self, form):
        classification = form.save(commit=False)
        classification.create_user = self.request.user
        classification.update_user = self.request.user
        classification.save()
        return redirect('list', master_type=self.master_type)

############################################################################

class Test_u(UpdateView):
    model = Classification
    form_class = ClassificationForm_u
    template_name = 'master_maintenance.html'
    pk_url_kwarg = 'primary_key'
    master_type = 'classification'

    def get_context_data(self, **kwargs):
        context = super(Test_u, self).get_context_data(**kwargs)
        context['title'] = '分類マスタ（更新）'
        context['master_type'] = self.master_type
        return context

    def form_valid(self, form):
        classification = form.save(commit=False)
        classification.update_user = self.request.user
        classification.save()
        return redirect('list', master_type=self.master_type)

############################################################################

class Test2_c(CreateView):
    model = Purpose
    form_class = PurposeForm_c
    template_name = 'master_maintenance.html'
    master_type = 'purpose'

    # TODO キーのコードを自動採番するようにしたい（99は除外した最大＋１）
    def get_context_data(self, **kwargs):
        context = super(Test2_c, self).get_context_data(**kwargs)
        context['title'] = '用途マスタ（登録）'
        context['master_type'] = self.master_type
        context['primary_key'] = ''
        return context

    def form_valid(self, form):
        purpose = form.save(commit=False)
        purpose.id = purpose.classification.id + purpose.sub_id
        purpose.create_user = self.request.user
        purpose.update_user = self.request.user
        purpose.save()
        return redirect('list', master_type=self.master_type)

############################################################################

class Test2_u(UpdateView):
    model = Purpose
    form_class = PurposeForm_u
    template_name = 'master_maintenance.html'
    pk_url_kwarg = 'primary_key'
    master_type = 'purpose'

    def get_context_data(self, **kwargs):
        context = super(Test2_u, self).get_context_data(**kwargs)
        context['title'] = '用途マスタ（更新）'
        context['master_type'] = self.master_type
        return context

    def form_valid(self, form):
        purpose = form.save(commit=False)
        purpose.update_user = self.request.user
        purpose.save()
        return redirect('list', master_type=self.master_type)

############################################################################

def master_main(request):
    title = 'マスタメンテナンス'
    d = {
        'title': title,
    }
    return render(request, 'master_main.html', d)

############################################################################

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

############################################################################

def master_list(request, master_type):
    if master_type == 'classification':
        models = Classification.objects.all().order_by('id')
        title = '分類マスタ一覧'
    elif master_type == 'purpose':
        models = Purpose.objects.all().order_by('id')
        title = '用途マスタ一覧'
    d = {
        'title': title,
        'master_type': master_type,
        'models': models,
    }
    return render(request, 'master_list.html', d)

############################################################################

# デバッグ用
def output_log(msg):
    logger = logging.getLogger('command')
    logger.info(msg)

############################################################################


