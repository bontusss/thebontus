
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/', include('djoser.urls')),
    # path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('news.urls')),
    path('weather/', include('weather.urls', namespace='weather')),
    path('crime/', include('crime_app.urls', namespace='crime'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
