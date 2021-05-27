from rest_framework import serializers

from api.models import Publicity
from api.serializers.ImageSerializers import GetImageSerializer


class AllPublicitySerializer(serializers.ModelSerializer):
    """Добавление, Обновление рекламы"""

    class Meta:
        model = Publicity
        fields = [
            'id',
            'image',
            'link',
        ]


class GetPublicitySerializer(serializers.ModelSerializer):
    """Вывод реклам"""

    # image = GetImageSerializer(many=True)

    class Meta:
        model = Publicity
        fields = [
            'id',
            'image',
            'link',
            'created',
            'updated',
        ]
