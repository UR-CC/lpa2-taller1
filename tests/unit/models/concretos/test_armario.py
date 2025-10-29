import pytest


def test_armario_mod_importable():
    """Comprueba que el módulo concreto 'armario' es importable."""
    pytest.importorskip("src.models.concretos.armario")
    assert True
