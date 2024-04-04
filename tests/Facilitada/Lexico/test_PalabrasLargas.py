import pytest
from Facilitada.Lexico.PalabrasLargas  import PalabrasLargas

class TestPalabrasLargas:

    def test_detectar_palabras_largas(self):
        """Prueba la detección de palabras largas en un texto."""
        detector = PalabrasLargas()
        texto_prueba = "Este es un texto de prueba con algunas palabraslargas incluyendo supercalifragilisticoespialidoso y arqueoantropología."
        resultado_esperado = ['palabraslargas', 'supercalifragilisticoespialidoso', 'arqueoantropología']

        # Comprobar que la lista de palabras largas coincide con el resultado esperado
        assert detector.detectar_palabras_largas(texto_prueba) == resultado_esperado

        # Prueba con un texto que contiene números
        texto_con_numeros = "Este texto contiene números como 123456789012 y palabras con longitud suficiente como internacionalización."
        resultado_esperado_numeros = ['internacionalización']

        # Comprobar que los números no se incluyen en la lista de resultados
        assert detector.detectar_palabras_largas(texto_con_numeros) == resultado_esperado_numeros

# Para ejecutar los tests, utiliza el comando `pytest` en tu terminal en el directorio que contiene el archivo test.
