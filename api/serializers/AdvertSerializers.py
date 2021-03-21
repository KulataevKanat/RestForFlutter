from rest_framework import serializers

from api.models import Advert
from api.serializers.CategorySerializers import GetCategorySerializer


class CreateAdvertSerializer(serializers.ModelSerializer):
    """Добавление объявления"""

    class Meta:
        model = Advert
        fields = '__all__'


class DeleteAdvertSerializer(serializers.ModelSerializer):
    """Удаление объявления по идентификации"""

    class Meta:
        model = Advert
        fields = '__all__'


class UpdateAdvertSerializer(serializers.ModelSerializer):
    """Обновление объявления по идентификации"""

    class Meta:
        model = Advert
        fields = '__all__'


class GetAdvertSerializer(serializers.ModelSerializer):
    """Вывод объявлений"""
    advert_category = GetCategorySerializer()

    class Meta:
        model = Advert
        fields = [
            'id',
            'advert_category',
            'created',
            'updated',
            'name',
            'description',
            'price',
            'phone',
            'whatsapp',

        ]
