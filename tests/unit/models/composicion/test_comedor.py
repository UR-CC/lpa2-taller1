import pytest

from src.models.composicion.comedor import Comedor
from src.models.concretos.mesa import Mesa
from src.models.concretos.silla import Silla


class TestComedor:
    @pytest.fixture
    def comedor_basico(self):
        mesa = Mesa(
            "Mesa Comedor",
            "Roble",
            "Marrón",
            200.0,
            "Rectangular",
            120.0,
            80.0,
            75.0,
            6,
        )
        sillas = [
            Silla("Silla Comedor", "Roble", "Marrón", 50.0, 4, "Roble")
            for _ in range(6)
        ]
        return Comedor("Comedor Familiar", mesa, sillas)

    def test_composicion_correcta(self, comedor_basico):
        assert comedor_basico.mesa is not None
        assert len(comedor_basico.sillas) == 6
        assert isinstance(comedor_basico.mesa, Mesa)
        assert all(isinstance(silla, Silla) for silla in comedor_basico.sillas)

    def test_calcular_precio_total(self, comedor_basico):
        precio_total = comedor_basico.calcular_precio_total()
        # Calcular el precio esperado sumando el precio calculado de la mesa y de cada silla
        precio_esperado = comedor_basico.mesa.calcular_precio() + sum(
            s.calcular_precio() for s in comedor_basico.sillas
        )
        assert precio_total == precio_esperado


# Nota: Las pruebas de servicio se encuentran en tests/unit/services
