from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from master.models import Purpose
from master.serializer import PurposeSerializer
from transaction.models import Expense

# 以下、Debug用に追加
import logging


class ExpenseSerializer(ModelSerializer):

    id = serializers.CharField(
        required = False,
    )
    date = serializers.DateField(
        required = True,
    )
    purpose_id = serializers.PrimaryKeyRelatedField(
        queryset = Purpose.objects.all(),
        write_only = True,
        required = False,
    )
    purpose = PurposeSerializer(
        read_only = True,
    )
    ammount = serializers.DecimalField(
        required = True,
        max_digits=8,
        decimal_places=0,
    )
    credit = serializers.BooleanField(
        required = True,
    )

    class Meta:
        model = Expense
        fields = (
            'id',
            'date',
            'purpose_id',
            'purpose',
            'ammount',
            'credit',
        )



