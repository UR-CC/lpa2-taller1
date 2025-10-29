import pytest


def test_asientos_mod_importable():
    """Comprueba que el módulo de categoría 'asientos' es importable."""
    pytest.importorskip("src.models.categorias.asientos")
    assert True
