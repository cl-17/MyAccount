from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView
from rest_framework import viewsets, filters
from Master.models import Classification, Purpose
from Master.forms import ClassificationForm, PurposeForm
from Master.serializer import ClassificationSerializer, PurposeSerializer, UserSerializer

############################################################################

class ClassificationViewSet(viewsets.ModelViewSet):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer
    filter_fields = (
        'c_id',
        'c_create_user',
    )

############################################################################

class PurposeViewSet(viewsets.ModelViewSet):
    queryset = Purpose.objects.all()
    serializer_class = PurposeSerializer
    filter_fields = (
        'p_id',
        'c_id',
        'p_create_user',
    )

############################################################################

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = (
        'user_name',
    )

############################################################################

#　★大体一緒だから、登録と更新で共通化したい
#　★用途マスタも対応して、なるべく共通化したい（分類マスタごとに絞りこみたい）
#　　※画面の追加は面倒だし、２段階構成にするか？
#　★最終的な理想は追加ボタンがあって、どっちのマスタも同時に１画面で登録も更新も削除もできるとか？
class Test_c(CreateView):
    model = Classification
    form_class = ClassificationForm
    template_name = 'master_maintenance.html'
    master_type = 'classification'

    def get_context_data(self, **kwargs):
        ctx = super(Test_c, self).get_context_data(**kwargs)
        ctx['title'] = '分類マスタ（登録）'
        ctx['master_type'] = self.master_type
        ctx['primary_key'] = ''
        return ctx

    def form_valid(self, form):
        classification = form.save(commit=False)
        classification.c_create_user = self.request.user
        classification.c_update_user = self.request.user
        classification.save()
        return redirect('list', master_type=self.master_type)

############################################################################

class Test_u(UpdateView):
    model = Classification
    form_class = ClassificationForm
    template_name = 'master_maintenance.html'
    pk_url_kwarg = 'primary_key'
    master_type = 'classification'

    def get_context_data(self, **kwargs):
        context  = super(Test_u, self).get_context_data(**kwargs)
        context ['title'] = '分類マスタ（更新）'
        context ['master_type'] = 'classification'
        return context

    def form_valid(self, form):
        classification = form.save(commit=False)
        classification.c_update_user = self.request.user
        classification.save()
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
        models = Classification.objects.all().order_by('c_id')
        title = '分類マスタ一覧'
    elif master_type == 'purpose':
        models = Purpose.objects.all().order_by('c_id')
        title = '用途マスタ一覧'
    d = {
        'title': title,
        'master_type': master_type,
        'models': models,
    }
    return render(request, 'master_list.html', d)

############################################################################

