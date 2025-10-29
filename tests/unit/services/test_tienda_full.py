from unittest.mock import Mock

import pytest

from src.models.concretos.mesa import Mesa
from src.models.concretos.silla import Silla
from src.services.tienda import TiendaMuebles


class TestTiendaFull:
    @pytest.fixture
    def tienda(self):
        return TiendaMuebles()

    @pytest.fixture
    def silla(self):
        return Silla("Silla Test", "Madera", "Marrón", 100.0, 4, "Roble")

    def test_agregar_mueble_valido(self, tienda, silla):
        msg = tienda.agregar_mueble(silla)
        assert "agregado" in msg
        assert silla in tienda.inventario

    def test_realizar_venta_y_acumulativos(self, tienda, silla):
        tienda.agregar_mueble(silla)
        venta = tienda.realizar_venta(silla, cliente="Juan")
        assert isinstance(venta, dict)
        assert venta["mueble"] == "Silla Test"
        assert tienda._total_muebles_vendidos >= 1

    def test_aplicar_descuento_y_venta(self, tienda, silla):
        tienda.agregar_mueble(silla)
        tienda.aplicar_descuento("sillas", 10)
        venta = tienda.realizar_venta(silla)
        assert venta["descuento"] == 10
        assert venta["precio_final"] == round(venta["precio_original"] * 0.9, 2)

    def test_buscar_y_filtrar(self, tienda, silla):
        tienda.agregar_mueble(silla)
        res = tienda.buscar_muebles_por_nombre("Silla")
        assert silla in res
        res2 = tienda.filtrar_por_material("Madera")
        assert silla in res2

    def test_filtrar_por_precio_con_mesa(self, tienda, silla):
        mesa = Mesa(
            "Mesa Test", "Madera", "Marrón", 200.0, "rectangular", 120.0, 80.0, 75.0, 6
        )
        tienda.agregar_mueble(silla)
        tienda.agregar_mueble(mesa)
        low = tienda.filtrar_por_precio(0, 150)
        assert silla in low and mesa not in low
        high = tienda.filtrar_por_precio(150, 1000)
        assert mesa in high

    def test_agregar_comedor_y_reporte(self, tienda):
        mesa = Mesa("Mesa Reporte", "Madera", "Marrón", 150.0)
        silla = Silla("Silla Rep", "Madera", "Negro", 40.0)
        from src.models.composicion.comedor import Comedor

        comedor = Comedor("Comedor Rep", mesa, [silla])
        msg = tienda.agregar_comedor(comedor)
        assert "agregado" in msg
        reporte = tienda.generar_reporte_inventario()
        assert "REPORTE DE INVENTARIO" in reporte

    def test_agregar_producto_direct_and_invalids(self, tienda):
        silla = Silla("Silla Directa", "Madera", "Negro", 30.0)
        tienda.agregar_producto(silla)
        assert silla in tienda.inventario
        # agregar None
        msg = tienda.agregar_mueble(None)
        assert "Error" in msg
        # agregar mueble con precio inválido using mock
        bad = Mock()
        bad.calcular_precio.side_effect = Exception("boom")
        msg2 = tienda.agregar_mueble(bad)
        assert "Error al calcular" in msg2
