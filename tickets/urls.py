from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import NightClubViewSet

# Crear un enrutador y registrar el ViewSet de discotecas
router = DefaultRouter()
router.register(r'nightclubs', NightClubViewSet, basename='nightclub')

urlpatterns = [
    path('', views.home_view, name='home'),
    path('tickets/<int:nightclub_id>/', views.TicketListView,
         name='ticket-list'),
    path('download-nightclub-json/<int:pk>/', views.download_nightclub_json,
         name='download-nightclub-json'),
    path('tickets/<int:pk>/', views.TicketDetailView, name='ticket-detail'),
    path('cart/', views.cart_view, name='cart'),
    path('order-confirmation/', views.order_confirmation, name='order-confirmation'),
    path('delete-ticket/<int:pk>/', views.delete_ticket, name='delete-ticket'),
    path('payment/', views.payment_view, name='payment'),
    path('payment-success/', views.payment_success_view, name='payment-success'),

]

