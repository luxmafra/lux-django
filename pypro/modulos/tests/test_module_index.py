from typing import List

import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.django_assertions import assert_contains
from pypro.modulos.models import Module, Aula


@pytest.fixture
def modules(db):
    return mommy.make(Module, 2)


@pytest.fixture
def aulas(modules):
    aulas = []
    for module in modules:
        aulas.extend(mommy.make(Aula, 3, module=module))
    return aulas


@pytest.fixture
def resp(client, modules, aulas):
    resp = client.get(reverse('modulos:index'))
    return resp


def test_index_available(resp):
    assert resp.status_code == 200


def test_title(resp, modules: List[Module]):
    for module in modules:
        assert_contains(resp, module.title)


def test_description(resp, modules: List[Module]):
    for module in modules:
        assert_contains(resp, module.description)


def test_public(resp, modules: List[Module]):
    for module in modules:
        assert_contains(resp, module.public)


def test_aulas_title(resp, aulas: List[Aula]):
    for aula in aulas:
        assert_contains(resp, aula.title)


def test_aulas_link(resp, aulas: List[Aula]):
    for aula in aulas:
        assert_contains(resp, aula.get_absolute_url())
