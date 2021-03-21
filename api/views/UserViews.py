import jwt
from django.contrib.auth import get_user_model
from django.http import Http404
from rest_framework import exceptions, generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import User as Users
from RestForFlutter import settings
from api.provider import generate_access_token, generate_refresh_token
from api.serializers import UserSerializers


class UserAuthorizationView(viewsets.GenericViewSet):
    """Авторизация, вывод access и refresh токена"""

    serializer_class = UserSerializers.AuthSerializer

    @action(detail=False, methods=['POST'])
    def access_token(self, request):
        User = get_user_model()
        username = request.data.get('username')
        password = request.data.get('password')
        response = Response()

        user = User.objects.filter(username=username).first()

        if user is None:
            raise exceptions.AuthenticationFailed('user not found')

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('wrong password')

        serialized_user = UserSerializers.GetUserSerializer(user).data

        access_token = generate_access_token(user)
        refresh_token = generate_refresh_token(user)

        response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)
        response.data = {
            'access_token': access_token,
            'user': serialized_user,
        }

        return response

    @action(detail=False, methods=['POST'])
    def refresh_token(self, request):
        User = get_user_model()
        refresh_token = request.COOKIES.get('refresh_token')

        if refresh_token is None:
            raise exceptions.AuthenticationFailed('Authentication credentials were not provided.')
        try:
            payload = jwt.decode(refresh_token, settings.REFRESH_TOKEN_SECRET, algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('expired refresh token, please login again.')

        user = User.objects.filter(id=payload.get('user_id')).first()

        if user is None:
            raise exceptions.AuthenticationFailed('User not found')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('user is inactive')

        access_token = generate_access_token(user)

        return Response({'access_token': access_token})


class UserRegistrationView(generics.CreateAPIView):
    """Регистрация"""

    serializer_class = UserSerializers.RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializers.RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteAllUserView(generics.DestroyAPIView):
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


class GetUserView(generics.ListAPIView):
    """Вывод пользователей"""

    queryset = Users.objects.all()
    serializer_class = UserSerializers.GetUserSerializer


class FindUserByIdView(generics.RetrieveAPIView):
    """Вывод пользователя по идентификации"""

    queryset = Users.objects.all()
    serializer_class = UserSerializers.GetUserSerializer
