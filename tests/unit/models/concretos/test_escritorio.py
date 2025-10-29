import pytest


def test_escritorio_mod_importable():
    """Comprueba que el módulo concreto 'escritorio' es importable."""
    pytest.importorskip("src.models.concretos.escritorio")
    assert True
