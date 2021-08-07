from django_filters import rest_framework as filterss
from rest_framework import generics, filters

from api.models import Announcement
from api.repository import AnnouncementFilterSet
from api.serializers import AnnouncementSerializers


class CreateAnnouncementView(generics.CreateAPIView):
    """Добавление объявления"""

    serializer_class = AnnouncementSerializers.CreateAnnouncementSerializer


class DeleteAnnouncementByIdView(generics.DestroyAPIView):
    """Удаление объявления по идентификации"""

    queryset = Announcement.objects.all()

    def perform_destroy(self, instance):
        for image_instance in instance.image.all():
            image_instance.image.delete()
            image_instance.delete()
            instance.delete()


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
