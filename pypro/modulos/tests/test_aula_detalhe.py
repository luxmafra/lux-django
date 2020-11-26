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
def resp(client_com_usuario_logado, aula):
    resp = client_com_usuario_logado.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp


def test_title(resp, aula: Aula):
    assert_contains(resp, aula.title)


def test_vimeo(resp, aula: Aula):
    assert_contains(resp, f'src="https://player.vimeo.com/video/{ aula.vimeo_id }"')


def test_module_breadcrumb(resp, module: Module):
    assert_contains(resp, f'<li class="breadcrumb-item"><a href="{module.get_absolute_url()}">{module.title}</a></li>')


@pytest.fixture
def resp_sem_usuario(client, aula):
    resp = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp


def test_usuario_nao_logado_redirect(resp_sem_usuario):
    assert resp_sem_usuario.status_code == 302
    assert resp_sem_usuario.url.startswith(reverse('login'))
