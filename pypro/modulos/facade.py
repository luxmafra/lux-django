from typing import List

from django.db.models import Prefetch

from pypro.modulos.models import Module, Aula


def list_modules_ordered() -> List[Module]:
    """
   List ordered modules by title
   :return:
   """

    return list(Module.objects.order_by('title').all())


def encontrar_modulo(slug: str) -> Module:
    return Module.objects.get(slug=slug)


def list_aulas_of_modules_ordered(module: Module):
    return list(module.aula_set.order_by('order').all())


def encontrar_aula(slug):
    return Aula.objects.select_related('module').get(slug=slug)


def list_modules_with_aulas():
    aulas_ordered = Aula.objects.order_by('order')
    return Module.objects.order_by('order').prefetch_related(
        Prefetch('aula_set', queryset=aulas_ordered, to_attr='aulas')
    ).all()
