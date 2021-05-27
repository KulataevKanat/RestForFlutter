from rest_framework import serializers
from django.contrib.auth.models import Group


class AllGroupSerializer(serializers.ModelSerializer):
    """Добавление, Изменение, Вывод групп"""

    class Meta:
        model = Group
        fields = ['id', 'name']
