import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.django_assertions import assert_contains
from pypro.modulos.models import Module, Aula


@pytest.fixture
def module(db):
    return mommy.make(Module)


@pytest.fixture
def aulas(module):
    return mommy.make(Aula, 3, module=module)


@pytest.fixture
def resp(client, module, aulas):
    resp = client.get(reverse('modulos:detail', kwargs={'slug': module.slug}))
    return resp


def test_title(resp, module: Module):
    assert_contains(resp, module.title)


def test_description(resp, module: Module):
    assert_contains(resp, module.description)


def test_public(resp, module: Module):
    assert_contains(resp, module.public)


def test_aulas_title(resp, aulas):
    for aula in aulas:
        assert_contains(resp, aula.title)
