# coding: utf-8
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Classification

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class ClassificationSerializer(serializers.ModelSerializer):

    CreateUser = UserSerializer()
    UpdateUser = UserSerializer()

    class Meta:
        model = Classification
        fields = ('ClassificationCode','ClassificationName','CreateUser','CreateDate','UpdateUser','UpdateDate')


