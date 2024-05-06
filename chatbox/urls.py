from django.urls import path
from . import views


urlpatterns = [
    path('lobby/', views.lobby_screen_view),
    path('room/', views.room_screen_view),
]