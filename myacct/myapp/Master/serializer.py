from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from Master.models import Classification, Purpose

# 以下、Debug用に追加
import logging

############################################################################

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
        )

############################################################################

class ClassificationSerializer(ModelSerializer):

    c_create_user = UserSerializer()
    c_update_user = UserSerializer()

    class Meta:
        model = Classification
        fields = (
            'c_id',
            'c_name',
            'c_create_user',
            'c_create_date',
            'c_update_user',
            'c_update_date',
        )
    
    def create(self, validated_data):
        classification = Classification(**validated_data)
        if classification.c_create_user == '':
            classification.c_create_user = User.objects.get(id=3)
        if classification.c_update_user == '':
            classification.c_update_user = User.objects.get(id=3)
        return classification

############################################################################

class PurposeSerializer(ModelSerializer):

    p_create_user = UserSerializer()
    p_update_user = UserSerializer()
    c_id = ClassificationSerializer()

    class Meta:
        model = Purpose
        fields = (
            'p_id',
            'p_name',
            'c_id',
            'p_sub_id',
            'p_create_user',
            'p_create_date',
            'p_update_user',
            'p_update_date',
        )

############################################################################


