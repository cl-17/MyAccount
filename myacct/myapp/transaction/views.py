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

import pandas as pd
from django_pandas.io import read_frame

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

        for rowData in request.data:
            # idのカウントアップ
            id += 1
            rowData['id'] = id

            # creditの値が'*'なら、Trueに変換
            if ('credit' in rowData) and rowData['credit'] == '*':
                rowData['credit'] = True
            else:
                rowData['credit'] = False

            # ammountを数値型に変換
            rowData['ammount'] = int(rowData['ammount'])
            
            # c_name、p_nameからclassification_id、sub_idへの変換
            classification = Classification.objects.get(name=rowData['c_name'])
            purpose = Purpose.objects.get(name=rowData['p_name'],classification=classification)
            rowData['classification_id'] = classification.id
            rowData['sub_id'] = purpose.sub_id

        serializer = ExpenseSerializer(data=request.data, many=True)

        if serializer.is_valid():
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            data = list(serializer.data)
            return Response(data,
                            status=status.HTTP_201_CREATED,
                            headers=headers)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @list_route(url_path='get-pandas-result')
    def get_pandas_result(self, request):
        expense_data = Expense.objects.all()
        df_expense_data = read_frame(expense_data)

        df_expense_data_r = df_expense_data.reset_index()
        valiables = ['date', 'purpose', 'ammount', 'credit']

        result = df_expense_data_r[valiables].to_html()
        return Response(result)

############################################################################

