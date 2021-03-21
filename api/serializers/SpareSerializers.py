from rest_framework import serializers

from api.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для вывода всех данных по категории"""

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'main_category'
        ]
        depth = 10
