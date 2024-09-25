from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Home page
    path('tickets/', views.TicketListView, name='ticket-list'),
    path('tickets/<int:pk>/', views.TicketDetailView, name='ticket-detail'),
    path('cart/', views.cart_view, name='cart'),
    path('order-confirmation/', views.order_confirmation, name='order-confirmation'),
    path('delete-ticket/<int:pk>/', views.delete_ticket, name='delete-ticket'),
    path('payment/', views.payment_view, name='payment'),
    path('payment-success/', views.payment_success_view,
         name='payment-success'),
]

