from rest_framework import generics

from api.models import Publicity
from api.serializers import PublicitySerializers


class CreatePublicityView(generics.CreateAPIView):
    """Добавление рекламы"""

    serializer_class = PublicitySerializers.AllPublicitySerializer


class DeletePublicityByIdView(generics.DestroyAPIView):
    """Удаление рекламы по идентификации"""

    queryset = Publicity.objects.all()


class UpdatePublicityByIdView(generics.UpdateAPIView):
    """Обновление рекламы по идентификации"""

    queryset = Publicity.objects.all()
    serializer_class = PublicitySerializers.AllPublicitySerializer


class GetPublicityView(generics.ListAPIView):
    """Вывод реклам"""

    queryset = Publicity.objects.all()
    serializer_class = PublicitySerializers.GetPublicitySerializer


class FindPublicityByIdView(generics.RetrieveAPIView):
    """Поиск рекламы по идентификации"""

    queryset = Publicity.objects.all()
    serializer_class = PublicitySerializers.GetPublicitySerializer
