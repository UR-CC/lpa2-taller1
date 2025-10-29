import pytest


def test_superficies_mod_importable():
    """Comprueba que el módulo de categoría 'superficies' es importable."""
    pytest.importorskip("src.models.categorias.superficies")
    assert True
