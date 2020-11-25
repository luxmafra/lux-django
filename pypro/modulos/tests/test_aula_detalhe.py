import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.django_assertions import assert_contains
from pypro.modulos.models import Module, Aula


@pytest.fixture
def module(db):
    return mommy.make(Module)


@pytest.fixture
def aula(module):
    return mommy.make(Aula, module=module)


@pytest.fixture
def resp(client, aula):
    resp = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp


def test_title(resp, aula: Aula):
    assert_contains(resp, aula.title)


def test_vimeo(resp, aula: Aula):
    assert_contains(resp, f'src="https://player.vimeo.com/video/{ aula.vimeo_id }"')
