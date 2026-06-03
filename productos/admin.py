from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Register your models here.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('productos.urls')), # Aquí vivirán tus rutas del API
]

# Esto permite ver las imágenes en el navegador durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)