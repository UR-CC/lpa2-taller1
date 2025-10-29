import pytest

from src.models.concretos.mesa import Mesa


class TestMesa:
    @pytest.fixture
    def mesa(self):
        return Mesa(
            "Mesa Test", "Roble", "Natural", 200.0, "rectangular", 120.0, 80.0, 75.0, 6
        )

    def test_calcular_precio_factor_y_capacidad(self, mesa):
        precio = mesa.calcular_precio()
        assert precio >= 200.0
        # si capacidad >4 y <=6 debería agregar 50
        assert precio >= 250.0

    def test_forma_invalida(self, mesa):
        with pytest.raises(ValueError):
            mesa.forma = "triangular"
