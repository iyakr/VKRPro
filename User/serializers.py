from rest_framework import serializers
from . import models
from django.contrib.auth.models import User,Group
from .models import Profile


class UserSerialiser(serializers.ModelSerializer):
    """Сериализация пользователя"""
    class Meta:
        model = User
        fields = ("id", "username", "email")

class RegSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("username", "email", "password")
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            username=validated_data['username'],
            password = validated_data['password'],
        )

        return user

class RedactSerialiser(serializers.ModelSerializer):
    """Сериализация редактирования пользователя"""
    class Meta:
        model = User
        fields = ("id","username", "email")

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        # group = Group.objects.get(name='Sportsmans')
        # group = Group.objects.get(name='Protocolist')
        # user.groups.add(group)
        return user

    class Meta:
        model = User
        fields = ('id',  'email', 'password', 'auth_token','username')
        read_only_fields = ('auth_token',)
        extra_kwargs = {'password': {'write_only': True}}

    def create_user(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
               )

        user.set_password(validated_data['password'])
        user.save()
        return user



class ProfileSerializer(serializers.ModelSerializer):
    """Сериализация профиля"""
    user = UserSerialiser()
    class Meta:
        model = Profile
        fields = ('id','user','fioP','yearbirthP','sexP','rankP','fiocoachP')
class GroupSerialiser(serializers.ModelSerializer):
    model = Group
    fields = ('name')

class ProfileRedact(serializers.ModelSerializer):
    user = UserSerialiser()
    class Meta:
        model = Profile
        fields = ( 'user')


class EditEmail(serializers.ModelSerializer):
    """Редактирование email"""
    class Meta:
        model = User
        fields = ("email", )


class WatchRegInfo(serializers.ModelSerializer):
    # groups = GroupSerialiser(many=True)
    class Meta:
        model = User
        fields = ('id',  'email', 'password', 'auth_token','username','groups')

