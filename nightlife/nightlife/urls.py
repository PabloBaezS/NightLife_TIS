from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import set_language
from django.conf.urls.i18n import i18n_patterns

# Configuración de rutas principales con prefijo de idioma
urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),               # Admin de Django
    path('', include('tickets.urls')),             # URLs de la aplicación de tickets
    path('users/', include('users.urls')),         # URLs relacionadas con usuarios
    prefix_default_language=False                  # Evita el prefijo de idioma si es el predeterminado (inglés)
)

# Incluye la ruta para el cambio de idioma fuera de i18n_patterns
urlpatterns += [
    path('i18n/set_language/', set_language, name='set_language'),  # Asegúrate de esta línea
]

# Configuración para archivos estáticos y media en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

