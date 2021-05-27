from rest_framework import generics, filters

from api.models import Announcement
from api.serializers import AnnouncementSerializers
from django_filters import rest_framework as filterss

from api.repository import AnnouncementFilterSet


class CreateAnnouncementView(generics.CreateAPIView):
    """Добавление объявления"""

    serializer_class = AnnouncementSerializers.CreateAnnouncementSerializer


class DeleteAnnouncementByIdView(generics.DestroyAPIView):
    """Удаление объявления по идентификации"""

    queryset = Announcement.objects.all()


class UpdateAnnouncementByIdView(generics.UpdateAPIView):
    """Обновление объявления по идентификации"""

    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializers.UpdateAnnouncementSerializer


class GetAnnouncementView(generics.ListAPIView):
    """Вывод объявлений"""

    queryset = Announcement.objects.all()
    filter_backends = [filterss.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['created', ]
    filterset_class = AnnouncementFilterSet
    search_fields = ['created', '^name']
    serializer_class = AnnouncementSerializers.GetAnnouncementSerializer


class FindAnnouncementByIdView(generics.RetrieveAPIView):
    """Поиск объявлений по идентификации"""

    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializers.GetAnnouncementSerializer
