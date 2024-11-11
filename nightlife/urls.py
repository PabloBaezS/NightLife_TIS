from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

# Configuración de rutas principales con prefijo de idioma
urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),              # Administración de Django
    path('', include('tickets.urls')),             # URLs de la aplicación de tickets
    path('users/', include('users.urls')),         # URLs relacionadas con los usuarios
)

# Incluye las URLs para cambiar de idioma, fuera del prefijo de idioma
urlpatterns += [
    path('i18n/', include('django.conf.urls.i18n')),  # URL para el cambio de idioma
]

# Incluye rutas de API específicas (opcional)
# Si tienes vistas de API específicas en `tickets.urls`, añade aquí solo las necesarias o agrégalas a su propio archivo de URLs
urlpatterns += [
    path('api/', include('tickets.urls')),  # Rutas de API para la aplicación de tickets, si son necesarias
]

# Configuración para archivos estáticos y media en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
