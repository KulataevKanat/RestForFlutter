from rest_framework import serializers

from api.models import User
from api.service import WritableSerializerMethodField


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


class UpdateRequestUserSerializer(serializers.ModelSerializer):
    """Изменение пользователя по идентификации"""

    old_password = WritableSerializerMethodField()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'old_password',
            'password',
            'first_name',
            'last_name',
            'groups',
            'is_active',
        ]

    def get_old_password(self, password):
        return password.__str__()


class UpdateResponseUserSerializer(serializers.ModelSerializer):
    """Вывод измененного пользователя по идентификации"""

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
            'last_name',
            'groups',
            'is_active',
        ]
        read_only_fields = [
            'id',
            'is_active',
        ]


class CreateSuperUserSerializer(serializers.ModelSerializer):
    """Добавление супер пользователя"""

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'groups',
        ]

    def create(self, validated_data):
        superuser = User.objects._create_superuser(username=validated_data.__getitem__('username'),
                                                   groups=validated_data.__getitem__('groups'),
                                                   email=validated_data.__getitem__('email'),
                                                   password=validated_data.__getitem__('password'),
                                                   )

        return superuser
