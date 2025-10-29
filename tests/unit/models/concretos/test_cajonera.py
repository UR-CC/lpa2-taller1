import pytest


def test_cajonera_mod_importable():
    """Comprueba que el módulo concreto 'cajonera' es importable."""
    pytest.importorskip("src.models.concretos.cajonera")
    assert True
