from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import NightClubViewSet

# Crear un enrutador solo para las vistas de API
router = DefaultRouter()
router.register(r'api/nightclubs', NightClubViewSet, basename='nightclub')  # Prefijo /api/nightclubs

urlpatterns = [
    path('', views.home_view, name='home'),  # Página principal
    path('nightclub/<int:nightclub_id>/tickets/', views.TicketListView,
         name='ticket-list'),  # Lista de tickets para un nightclub
    path('ticket/<int:pk>/', views.TicketDetailView, name='ticket-detail'),
    # Detalle de un ticket específico
    path('download-nightclub-json/<int:pk>/', views.download_nightclub_json,
         name='download-nightclub-json'),
    path('cart/', views.cart_view, name='cart'),
    path('order-confirmation/', views.order_confirmation, name='order-confirmation'),
    path('delete-ticket/<int:pk>/', views.delete_ticket, name='delete-ticket'),
    path('payment/', views.payment_view, name='payment'),
    path('payment-success/', views.payment_success_view, name='payment-success'),
    path('api/', include(router.urls)),  # Incluye solo las rutas de API
    path('cart/remove/<int:item_id>/', views.remove_cart_item,
         name='remove-cart-item'),

]
