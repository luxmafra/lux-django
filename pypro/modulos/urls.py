from django.urls import path

from pypro.modulos import views

app_name = 'modulos'
urlpatterns = [
    path('<slug:slug>', views.detail, name='detail'),
    path('aulas/<slug:slug>', views.aula, name='aula'),
    path('', views.index, name='index'),
]
