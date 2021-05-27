from rest_framework import serializers

from api.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для вывода всех данных у категории"""

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'main_category'
        ]
        depth = 10


class NotSerializer(serializers.Serializer, object):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
