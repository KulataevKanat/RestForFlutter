from rest_framework import serializers

from api.models import User
from api.serializers import GroupSerializers
from django.contrib.auth.hashers import make_password as encode


class GetUserSerializer(serializers.ModelSerializer):
    """Вывод и Поиск пользователей"""

    groups = GroupSerializers.AllGroupSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password',
                  'first_name', 'last_name', 'groups', 'is_active']


class AuthSerializer(serializers.ModelSerializer):
    """Авторизация, вывод access и refresh токена"""

    class Meta:
        model = User
        fields = ['username', 'password']


class RegistrationSerializer(serializers.ModelSerializer):
    """Регистрация пользователя"""

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password',
                  'first_name', 'last_name']

    def create(self, validated_data):
        user = User.objects.create(username=validated_data.__getitem__('username'),
                                   email=validated_data.__getitem__('email'),
                                   password=encode(validated_data.__getitem__('password')),
                                   first_name=validated_data.__getitem__('first_name'),
                                   last_name=validated_data.__getitem__('last_name'), )

        return user
