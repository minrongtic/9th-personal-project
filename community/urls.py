from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "community"

urlpatterns = [
    path('', views.communityBoard, name="communityBoard"),
    path('<int:community_id>/', views.communityDetail, name="communityDetail"),
    path('new/', views.communityNew, name="communityNew"),
    path('create/', views.communityCreate, name="communityCreate"),
    path('edit/<int:community_id>', views.communityEdit, name="communityEdit"),
    path('update/<int:community_id>',
         views.communityUpdate, name="communityUpdate"),
    path('delete/<int:community_id>',
         views.communityDelete, name="communityDelete"),
]
