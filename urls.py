from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.food_list, name='list'),
    path('<slug:slug>/', views.food_detail, name='detail'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('video_feed/', views.video_feed, name='video_feed'),
]
