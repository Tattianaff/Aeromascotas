from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from aeromascotas.views import ver_imagen_cliente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aeromascotas.urls')),  
    path('ver-imagen/', ver_imagen_cliente),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
