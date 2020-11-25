from django.shortcuts import render

from pypro.modulos import facade


def detail(request, slug):
    module = facade.encontrar_modulo(slug)
    return render(request, 'module/module_detail.html', {'module': module})
