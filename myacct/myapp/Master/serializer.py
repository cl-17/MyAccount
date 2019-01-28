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
    c_create_user_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        write_only = True,
    )
    c_create_user = UserSerializer(
        read_only = True,
    )
    c_update_user_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        write_only = True,
    )
    c_update_user = UserSerializer(
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
        
        # validated_data['c_create_user'] = validated_data.get('c_create_user_id', None)
        validated_data['c_create_user'] = 3
        if validated_data['c_create_user'] is None:
            raise serializers.VilidationError('user not found.')
        del validated_data['c_create_user_id']
        
        # validated_data['c_update_user'] = validated_data.get('c_update_user_id', None)
        validated_data['c_update_user'] = 3
        if validated_data['c_update_user'] is None:
            raise serializers.VilidationError('user not found.')
        del validated_data['c_update_user_id']

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

    classification_id = serializers.PrimaryKeyRelatedField(
        queryset = Classification.objects.all(),
        write_only = True,
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
    p_create_user_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        write_only = True,
    )
    p_create_user = UserSerializer(
        read_only = True,
    )
    p_update_user_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        write_only = True,
    )
    p_update_user = UserSerializer(
        read_only = True,
    )

    class Meta:
        model = Purpose
        fields = (
            'classification_id',
            'c_id',
            'p_sub_id',
            'p_name',
            'p_create_user_id',
            'p_create_user',
            'p_update_user_id',
            'p_update_user',
        )

    def create(self, validated_data):
        
        validated_data['p_id'] = validated_data.get('c_id', None) + validated_data.get('p_sub_id', None)
        
        validated_data['calssification'] = validated_data.get('c_id', None)
        if validated_data['calssification'] is None:
            raise serializers.VilidationError('classification not found.')
        del validated_data['c_id']

        # validated_data['p_create_user'] = validated_data.get('p_create_user_id', None)
        validated_data['p_create_user'] = 3
        if validated_data['p_create_user'] is None:
            raise serializers.VilidationError('user not found.')
        del validated_data['p_create_user_id']
        
        # validated_data['p_update_user'] = validated_data.get('p_update_user_id', None)
        validated_data['p_update_user'] = 3
        if validated_data['p_update_user'] is None:
            raise serializers.VilidationError('user not found.')
        del validated_data['p_update_user_id']

        purpose = Purpose.objects.create(**validated_data)
        return purpose

    # def update(self, instance, validated_data):
    #     update_user = User.objects.get(pk=1)
    #     instance.p_name = validated_data.get('p_name', instance.p_name)
    #     instance.p_update_user = update_user
    #     instance.save()
    #     return instance

############################################################################

# デバッグ用
def output_log(msg):
    logger = logging.getLogger('command')
    logger.info(msg)

############################################################################
