import pytest

from src.models.composicion.comedor import Comedor
from src.models.concretos.armario import Armario
from src.models.concretos.cajonera import Cajonera
from src.models.concretos.cama import Cama
from src.models.concretos.escritorio import Escritorio
from src.models.concretos.mesa import Mesa
from src.models.concretos.silla import Silla


@pytest.fixture
def armario_basico():
    return Armario(
        "Armario 1",
        "Madera",
        "Blanco",
        500.0,
        num_puertas=2,
        num_cajones=3,
        tiene_espejos=False,
    )


@pytest.fixture
def cajonera_basica():
    return Cajonera(
        "Cajonera 1", "Madera", "Marron", 250.0, num_cajones=4, tiene_ruedas=True
    )


@pytest.fixture
def cama_basica():
    return Cama(
        "Cama 1",
        "Madera",
        "Nogal",
        800.0,
        tamaño="king",
        incluye_colchon=True,
        tiene_cabecera=True,
    )


@pytest.fixture
def escritorio_basico():
    return Escritorio(
        "Escritorio 1",
        "Madera",
        "Caoba",
        400.0,
        forma="L",
        tiene_cajones=True,
        num_cajones=3,
    )


@pytest.fixture
def comedor_basico():
    mesa = Mesa(
        "Mesa Comedor", "Roble", "Roble", 200.0, "rectangular", 120.0, 80.0, 75.0, 6
    )
    sillas = [Silla("Silla Comedor", "Roble", "Roble", 50.0) for _ in range(6)]
    return Comedor("Comedor Test", mesa, sillas)


def test_armario_properties_and_precio(armario_basico):
    assert armario_basico.num_puertas == 2
    assert armario_basico.num_cajones == 3
    precio = armario_basico.calcular_precio()
    assert precio >= armario_basico.precio_base


def test_cajonera_behaviour_and_precio(cajonera_basica):
    assert cajonera_basica.num_cajones == 4
    assert cajonera_basica.tiene_ruedas is True
    precio = cajonera_basica.calcular_precio()
    assert precio >= cajonera_basica.precio_base


def test_cama_size_and_precio(cama_basica):
    assert cama_basica.tamaño == "king"
    # precio should increase when incluye_colchon
    p = cama_basica.calcular_precio()
    assert p > cama_basica.precio_base


def test_escritorio_properties(escritorio_basico):
    assert escritorio_basico.forma == "L"
    assert escritorio_basico.tiene_cajones is True
    assert escritorio_basico.num_cajones == 3
    assert escritorio_basico.calcular_precio() >= escritorio_basico.precio_base


def test_comedor_composition_and_price(comedor_basico):
    assert comedor_basico.mesa is not None
    assert len(comedor_basico.sillas) == 6
    precio_total = comedor_basico.calcular_precio_total()
    expected = comedor_basico.mesa.calcular_precio() + sum(
        s.calcular_precio() for s in comedor_basico.sillas
    )
    assert precio_total == expected


def test_comedor_add_remove_and_limits(comedor_basico):
    silla_extra = Silla("Silla Extra", "Madera", "Marron", 60.0)
    # capacity default from mesa is 6 -> adding should be blocked
    res = comedor_basico.agregar_silla(silla_extra)
    assert "No se pueden agregar" in res or "agregada" in res
    # quitar sillas until none left
    for _ in range(len(comedor_basico.sillas)):
        comedor_basico.quitar_silla()
    assert comedor_basico.quitar_silla() == "No hay sillas para quitar"
