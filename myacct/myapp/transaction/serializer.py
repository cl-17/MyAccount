from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from master.models import Purpose
from master.serializer import PurposeSerializer
from transaction.models import Expense

from myapp.common import output_log, output_log_dict

class ExpenseSerializer(ModelSerializer):

    id = serializers.CharField(
        required = False,
    )
    date = serializers.DateField(
        required = True,
    )
    classification_id = serializers.CharField(
        write_only = True,
        required = False,
    )
    sub_id = serializers.CharField(
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
        required = False,
    )

    class Meta:
        model = Expense
        fields = (
            'id',
            'date',
            'classification_id',
            'sub_id',
            'purpose',
            'ammount',
            'credit',
        )

    def create(self, validated_data):

        classification_id = validated_data.get('classification_id', None)
        sub_id = validated_data.get('sub_id', None)
        purpose_id = classification_id + sub_id
        validated_data['purpose'] = Purpose.objects.get(pk=purpose_id)
        if validated_data['purpose'] is None:
            raise serializers.VilidationError('purpose not found.')
        del validated_data['classification_id']
        del validated_data['sub_id']

        expense = Expense.objects.create(**validated_data)
        return expense

    def update(self, instance, validated_data):

        classification_id = validated_data.get('classification_id', None)
        sub_id = validated_data.get('sub_id', None)
        purpose_id = classification_id + sub_id
        instance.purpose = Purpose.objects.get(pk=purpose_id)
        if instance.purpose is None:
            raise serializers.VilidationError('purpose not found.')
        del validated_data['classification_id']
        del validated_data['sub_id']

        instance.date = validated_data.get('date', instance.date)
        instance.ammount = validated_data.get('ammount', instance.ammount)
        instance.credit = validated_data.get('credit', instance.credit)

        instance.save()
        return instance

