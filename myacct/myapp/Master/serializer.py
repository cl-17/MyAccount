from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from Master.models import Classification, Purpose

# 以下、Debug用に追加
import logging

############################################################################

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
        )

############################################################################

class ClassificationSerializer(ModelSerializer):

    c_id = serializers.CharField(
        required = True,
    )
    c_name = serializers.CharField(
        required = False,
    )
    c_create_user_id = serializers.IntegerField(
        write_only = True,
    )
    c_create_user = serializers.CharField(
        source='c_create_user.username',
        read_only = True,
    )
    c_update_user_id = serializers.IntegerField(
        write_only = True,
    )
    c_update_user = serializers.CharField(
        source='c_update_user.username',
        read_only = True,
    )

    class Meta:
        model = Classification
        fields = (
            'c_id',
            'c_name',
            'c_create_user_id',
            'c_create_user',
            'c_update_user_id',
            'c_update_user',
        )

    def create(self, validated_data):
        create_user = User.objects.get(pk=validated_data.pop('c_create_user_id'))
        update_user = User.objects.get(pk=validated_data.pop('c_update_user_id'))
        classification = Classification.objects.create(c_create_user=create_user, c_update_user=update_user, **validated_data)
        return classification

############################################################################

class PurposeSerializer(ModelSerializer):

    c_id = ClassificationSerializer()
    p_create_user = UserSerializer()
    p_update_user = UserSerializer()

    class Meta:
        model = Purpose
        fields = (
            'p_id',
            'p_name',
            'c_id',
            'p_sub_id',
            'p_create_user',
            'p_update_user',
        )

############################################################################


