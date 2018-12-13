# coding: utf-8
from rest_framework import serializers
from .models import Classification

class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = ('ClassificationCode','ClassificationName','CreateUser','CreateDate','UpdateUser','UpdateDate')


