from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()
    DoesNotExist = None

    class Meta:
        abstract = True