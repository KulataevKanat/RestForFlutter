from rest_framework import serializers

from api.models import Advert
from api.serializers.CategorySerializers import GetCategorySerializer
from api.serializers.ImageSerializers import GetImageSerializer


class AllAdvertSerializer(serializers.ModelSerializer):
    """Добавление, Удаление, Изменение объявлений"""

    class Meta:
        model = Advert
        fields = '__all__'


class GetAdvertSerializer(serializers.ModelSerializer):
    """Вывод объявлений"""
    advert_category = GetCategorySerializer()
    image = GetImageSerializer(many=True)

    class Meta:
        model = Advert
        fields = [
            'id',
            'advert_category',
            'created',
            'updated',
            'image',
            'name',
            'description',
            'price',
            'phone',
            'whatsapp',

        ]
