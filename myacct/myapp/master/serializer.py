from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from master.models import Classification, Purpose

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

    id = serializers.CharField(
        required = True,
    )
    name = serializers.CharField(
        required = False,
    )
    create_user_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        write_only = True,
        required = False,
    )
    create_user = UserSerializer(
        read_only = True,
    )
    update_user_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        write_only = True,
        required = True,
    )
    update_user = UserSerializer(
        read_only = True,
    )

    class Meta:
        model = Classification
        fields = (
            'id',
            'name',
            'create_user_id',
            'create_user',
            'update_user_id',
            'update_user',
        )

    def create(self, validated_data):
        
        validated_data['update_user'] = validated_data.get('update_user_id', None)
        if validated_data['update_user'] is None:
            raise serializers.VilidationError('user not found.')
        del validated_data['update_user_id']

        if validated_data.get('create_user_id', None) is None:
            validated_data['create_user'] = validated_data['update_user']
        else:
            validated_data['create_user'] = validated_data.get('create_user_id', None)
            if validated_data['create_user'] is None:
                raise serializers.VilidationError('user not found.')
            del validated_data['create_user_id']
        
        classification = Classification.objects.create(**validated_data)
        return classification

    def update(self, instance, validated_data):

        instance.update_user = validated_data.get('update_user_id', instance.update_user)
        if instance.update_user is None:
            raise serializers.VilidationError('user not found.')
        del validated_data['update_user_id']

        instance.name = validated_data.get('name', instance.name)

        instance.save()
        return instance

############################################################################

class PurposeSerializer(ModelSerializer):

    classification_id = serializers.PrimaryKeyRelatedField(
        queryset = Classification.objects.all(),
        write_only = True,
        required = False,
    )
    classification = ClassificationSerializer(
        read_only = True,
    )
    sub_id = serializers.CharField(
        required = True,
    )
    name = serializers.CharField(
        required = True,
    )
    create_user_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        write_only = True,
        required = False,
    )
    create_user = UserSerializer(
        read_only = True,
    )
    update_user_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        write_only = True,
        required = True,
    )
    update_user = UserSerializer(
        read_only = True,
    )

    class Meta:
        model = Purpose
        fields = (
            'classification_id',
            'classification',
            'sub_id',
            'name',
            'create_user_id',
            'create_user',
            'update_user_id',
            'update_user',
        )

    def create(self, validated_data):

        validated_data['classification'] = validated_data.get('classification_id', None)
        if validated_data['classification'] is None:
            raise serializers.VilidationError('classification not found.')
        del validated_data['classification_id']

        validated_data['update_user'] = validated_data.get('update_user_id', None)
        if validated_data['update_user'] is None:
            raise serializers.VilidationError('user not found.')
        del validated_data['update_user_id']

        if validated_data.get('create_user_id', None) is None:
            validated_data['create_user'] = validated_data['update_user']
        else:
            validated_data['create_user'] = validated_data.get('create_user_id', None)
            if validated_data['create_user'] is None:
                raise serializers.VilidationError('user not found.')
            del validated_data['create_user_id']

        validated_data['id'] = validated_data['classification'].id + validated_data.get('sub_id', None)

        purpose = Purpose.objects.create(**validated_data)
        return purpose

    def update(self, instance, validated_data):
    
        instance.update_user = validated_data.get('update_user_id', instance.update_user)
        if instance.update_user is None:
            raise serializers.VilidationError('user not found.')
        del validated_data['update_user_id']

        instance.name = validated_data.get('name', instance.name)

        instance.save()
        return instance

############################################################################
