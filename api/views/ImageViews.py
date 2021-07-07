import os

from rest_framework import generics, status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from RestForFlutter import settings
from api.models import Image
from api.serializers import ImageSerializers


class CreateImageView(generics.CreateAPIView):
    """Добавление изображений"""

    serializer_class = ImageSerializers.AllImageSerializer
    parser_classes = (FormParser, MultiPartParser)


class DeleteImageByIdView(generics.DestroyAPIView):
    """Удаление изображений по идентификации"""

    queryset = Image.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        image_root = settings.MEDIA_ROOT + "\\" + str(instance.image)
        self.perform_destroy(instance, image_root)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance, image_root=None):
        instance.delete()
        os.remove(image_root)


class UpdateImageByIdView(generics.UpdateAPIView):
    """Обновление изображений по идентификации"""

    queryset = Image.objects.all()
    serializer_class = ImageSerializers.AllImageSerializer
    parser_classes = (FormParser, MultiPartParser)


class GetImageView(generics.ListAPIView):
    """Вывод изображений"""

    queryset = Image.objects.all()
    serializer_class = ImageSerializers.GetImageSerializer


class FindImageByIdView(generics.RetrieveAPIView):
    """Поиск изображений по идентификации"""

    queryset = Image.objects.all()
    serializer_class = ImageSerializers.GetImageSerializer
