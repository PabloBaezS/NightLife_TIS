from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import set_language
from django.conf.urls.i18n import i18n_patterns
from django.urls import path
from tickets import views  # Importa tus vistas

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # Rutas para cambiar idioma
]

# Rutas con prefijos de idioma
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),  # Admin de Django
    path('', include('tickets.urls')),  # URLs de la aplicación de tickets
    path('users/', include('users.urls')),  # URLs relacionadas con usuarios
    prefix_default_language=True
    # Evita el prefijo de idioma si es el predeterminado (inglés)
)

# Configuración para archivos estáticos y media en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

