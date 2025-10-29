import pytest

from src.models.mueble import Mueble


class TestMueble:
    def test_es_clase_abstracta(self):
        # Verificar que Mueble es abstracta
        with pytest.raises(TypeError):
            Mueble("Mesa", "Madera", "Blanco", 100.0)
