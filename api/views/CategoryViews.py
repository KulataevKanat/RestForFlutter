from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response

from api.models import Category
from api.serializers import CategorySerializers


class CreateCategoryView(generics.CreateAPIView):
    """Добавление категории"""

    serializer_class = CategorySerializers.CreateCategorySerializer


class CreateSubCategoryView(generics.CreateAPIView):
    """Добавление подкатегории"""

    serializer_class = CategorySerializers.CreateSubCategorySerializer


class DeleteCategoryByIdView(generics.DestroyAPIView):
    """Удаление категории по идентификации"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializers.DeleteCategorySerializer

    def get_object(self):
        try:
            return Category.objects.all()
        except Category.DoesNotExist:
            raise Http404

    def delete(self, request, format=None, **kwargs):
        """Метод удаления всех категорий"""
        category = self.get_object()
        self.perform_destroy(category)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateCategoryByIdView(generics.UpdateAPIView):
    """Обновление категории по идентификации"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializers.UpdateCategorySerializer


class GetCategoryView(generics.ListAPIView):
    """Вывод категорий"""

    queryset = Category.objects.filter(main_category=None)
    serializer_class = CategorySerializers.GetCategorySerializer


class FindCategoryByIdView(generics.RetrieveAPIView):
    """Поиск категории по идентификации"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializers.GetCategorySerializer
