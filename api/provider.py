import datetime
import jwt
from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, username, groups_id, email, password=None):
        if not email:
            raise ValueError('Email must be set!')
        user = self.model(username=username, groups_id=groups_id, email=email)
        user.set_password(password)
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, groups_id, email, password):
        user = self.create_user(username, groups_id, email, password)
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username_):
        return self.get(username=username_)


def generate_access_token(user):
    access_token_payload = {
        'user_id': user.id,
        'username': user.username,
        'role': user.groups.name,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=8, minutes=1),
        'iat': datetime.datetime.utcnow(),
    }

    access_token = jwt.encode(
        access_token_payload,
        settings.SECRET_KEY,
        algorithm='HS256').decode('utf-8')

    return access_token


def generate_refresh_token(user):
    refresh_token_payload = {
        'user_id': user.id,
        'username': user.username,
        'role': user.groups.name,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow()
    }

    refresh_token = jwt.encode(
        refresh_token_payload,
        settings.REFRESH_TOKEN_SECRET,
        algorithm='HS256').decode('utf-8')

    return refresh_token
