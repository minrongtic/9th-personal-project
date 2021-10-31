from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.communityBoard, name="communityBoard"),
    path('<int:community_id>/', views.communityDetail, name="communityDetail"),
]
