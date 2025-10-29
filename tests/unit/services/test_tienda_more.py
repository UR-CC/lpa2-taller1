from unittest.mock import Mock

from src.models.concretos.mesa import Mesa
from src.models.concretos.silla import Silla
from src.services.tienda import TiendaMuebles


class TestTiendaMore:
    def test_estadisticas_reporte_vacio(self):
        t = TiendaMuebles()
        stats = t.obtener_estadisticas()
        assert isinstance(stats, dict)
        reporte = t.generar_reporte_inventario()
        assert "Total de muebles" in reporte

    def test_agregar_producto_y_filtrar(self):
        t = TiendaMuebles()
        s = Silla("S1", "Madera", "Negro", 80.0)
        t.agregar_producto(s)
        assert s in t.inventario
        res = t.filtrar_por_precio(0, 100)
        assert s in res

    def test_aplicar_descuento_no_valido(self):
        t = TiendaMuebles()
        msg = t.aplicar_descuento("sillas", 0)
        assert "Error" in msg

    def test_calcular_valor_inventario_with_errors(self):
        t = TiendaMuebles()
        bad = Mock()
        bad.calcular_precio.side_effect = Exception("boom")
        s = Silla("S1", "Madera", "Negro", 80.0)
        t.agregar_producto(bad)
        t.agregar_producto(s)
        total = t.calcular_valor_inventario()
        assert total >= s.calcular_precio()

    def test_obtener_muebles_por_tipo_and_count(self):
        t = TiendaMuebles()
        s = Silla("S1", "Madera", "Negro", 80.0)
        m = Mesa("M1", "Madera", "Marron", 200.0)
        t.agregar_producto(s)
        t.agregar_producto(m)
        res = t.obtener_muebles_por_tipo(Silla)
        assert all(isinstance(x, Silla) for x in res)
        conteo = t._contar_tipos_muebles()
        assert conteo.get("Silla", 0) >= 1

    def test_realizar_venta_error_in_calculo(self):
        t = TiendaMuebles()
        bad = Mock()
        bad.calcular_precio.side_effect = Exception("boom")
        bad.nombre = "Bad"
        t.agregar_producto(bad)
        res = t.realizar_venta(bad)
        assert "error" in res

    def test_realizar_venta_updates_accumulators(self):
        t = TiendaMuebles()
        s = Silla("S1", "Madera", "Negro", 80.0)
        t.agregar_producto(s)
        t.aplicar_descuento("sillas", 10)
        venta = t.realizar_venta(s, cliente="Ana")
        assert venta["cliente"] == "Ana"
        assert t._total_muebles_vendidos >= 1
        assert t._valor_total_ventas >= venta["precio_final"]
