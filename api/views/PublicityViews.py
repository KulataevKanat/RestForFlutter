from rest_framework import generics

from api.models import Publicity
from api.serializers import PublicitySerializers


class CreatePublicityView(generics.CreateAPIView):
    """Добавление рекламы"""

    serializer_class = PublicitySerializers.AllPublicitySerializer


class DeletePublicityByIdView(generics.DestroyAPIView):
    """Удаление рекламы по идентификации"""

    queryset = Publicity.objects.all()

    def perform_destroy(self, instance):
        for image_instance in instance.image.all():
            image_instance.image.delete()
            image_instance.delete()
            instance.delete()


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
