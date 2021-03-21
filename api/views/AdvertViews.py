from rest_framework import generics, filters

from api.models import Advert
from api.serializers import AdvertSerializers
from django_filters import rest_framework as filterss

from api.service import AdvertFilterSet


class CreateAdvertView(generics.CreateAPIView):
    """Добавление объявления"""

    serializer_class = AdvertSerializers.CreateAdvertSerializer


class DeleteAdvertByIdView(generics.DestroyAPIView):
    """Удаление объявления по идентификации"""

    queryset = Advert.objects.all()
    serializer_class = AdvertSerializers.DeleteAdvertSerializer


class UpdateAdvertByIdView(generics.UpdateAPIView):
    """Обновление объявления по идентификации"""

    queryset = Advert.objects.all()
    serializer_class = AdvertSerializers.UpdateAdvertSerializer


class GetAdvertView(generics.ListAPIView):
    """Вывод объявлений"""

    queryset = Advert.objects.all()
    filter_backends = [filterss.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['created', 'amount']
    filterset_class = AdvertFilterSet
    search_fields = ['created', '^name']
    serializer_class = AdvertSerializers.GetAdvertSerializer


class FindCategoryByIdView(generics.RetrieveAPIView):
    """Поиск объявлений по идентификации"""

    queryset = Advert.objects.all()
    serializer_class = AdvertSerializers.GetAdvertSerializer
