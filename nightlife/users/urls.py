from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('custom-admin/dashboard/', views.admin_dashboard, name='admin-dashboard'),
    path('custom-admin/create-nightclub/', views.create_nightclub, name='create-nightclub'),
    path('custom-admin/edit-nightclub/<int:pk>/', views.edit_nightclub, name='edit-nightclub'),
    path('custom-admin/delete-nightclub/<int:pk>/', views.delete_nightclub, name='delete-nightclub'),
    path('nightclub/<int:pk>/', views.nightclub_detail, name='nightclub-detail'),
]
