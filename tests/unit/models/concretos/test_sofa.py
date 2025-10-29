import pytest

from src.models.concretos.sofa import Sofa


class TestSofa:
    @pytest.fixture
    def sofa_basico(self):
        return Sofa("Sofá Básico", "Tela", "Gris", 300.0, 3, True, "Tela")

    def test_instanciacion_correcta(self, sofa_basico):
        # Verificar herencia de atributos
        assert sofa_basico.nombre == "Sofá Básico"
        assert sofa_basico.material == "Tela"
        assert sofa_basico.color == "Gris"
        assert sofa_basico.precio_base == 300.0
        assert sofa_basico.capacidad_personas == 3
        assert sofa_basico.tiene_respaldo is True
        assert sofa_basico.material_tapizado == "Tela"

    def test_calcular_precio(self, sofa_basico):
        # Verificar cálculo de precio con factor de comodidad
        precio = sofa_basico.calcular_precio()
        assert precio > 300.0  # Debe incluir recargos por comodidad

    def test_obtener_descripcion(self, sofa_basico):
        # Verificar que la descripción contiene los datos correctos
        descripcion = sofa_basico.obtener_descripcion()
        assert "Sofá Básico" in descripcion
        assert "Tela" in descripcion
