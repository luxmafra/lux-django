from typing import List

from pypro.modulos.models import Module


def list_modules_ordered() -> List[Module]:
    """
   List ordered modules by title
   :return:
   """

    return list(Module.objects.order_by('order').all())


def encontrar_modulo(slug: str) -> Module:
    return Module.objects.get(slug=slug)


def list_aulas_of_modules_ordered(module: Module):
    return list(module.aula_set.order_by('order').all())
