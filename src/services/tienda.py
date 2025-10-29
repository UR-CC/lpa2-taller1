"""Tienda de muebles — implementación ligera usada por los tests.

Esta versión es deliberadamente sencilla y tolerante a errores en los
objetos mueble (por ejemplo, si `calcular_precio()` lanza). Expone
`_inventario` (atributo interno) y también una propiedad `inventario`
para compatibilidad con distintos consumidores.
"""

from typing import Any, Dict, List, Optional, Type


class TiendaMuebles:
    def __init__(self, nombre: str = "Tienda") -> None:
        self.nombre: str = nombre
        # atributo interno que otros módulos en el repo esperan
        self._inventario: List[Any] = []
        self._descuentos: Dict[str, float] = {}
        self._total_muebles_vendidos: int = 0
        self._valor_total_ventas: float = 0.0

    # propiedad para compatibilidad con código que usa `inventario`
    @property
    def inventario(self) -> List[Any]:
        return self._inventario

    @inventario.setter
    def inventario(self, v: List[Any]) -> None:  # pragma: no cover - simple alias
        self._inventario = v

    def agregar_producto(self, producto: Any) -> None:
        if producto is None:
            return
        self._inventario.append(producto)

    def agregar_mueble(self, mueble: Any) -> str:
        if mueble is None:
            return "Error: mueble None"
        try:
            precio = mueble.calcular_precio()
        except Exception:
            return "Error al calcular precio"
        try:
            if precio <= 0:
                return "Error: precio inválido"
        except Exception:
            return "Error al validar precio"
        self._inventario.append(mueble)
        return "mueble agregado"

    def agregar_comedor(self, comedor: Any) -> str:
        if comedor is None:
            return "Error: comedor None"
        # intentar añadir el objeto compuesto como mueble (si aplica)
        try:
            res = self.agregar_mueble(comedor)
            if "agregado" in res:
                return res
        except Exception:
            pass
        # si no se pudo, intentar extraer mesa y sillas
        try:
            mesa = getattr(comedor, "mesa", None)
            sillas = getattr(comedor, "sillas", [])
            if mesa is not None:
                self.agregar_mueble(mesa)
            for s in sillas:
                self.agregar_producto(s)
            return "comedor agregado"
        except Exception:
            return "Error al agregar comedor"

    def vender_producto(self, nombre: str) -> bool:
        for p in list(self._inventario):
            if getattr(p, "nombre", None) == nombre:
                try:
                    self._inventario.remove(p)
                except ValueError:
                    return False
                # se deja print para trazabilidad en tests que puedan inspeccionarlo
                print(f"Vendido: {nombre}")
                return True
        return False

    def realizar_venta(self, mueble: Any, cliente: Optional[str] = None) -> Any:
        try:
            precio_original = mueble.calcular_precio()
        except Exception:
            return {"error": "no se pudo calcular precio"}

        tipo = type(mueble).__name__.lower()
        descuento_key: Optional[str] = None
        if f"{tipo}s" in self._descuentos:
            descuento_key = f"{tipo}s"
        elif tipo in self._descuentos:
            descuento_key = tipo

        descuento = int(self._descuentos.get(descuento_key, 0)) if descuento_key else 0
        precio_final = round(precio_original * (1 - descuento / 100.0), 2)

        self._total_muebles_vendidos += 1
        try:
            self._valor_total_ventas += precio_final
        except Exception:
            pass

        return {
            "mueble": getattr(mueble, "nombre", str(mueble)),
            "precio_original": precio_original,
            "descuento": descuento,
            "precio_final": precio_final,
            "cliente": cliente,
        }

    def calcular_valor_inventario(self) -> float:
        total = 0.0
        for p in self._inventario:
            try:
                total += float(p.calcular_precio())
            except Exception:
                continue
        return round(total, 2)

    def filtrar_por_precio(self, minimo: float, maximo: float) -> List[Any]:
        out: List[Any] = []
        for p in self._inventario:
            try:
                precio = float(p.calcular_precio())
            except Exception:
                continue
            if minimo <= precio <= maximo:
                out.append(p)
        return out

    def filtrar_por_material(self, material: str) -> List[Any]:
        return [p for p in self._inventario if getattr(p, "material", None) == material]

    def buscar_muebles_por_nombre(self, term: str) -> List[Any]:
        t = term.lower()
        return [
            p for p in self._inventario if t in str(getattr(p, "nombre", "")).lower()
        ]

    def obtener_muebles_por_tipo(self, tipo: Type) -> List[Any]:
        return [p for p in self._inventario if isinstance(p, tipo)]

    def _contar_tipos_muebles(self) -> Dict[str, int]:
        conteo: Dict[str, int] = {}
        for p in self._inventario:
            name = type(p).__name__
            conteo[name] = conteo.get(name, 0) + 1
        return conteo

    def obtener_estadisticas(self) -> Dict[str, Any]:
        return {
            "tipos_muebles": self._contar_tipos_muebles(),
            "total_muebles": len(self._inventario),
            "ventas": {
                "cantidad": self._total_muebles_vendidos,
                "valor": self._valor_total_ventas,
            },
        }

    def aplicar_descuento(self, categoria: str, porcentaje: float) -> str:
        try:
            porcentaje = float(porcentaje)
        except Exception:
            return "Error: porcentaje inválido"
        if porcentaje <= 0:
            return "Error: porcentaje debe ser > 0"
        self._descuentos[categoria.lower()] = porcentaje
        return "descuento aplicado"

    def generar_reporte_inventario(self) -> str:
        lines: List[str] = []
        lines.append("REPORTE DE INVENTARIO")
        lines.append(f"Total de muebles: {len(self._inventario)}")
        lines.append("")
        lines.append("MUEBLES:")
        for p in self._inventario:
            tipo = type(p).__name__
            nombre = getattr(p, "nombre", repr(p))
            lines.append(f" - {nombre} ({tipo})")
        if self._descuentos:
            lines.append("")
            lines.append("DESCUENTOS ACTIVOS")
            for k, v in self._descuentos.items():
                lines.append(f" - {k}: {v}%")
        return "\n".join(lines)

    def agregar_producto_directo(self, producto: Any) -> None:
        # alias útil en tests
        self.agregar_producto(producto)
