from unittest.mock import Mock

from src.models.concretos.silla import Silla
from src.services.tienda import TiendaMuebles


def test_vender_producto_true_false():
    t = TiendaMuebles()
    s = Silla("Vende", "Madera", "Negro", 70.0)
    t.agregar_producto(s)
    assert t.vender_producto("Vende") is True
    # ahora ya no existe
    assert t.vender_producto("Vende") is False


def test_agregar_comedor_none():
    t = TiendaMuebles()
    res = t.agregar_comedor(None)
    assert "Error" in res


def test_agregar_mueble_precio_cero():
    t = TiendaMuebles()
    bad = Mock()
    bad.calcular_precio.return_value = 0
    bad.nombre = "Cero"
    res = t.agregar_mueble(bad)
    assert "Error" in res
