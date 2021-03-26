from django.contrib import admin
from django.urls import path, include

from RestForFlutter import settings
from RestForFlutter.swagger import urlpatterns as doc_urls
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
