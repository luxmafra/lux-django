from django.shortcuts import render

from pypro.modulos import facade


def home(request):
    return render(request, 'base/home.html', {'MODULES': facade.list_modules_ordered()})
