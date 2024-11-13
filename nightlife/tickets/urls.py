from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path
from tickets.views import test_translation_view
from .views import debug_language_view

router = DefaultRouter()
router.register(r'api/nightclubs', views.NightClubViewSet, basename='nightclub')

urlpatterns = [
    path('', views.home_view, name='home'),                      # Página principal
    path('nightclub/<int:nightclub_id>/tickets/', views.TicketListView, name='ticket-list'),  # Lista de tickets
    path('ticket/<int:pk>/', views.TicketDetailView, name='ticket-detail'),  # Detalle de ticket
    path('download-nightclub-json/<int:pk>/', views.download_nightclub_json, name='download-nightclub-json'),
    path('cart/', views.cart_view, name='cart'),
    path('order-confirmation/<int:order_id>/', views.order_confirmation, name='order-confirmation'),
    path('delete-ticket/<int:pk>/', views.delete_ticket, name='delete-ticket'),
    path('payment/', views.payment_view, name='payment'),
    path('payment-success/', views.payment_success_view, name='payment-success'),
    path('api/', include(router.urls)),  # Incluye solo las rutas de API
    path('cart/remove/<int:item_id>/', views.remove_cart_item, name='remove-cart-item'),
    path('download-receipt/<int:order_id>/', views.download_receipt,
         name='download-receipt'),

    #path('test-translation/', test_translation_view),
    #path('debug-language/', debug_language_view),

]

from django.conf.urls.i18n import set_language

urlpatterns += [
    path('i18n/set_language/', set_language, name='set_language'),
]

