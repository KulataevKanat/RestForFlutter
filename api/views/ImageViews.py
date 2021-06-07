from rest_framework import generics

from api.models import Image
from api.serializers import ImageSerializers
from rest_framework.parsers import FormParser, MultiPartParser


class CreateImageView(generics.CreateAPIView):
    """Добавление изображений"""

    serializer_class = ImageSerializers.AllImageSerializer
    # parser_classes = (FormParser, MultiPartParser)


class DeleteImageByIdView(generics.DestroyAPIView):
    """Удаление изображений по идентификации"""

    queryset = Image.objects.all()


class UpdateImageByIdView(generics.UpdateAPIView):
    """Обновление изображений по идентификации"""

    queryset = Image.objects.all()
    serializer_class = ImageSerializers.AllImageSerializer
    # parser_classes = (FormParser, MultiPartParser)


class GetImageView(generics.ListAPIView):
    """Вывод изображений"""

    queryset = Image.objects.all()
    serializer_class = ImageSerializers.GetImageSerializer


class FindImageByIdView(generics.RetrieveAPIView):
    """Поиск изображений по идентификации"""

    queryset = Image.objects.all()
    serializer_class = ImageSerializers.GetImageSerializer
