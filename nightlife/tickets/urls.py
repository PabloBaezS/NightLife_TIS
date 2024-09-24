from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Home page
    path('tickets/', views.TicketListView, name='ticket-list'),
    path('tickets/<int:pk>/', views.TicketDetailView, name='ticket-detail'),
    path('cart/', views.cart_view, name='cart'),
    path('order-confirmation/', views.order_confirmation, name='order-confirmation'),
]
