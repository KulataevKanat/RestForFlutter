from django.contrib.auth.models import Group
from rest_framework import generics

from api.serializers import GroupSerializers


class CreateGroupView(generics.CreateAPIView):
    """Добавление группы"""

    serializer_class = GroupSerializers.AllGroupSerializer


class DeleteGroupByIdView(generics.DestroyAPIView):
    """Удаление группы по идентификации"""

    queryset = Group.objects.all()


class UpdateGroupByIdView(generics.UpdateAPIView):
    """Обновление группы по идентификации"""

    queryset = Group.objects.all()
    serializer_class = GroupSerializers.AllGroupSerializer


class GetGroupView(generics.ListAPIView):
    """Вывод групп"""

    queryset = Group.objects.all()
    serializer_class = GroupSerializers.AllGroupSerializer


class FindGroupByIdView(generics.RetrieveAPIView):
    """Поиск группы по идентификации"""

    queryset = Group.objects.all()
    serializer_class = GroupSerializers.AllGroupSerializer
