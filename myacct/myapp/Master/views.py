from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView
from rest_framework import viewsets
from Master.models import Classification, Purpose
from Master.forms import ClassificationForm_c, ClassificationForm_u, PurposeForm_c, PurposeForm_u
from Master.serializer import ClassificationSerializer, PurposeSerializer, UserSerializer

# 以下、Angular用に追加
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

############################################################################

class ClassificationViewSet(viewsets.ModelViewSet):
    queryset = Classification.objects.all().order_by('c_id')
    serializer_class = ClassificationSerializer
    filter_fields = (
        'c_id',
        'c_create_user',
    )

############################################################################

class PurposeViewSet(viewsets.ModelViewSet):
    queryset = Purpose.objects.all().order_by('p_id')
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
        classification.c_create_user = self.request.user
        classification.c_update_user = self.request.user
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
        classification.c_update_user = self.request.user
        classification.save()
        return redirect('list', master_type=self.master_type)

############################################################################

class Test2_c(CreateView):
    model = Purpose
    form_class = PurposeForm_c
    template_name = 'master_maintenance.html'
    master_type = 'purpose'

    # TODO 分類コードのリストのソート順を変えたい
    # TODO キーのコードを自動採番するようにしたい（99は除外した最大＋１）
    def get_context_data(self, **kwargs):
        context = super(Test2_c, self).get_context_data(**kwargs)
        context['title'] = '用途マスタ（登録）'
        context['master_type'] = self.master_type
        context['primary_key'] = ''
        return context

    def form_valid(self, form):
        purpose = form.save(commit=False)
        purpose.p_id = purpose.c_id.c_id + purpose.p_sub_id
        purpose.p_create_user = self.request.user
        purpose.p_update_user = self.request.user
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
        purpose.p_update_user = self.request.user
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
        models = Classification.objects.all().order_by('c_id')
        title = '分類マスタ一覧'
    elif master_type == 'purpose':
        models = Purpose.objects.all().order_by('p_id')
        title = '用途マスタ一覧'
    d = {
        'title': title,
        'master_type': master_type,
        'models': models,
    }
    return render(request, 'master_list.html', d)

############################################################################

# 以下、Angular用に追加
@csrf_exempt
def get_classification(request):
    data = Classification.objects.all().order_by('c_id')
    if request.method == 'GET':
        serializer = ClassificationSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

