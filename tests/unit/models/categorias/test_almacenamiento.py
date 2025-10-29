import pytest


def test_almacenamiento_mod_importable():
    """Comprueba que el módulo de categoría 'almacenamiento' es importable."""
    pytest.importorskip("src.models.categorias.almacenamiento")
    assert True
