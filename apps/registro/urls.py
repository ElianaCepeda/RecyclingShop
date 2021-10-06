from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registroform/', views.registroform, name='Registro Cliente reciclador')
]