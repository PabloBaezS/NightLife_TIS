from django.contrib import admin
from django.urls import path, include
from nightclubs import views as nightclub_views  # Import the landing page view from the nightclubs app

urlpatterns = [
    path('admin/', admin.site.urls),               # Admin site
    path('accounts/', include('accounts.urls')),   # Accounts app URLs
    path('nightclubs/', include('nightclubs.urls')),  # Nightclubs app URLs
    path('', nightclub_views.landing_page, name='landing_page'),  # Root URL points to the landing page
]
