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
        required = True,
    )
    c_create_user = UserSerializer(
        read_only = True,
    )
    c_update_user = UserSerializer(
        read_only = True,
    )

    class Meta:
        model = Classification
        fields = (
            'c_id',
            'c_name',
            'c_create_user',
            'c_update_user',
        )

    def create(self, validated_data):
        create_user = User.objects.get(pk=3)
        update_user = User.objects.get(pk=3)
        classification = Classification.objects.create(c_create_user=create_user, c_update_user=update_user, **validated_data)
        return classification

    def update(self, instance, validated_data):
        update_user = User.objects.get(pk=1)
        instance.c_name = validated_data.get('c_name', instance.c_name)
        instance.c_update_user = update_user
        instance.save()
        return instance

############################################################################

class PurposeSerializer(ModelSerializer):

    p_id = serializers.CharField(
        required = True,
    )
    c_id = ClassificationSerializer(
        read_only = True,
    )
    p_sub_id = serializers.CharField(
        required = True,
    )
    p_name = serializers.CharField(
        required = True,
    )
    p_create_user = UserSerializer(
        read_only = True,
    )
    p_update_user = UserSerializer(
        read_only = True,
    )

    class Meta:
        model = Purpose
        fields = (
            'p_id',
            'c_id',
            'p_sub_id',
            'p_name',
            'p_create_user',
            'p_update_user',
        )

    def create(self, validated_data):
        create_user = User.objects.get(pk=3)
        update_user = User.objects.get(pk=3)
        purpose = Purpose.objects.create(p_create_user=create_user, p_update_user=update_user, **validated_data)
        return purpose

    def update(self, instance, validated_data):
        update_user = User.objects.get(pk=1)
        instance.p_name = validated_data.get('p_name', instance.p_name)
        instance.p_update_user = update_user
        instance.save()
        return instance

############################################################################

# デバッグ用
def output_log(msg):
    logger = logging.getLogger('command')
    logger.info(msg)

############################################################################
