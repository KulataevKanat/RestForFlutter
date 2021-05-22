import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from django.conf import settings
from django.contrib.auth import get_user_model

from RestForFlutter.advice import ACCESS_TOKEN_EXPIRED, TOKEN_PREFIX, USER_NOT_FOUND, USER_NOT_ACTIVE, USER_DETAIL


class SafeJWTAuthentication(BaseAuthentication):

    def authenticate(self, request):
        User = get_user_model()
        authorization_header = request.headers.get('Authorization')

        if not authorization_header:
            return None

        try:
            access_token = authorization_header.split(' ')[1]

            if access_token.__eq__('null'):
                return None

            payload = jwt.decode(
                access_token, settings.SECRET_KEY, algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed(ACCESS_TOKEN_EXPIRED)

        except IndexError:
            raise exceptions.AuthenticationFailed(TOKEN_PREFIX)

        user = User.objects.filter(id=payload['user_id']).first()

        if user is None:
            raise exceptions.AuthenticationFailed({
                USER_DETAIL: USER_NOT_FOUND
            })

        if not user.is_active:
            raise exceptions.AuthenticationFailed(USER_NOT_ACTIVE)

        return user, None
