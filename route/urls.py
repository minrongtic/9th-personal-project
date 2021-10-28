from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main),
    path('route/', views.routeBoard, name="routeBoard"),
    path('route/<int:route_id>', views.routeDetail, name="routeDetail"),
]
