from rest_framework import serializers

from api.models import User


class GetUserSerializer(serializers.ModelSerializer):
    """Вывод и Поиск пользователей"""

    groups = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'groups',
            'is_active'
        ]


class AuthSerializer(serializers.ModelSerializer):
    """Авторизация, вывод access и refresh токена"""

    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]


class UpdateUserSerializer(serializers.ModelSerializer):
    """Изменение пользователя"""

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'groups',
            'is_active',
        ]


class RegistrationSerializer(serializers.ModelSerializer):
    """Регистрация пользователя"""

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'first_name',
            'last_name'
        ]
        read_only_fields = [
            'is_active',
        ]
