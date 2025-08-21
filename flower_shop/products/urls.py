from django.urls import path
from . import views

urlpatterns = [
    path('', views.flower_list, name='home'),
    path('catalog/', views.flower_list, name='catalog'),
]