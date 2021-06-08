import jwt
from django.contrib.auth import get_user_model
from django.http import Http404
from rest_framework import exceptions, generics, status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password as encode
from django.contrib.auth.hashers import check_password as check
from RestForFlutter.advice import USER_DETAIL, USER_NOT_FOUND, WRONG_PASSWORD, ACCESS_TOKEN_DETAIL, USER_BLOCKED, \
    REFRESH_TOKEN_EXPIRED, AUTH_CREDENTIALS, DATA_DETAIL, WRONG_OLD_PASSWORD, WRONG_ACTIVE_OLD_PASSWORD
from api import service
from api.models import User as Users
from RestForFlutter import settings
from api.provider import generate_access_token, generate_refresh_token
from api.serializers import UserSerializers
from api.serializers.SpareSerializers import NotSerializer


class AccessToken(generics.CreateAPIView):
    """Авторизация - access token"""

    serializer_class = UserSerializers.AuthSerializer

    def post(self, request, *args, **kwargs):
        """Метод вывода access токена"""

        User = get_user_model()
        username = request.data.get('username')
        password = request.data.get('password')
        response = Response()

        user = User.objects.filter(username=username).first()

        if user is None:
            raise exceptions.AuthenticationFailed({USER_DETAIL: USER_NOT_FOUND})

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed(WRONG_PASSWORD)

        serialized_user = UserSerializers.GetUserSerializer(user).data

        access_token = generate_access_token(user)
        refresh_token = generate_refresh_token(user)

        response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)
        response.data = {
            'access_token': access_token,
            'user': serialized_user,
        }

        return response


class RefreshToken(generics.ListAPIView):
    """Авторизация - вывод refresh токена"""

    queryset = Users.objects.all()
    serializer_class = NotSerializer

    def get(self, request, *args, **kwargs):
        """Метод вывода refresh токена"""

        User = get_user_model()
        refresh_token = request.COOKIES.get('refresh_token')

        if refresh_token is None:
            raise exceptions.AuthenticationFailed(AUTH_CREDENTIALS)
        try:
            payload = jwt.decode(refresh_token, settings.REFRESH_TOKEN_SECRET, algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed(REFRESH_TOKEN_EXPIRED)

        user = User.objects.filter(id=payload.get('user_id')).first()

        if user is None:
            raise exceptions.AuthenticationFailed({USER_DETAIL: USER_NOT_FOUND})

        if not user.is_active:
            raise exceptions.AuthenticationFailed(USER_BLOCKED)

        access_token = generate_access_token(user)

        return Response({ACCESS_TOKEN_DETAIL: access_token})


class UserRegistrationView(generics.CreateAPIView):
    """Регистрация"""

    serializer_class = UserSerializers.RegistrationSerializer

    def perform_create(self, serializer):
        serializer.save(password=encode(serializer.validated_data.__getitem__('password')))


class CreateSuperUserView(generics.CreateAPIView):
    """Добавление супер пользователя"""

    serializer_class = UserSerializers.CreateSuperUserSerializer


class DeleteUserByIdView(generics.DestroyAPIView):
    """Удаление пользователя по идентификации"""

    queryset = Users.objects.all()


class DeleteAllUsersView(generics.DestroyAPIView):
    """Удаление всех пользователей"""

    def get_object(self):
        try:
            return Users.objects.all()
        except Users.DoesNotExist:
            raise Http404

    def delete(self, request, format=None, **kwargs):
        """Метод удаления всех пользователей"""
        users = self.get_object()
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateUserView(service.PartialUpdateServiceView):
    """Изменение пользователя по идентификации"""

    queryset = Users.objects.all()
    serializer_class = UserSerializers.UpdateRequestUserSerializer

    def patch(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = UserSerializers.UpdateResponseUserSerializer(instance, data=request.data, partial=partial)
        if serializer.is_valid(raise_exception=True):
            try:
                if "password" in request.data:
                    if check(request.data["old_password"], self.request.user.password):
                        serializer.save(password=encode(request.data['password']))
                    else:
                        return Response({DATA_DETAIL: WRONG_OLD_PASSWORD})
                else:
                    self.perform_update(serializer)
            except KeyError:
                return Response({DATA_DETAIL: WRONG_ACTIVE_OLD_PASSWORD})
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer, *args, **kwargs):
        serializer.save()


class GetUserView(generics.ListAPIView):
    """Вывод пользователей"""

    queryset = Users.objects.all()
    serializer_class = UserSerializers.GetUserSerializer


class FindUserByIdView(generics.RetrieveAPIView):
    """Вывод пользователя по идентификации"""

    queryset = Users.objects.all()
    serializer_class = UserSerializers.GetUserSerializer
