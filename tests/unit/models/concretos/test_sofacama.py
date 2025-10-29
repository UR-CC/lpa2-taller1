from src.models.concretos.sofacama import SofaCama


class TestSofaCama:
    def test_herencia_multiple(self):
        sofa_cama = SofaCama("Sofá Cama Moderno", "Tela", 500.0, 2, "Queen")

        # Verificar atributos de Sofa
        assert sofa_cama.capacidad_personas == 2

        # Verificar atributos de Cama (propiedad específica para evitar conflicto MRO)
        assert sofa_cama.tamaño_cama_sofacama == "queen"

        # Verificar método específico
        assert hasattr(sofa_cama, "convertir_a_cama")

    def test_resolucion_metodos(self):
        sofa_cama = SofaCama("Sofá Cama", "Cuero", 600.0, 1, "Full")

        # Verificar que usa el método correcto (MRO)
        precio = sofa_cama.calcular_precio()
        assert precio > 600.0  # Debe incluir recargos de ambas clases
