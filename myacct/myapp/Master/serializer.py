# coding: utf-8
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Classification, Purpose

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'user_name',
        )

class ClassificationSerializer(serializers.ModelSerializer):

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

'''
    def create(self, validated_data):
        return Classification(**validated_data)

    def update(self, instance, validated_data):
        instance.c_create_user = validated_data.get('c_create_user', instance.c_create_user)
        instance.c_create_date = validated_data.get('c_create_date', instance.c_create_date)
        instance.c_update_user = validated_data.get('c_update_user', instance.c_update_user)
        instance.c_update_date = validated_data.get('c_update_date', instance.c_update_date)
        return instance
'''

class PurposeSerializer(serializers.ModelSerializer):

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
            'p_create_date',
            'p_update_user',
            'p_update_date',
        )


