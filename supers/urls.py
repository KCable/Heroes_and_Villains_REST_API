from django.urls import path
from . import views

urlpatterns = [
    path('', views.super),
    path('<pk>/', views.super_type),
    path('<str:make>', views.supers_by_id),
    ]