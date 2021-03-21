from django.contrib import admin
from django.urls import path, include
from RestForFlutter.swagger import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

urlpatterns += doc_urls
