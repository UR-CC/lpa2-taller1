import pytest


def test_mesa_mod_importable_concreto():
    """Comprueba que el módulo concreto 'mesa' es importable (concreto)."""
    pytest.importorskip("src.models.concretos.mesa")
    assert True
