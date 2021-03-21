from django.contrib.auth.models import AbstractUser, Group
from django.db import models

from RestForFlutter.models import BaseModel
from api.provider import UserAccountManager


class User(BaseModel, AbstractUser):
    groups = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, default=1)
    email = models.EmailField(max_length=50, unique=True)

    objects = UserAccountManager()

    REQUIRED_FIELDS = ['groups_id', 'email']

    def __str__(self):
        return self.username.__str__()

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

