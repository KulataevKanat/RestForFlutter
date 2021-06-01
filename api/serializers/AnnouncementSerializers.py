from rest_framework import serializers

from api.models import Announcement
from api.serializers.CategorySerializers import GetCategorySerializer
from api.serializers.ImageSerializers import GetImageSerializer


class CreateAnnouncementSerializer(serializers.ModelSerializer):
    """Добавление объявления"""

    class Meta:
        model = Announcement
        fields = '__all__'


class UpdateAnnouncementSerializer(serializers.ModelSerializer):
    """Обновление объявления по идентификации"""

    class Meta:
        model = Announcement
        fields = '__all__'


class GetAnnouncementSerializer(serializers.ModelSerializer):
    """Вывод объявлений"""

    announcement_category = GetCategorySerializer()
    image = GetImageSerializer(many=True)

    class Meta:
        model = Announcement
        fields = [
            'id',
            'announcement_category',
            'created',
            'updated',
            'name',
            'description',
            'image',
            'price',
            'phone',
            'whatsapp',

        ]
