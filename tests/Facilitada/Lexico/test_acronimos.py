import pytest
from Facilitada.Lexico.Acronimos import Acronimos

class TestAcronimos:
    # Diccionario de acrónimos para usar en las pruebas
    diccionario_prueba = {
        "OTAN": "Organización del Tratado del Atlántico Norte",
        "ONU": "Organización de Naciones Unidas",
    }

    def setup_method(self):
        """Método para crear una instancia de la clase Acronimos con un diccionario de prueba antes de cada prueba."""
        self.instancia_acronimos = Acronimos(self.diccionario_prueba)

    def test_sustituir_acronimos_simple(self):
        texto_prueba = "La finalidad de la OTAN es militar."
        resultado_esperado = "La finalidad de la OTAN es militar. OTAN Organización del Tratado del Atlántico Norte."
        assert self.instancia_acronimos.sustituir_acronimos(texto_prueba) == resultado_esperado, "El texto modificado no coincide con el esperado."

    def test_sustituir_acronimos_multiple(self):
        texto_prueba = "La OTAN y la ONU tienen roles internacionales. Ambas son importantes."
        resultado_esperado = "La OTAN y la ONU tienen roles internacionales. OTAN Organización del Tratado del Atlántico Norte. ONU Organización de Naciones Unidas. Ambas son importantes."
        assert self.instancia_acronimos.sustituir_acronimos(texto_prueba) == resultado_esperado, "El texto modificado no coincide con el esperado."

    def test_preservacion_de_estructura(self):
        texto_prueba = "La OTAN es importante.\nDebe ser respetada."
        resultado_esperado = "La OTAN es importante. OTAN Organización del Tratado del Atlántico Norte.\nDebe ser respetada."
        assert self.instancia_acronimos.sustituir_acronimos(texto_prueba) == resultado_esperado, "El texto modificado no preserva los saltos de línea originales."