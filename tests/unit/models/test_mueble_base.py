import pytest

from src.models.mueble import Mueble


class TestMuebleBase:
    def test_mueble_abstracto(self):
        with pytest.raises(TypeError):
            Mueble("X", "Y", "Z")

    def test_abstract_methods_exist(self):
        assert hasattr(Mueble, "calcular_precio")
        assert hasattr(Mueble, "obtener_descripcion")
