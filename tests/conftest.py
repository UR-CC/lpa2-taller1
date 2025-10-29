import pytest

from src.models.composicion.comedor import Comedor
from src.models.concretos.mesa import Mesa
from src.models.concretos.silla import Silla
from src.services.tienda import TiendaMuebles


@pytest.fixture
def tienda():
    return TiendaMuebles("Tienda Fixture")


@pytest.fixture
def silla_basica():
    return Silla("Silla Fixture", "Madera", "Negro", 50.0)


@pytest.fixture
def mesa_basica():
    return Mesa("Mesa Fixture", "Madera", "Marron", 200.0)


@pytest.fixture
def comedor_basico(mesa_basica):
    sillas = [Silla(f"Silla {i}", "Madera", "Marron", 45.0) for i in range(4)]
    return Comedor("Comedor Fixture", mesa_basica, sillas)
