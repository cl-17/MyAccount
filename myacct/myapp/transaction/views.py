from django.shortcuts import render
from django.db.models import Max
from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import list_route

from master.models import Classification, Purpose
from transaction.models import Expense
from transaction.serializer import ExpenseSerializer

from myapp.common import output_log, output_log_dict

############################################################################

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all().order_by('id')
    serializer_class = ExpenseSerializer
    filter_fields = (
        'id',
        'date',
        'purpose',
    )

    @list_route(url_path='get-all')
    def get_all(self, request):
        data = Expense.objects.all().order_by('date').reverse()[:50]
        serializer = ExpenseSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

    @list_route(url_path='get-next-key')
    def get_next_key(self, request):
        return_value = {}
        id = Expense.objects.all().aggregate(Max('id'))['id__max']
        if id is None:
            id = 1
        else:
            id += 1
        return_value['next_key'] = id
        return JsonResponse(return_value)

    @list_route(url_path='input-csv', methods=['post'])
    def input_csv(self, request, *args, **kwargs):
        
        # idの最大値の取得
        id = Expense.objects.all().aggregate(Max('id'))['id__max']
        if id is None:
            id = 0

        for xxx in request.data:
            # idのカウントアップ
            id += 1
            xxx['id'] = id

            # creditの値が'*'なら、Trueに変換
            if xxx['credit'] == '*':
                xxx['credit'] = True
            else:
                xxx['credit'] = False

            # ammountを数値型に変換
            xxx['ammount'] = int(xxx['ammount'])
            
            # c_name、p_nameからpurpose_idへの変換
            classification = Classification.objects.get(name=xxx['c_name'])
            purpose = Purpose.objects.get(name=xxx['p_name'],classification=classification)
            xxx['purpose_id'] = purpose.id

        serializer = ExpenseSerializer(data=request.data, many=True)

        if serializer.is_valid():
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            data = list(serializer.data)
            output_log('good end')
            return Response(data,
                            status=status.HTTP_201_CREATED,
                            headers=headers)
        else:
            output_log('bad end')
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


############################################################################

