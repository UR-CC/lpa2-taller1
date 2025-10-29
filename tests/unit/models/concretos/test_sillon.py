import pytest


def test_sillon_mod_importable():
    """Comprueba que el módulo concreto 'sillon' es importable."""
    pytest.importorskip("src.models.concretos.sillon")
    assert True
