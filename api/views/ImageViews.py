from rest_framework import generics

from api.models import Image
from api.serializers import ImageSerializers


class CreateImageView(generics.CreateAPIView):
    """Добавление изображений"""

    serializer_class = ImageSerializers.AllImageSerializer


class DeleteImageByIdView(generics.DestroyAPIView):
    """Удаление изображений по идентификации"""

    queryset = Image.objects.all()


class UpdateImageByIdView(generics.UpdateAPIView):
    """Обновление изображений по идентификации"""

    queryset = Image.objects.all()
    serializer_class = ImageSerializers.AllImageSerializer


class GetImageView(generics.ListAPIView):
    """Вывод изображений"""

    queryset = Image.objects.all()
    serializer_class = ImageSerializers.GetImageSerializer


class FindImageByIdView(generics.RetrieveAPIView):
    """Поиск изображений по идентификации"""

    queryset = Image.objects.all()
    serializer_class = ImageSerializers.GetImageSerializer
