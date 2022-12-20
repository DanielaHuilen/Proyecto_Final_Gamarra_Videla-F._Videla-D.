from django.urls import path
from ProyectoFinalApp import views

urlpatterns = [
path ("", views.inicio, name='inicio'),
path ("profesores", views.Profesores_index, name='profesores_index'),

]