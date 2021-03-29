from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from versatileimagefield.fields import VersatileImageField, PPOIField
from django.utils.translation import gettext_lazy as _
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

    class Meta:
        verbose_name = _('Пользоваетель')
        verbose_name_plural = _('Пользователи')


class Image(BaseModel):
    name = models.CharField(max_length=255)
    image = VersatileImageField(
        'Image',
        upload_to='images/',
        ppoi_field='image_ppoi'
    )
    image_ppoi = PPOIField()

    class Meta:
        verbose_name = _('Картинка')
        verbose_name_plural = _('Картинки')


class Category(BaseModel):
    name = models.CharField(max_length=30, blank=True, default='category_name')
    main_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True,
                                      related_name='add_main_category')

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')


class Announcement(BaseModel):
    announcement_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=300, blank=True, default='advert_name')
    description = models.TextField(max_length=5000, blank=True, default="advert_description")
    image = models.ManyToManyField(Image, related_name='advert_image')
    price = models.IntegerField(blank=False, default='1')
    phone = models.IntegerField(blank=False, default='+996700806860')
    whatsapp = models.CharField(max_length=300, blank=True, default='whatsapp')

    class Meta:
        verbose_name = _('Объявление')
        verbose_name_plural = _('Объявления')
