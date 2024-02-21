import pytest
from Facilitada.Lexico.Adverbios import Adverbios

class TestAdverbios():

    def test_sustitucion_adverbio_simple(self):
        """Prueba la sustitución de un adverbio simple."""
        adverbios = Adverbios()
        texto_prueba = "Ella trabajaba rápidamente."
        resultado_esperado = "Ella trabajaba de forma rápida."  # Asegúrate de que este sea el resultado esperado
        assert adverbios.sustituir_adverbios(texto_prueba).strip() == resultado_esperado

    def test_sustitucion_adverbio_con_diccionario(self):
        """Prueba la sustitución de un adverbio usando el diccionario de excepciones."""
        adverbios = Adverbios()
        texto_prueba = "El trabajo se realizó normalmente."
        resultado_esperado = "El trabajo se realizó a menudo."  # Usando tu diccionario de adverbios
        assert adverbios.sustituir_adverbios(texto_prueba).strip() == resultado_esperado

    def test_detectar_adverbios_mente(self):
        adverbios = Adverbios()
        texto = "Ella habló rápidamente y actuó eficientemente."

        # Lista esperada de adverbios detectados
        adverbios_esperados = [('rápidamente', 'ADV'), ('eficientemente', 'ADV')]

        # Ejecuta la función de detección
        adverbios_detectados = adverbios.detectar_adverbios_mente(texto)

        # Verifica si la lista de adverbios detectados coincide con la lista esperada
        assert adverbios_detectados == adverbios_esperados

if __name__ == '__main__':
    pytest.main()
