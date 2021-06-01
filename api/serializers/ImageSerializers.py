from rest_framework import serializers

from api.models import Image
from versatileimagefield.serializers import VersatileImageFieldSerializer


class AllImageSerializer(serializers.ModelSerializer):
    """Добавление, Обновление изображений"""

    class Meta:
        model = Image
        fields = [
            'id',
            'name',
            'image'
        ]


class GetImageSerializer(serializers.ModelSerializer):
    """Вывод изображений"""

    image = VersatileImageFieldSerializer(sizes="image_headshot")

    class Meta:
        model = Image
        fields = [
            'id',
            'name',
            'image'
        ]
