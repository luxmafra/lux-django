import pytest
from model_mommy import mommy

from pypro.modulos import facade
from pypro.modulos.models import Module


@pytest.fixture
def modules(db):
    return [mommy.make(Module, title=s) for s in 'Antes Depois'.split()]


def test_list_moludes_ordered(modules):
    assert list(sorted(modules, key=lambda module: module.title)) == facade.list_modules_ordered()
