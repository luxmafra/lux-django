from django.urls import path

from pypro.modulos import views

app_name = 'modulos'
urlpatterns = [
    path('<slug:slug>', views.detail, name='detail'),
]
