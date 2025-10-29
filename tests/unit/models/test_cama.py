import pytest

from src.models.concretos.cama import Cama


class TestCama:
    @pytest.fixture
    def cama(self):
        return Cama("Cama Test", "Madera", "Blanco", 300.0, "queen", True, True)

    def test_instanciacion_y_atributos(self, cama):
        assert cama.tamaño == "queen"
        assert cama.incluye_colchon is True

    def test_calcular_precio(self, cama):
        precio = cama.calcular_precio()
        assert precio > 300.0

    def test_setter_tamaño_valido(self, cama):
        cama.tamaño = "king"
        assert cama.tamaño == "king"

    def test_setter_tamaño_invalido(self, cama):
        with pytest.raises(ValueError):
            cama.tamaño = "gigante"
