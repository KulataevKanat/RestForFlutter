from django.contrib import admin

from api.models import User, Category, Announcement, Image, Publicity

admin.site.register(User)
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Announcement)
admin.site.register(Publicity)
