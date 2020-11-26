from django.shortcuts import render

from pypro.modulos import facade


def index(request):
    ctx = {'modules': facade.list_modules_with_aulas()}
    return render(request, 'module/index.html', ctx)


def detail(request, slug):
    module = facade.encontrar_modulo(slug)
    aulas = facade.list_aulas_of_modules_ordered(module)
    return render(request, 'module/module_detail.html', {'module': module, 'aulas': aulas})


def aula(request, slug):
    aula = facade.encontrar_aula(slug)
    return render(request, 'module/aula_detalhe.html', {'aula': aula})
