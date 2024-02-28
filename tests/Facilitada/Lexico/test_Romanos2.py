import pytest
from Facilitada.Lexico.Romanos2 import Romanos2

class TestRomanos2:
    def setup_method(self):
        """Método para crear una instancia de la clase Romanos2 antes de cada prueba."""
        self.instancia_romanos = Romanos2()

    def test_detectar_romanos(self):
        texto = "En el año MMXX en plena pandemia."
        assert self.instancia_romanos.detectar_romanos(texto) == ['MMXX']

    def test_roman_to_arabic(self):
        assert self.instancia_romanos.roman_to_arabic('MMXX') == 2020
        assert self.instancia_romanos.roman_to_arabic('IV') == 4

    def test_reemplazar_romanos(self):
        texto = "En el año MMXX en plena pandemia."
        assert self.instancia_romanos.reemplazar_romanos(texto) == "En el año 2020 en plena pandemia."



    #
