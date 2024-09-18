from django.urls import path
from . import views

urlpatterns = [
    path('', views.club_list, name='club_list'),
    path('<int:nightclubID>/', views.club_detail, name='club_detail'),
    path('create/', views.create_club, name='create_club'),
    path('<int:nightclubID>/update_hours/', views.update_club_hours, name='update_club_hours'),
    path('<int:nightclubID>/delete/', views.delete_club, name='delete_club'),
]
