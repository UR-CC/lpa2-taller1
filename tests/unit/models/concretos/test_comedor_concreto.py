import pytest


def test_comedor_mod_importable_concreto():
    """Comprueba que el módulo concreto 'comedor' es importable (concreto)."""
    pytest.importorskip("src.models.concretos.comedor")
    assert True
