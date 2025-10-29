import pytest


def test_cama_mod_importable_concreto():
    """Comprueba que el módulo concreto 'cama' es importable (concreto)."""
    pytest.importorskip("src.models.concretos.cama")
    assert True
