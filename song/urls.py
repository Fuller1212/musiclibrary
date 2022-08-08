from django.urls import path
from . import views


urlpatterns = [
    path('', views.song_list),
    path('<int:pk>/', views.song_detail),
    path('<int:pk>/like', views.like_count)
]