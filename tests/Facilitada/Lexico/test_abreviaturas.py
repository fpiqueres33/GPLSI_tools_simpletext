import pytest
from Facilitada.Lexico.Abreviaturas import Abreviaturas

class TestAbreviaturas:
    # Diccionario de abreviaturas para usar en las pruebas
    diccionario_prueba = {
        "a. m.": "ante meridiem",
        "p. m.": "post meridiem",
        "etc.": "et cetera.",
        "e.g.": "for example",
        "i.e.": "that is"
    }

    def setup_method(self):
        """Método para crear una instancia de la clase Abreviaturas con un diccionario de prueba antes de cada prueba."""
        self.instancia_abreviaturas = Abreviaturas(self.diccionario_prueba)

    def test_sustituir_abreviaturas(self):
        texto_prueba = "Las reuniones son a las 9 a. m. y a las 5 p. m., etc."
        resultado_esperado = "Las reuniones son a las 9 ante meridiem y a las 5 post meridiem, et cetera."
        assert self.instancia_abreviaturas.sustituir_abreviaturas(texto_prueba) == resultado_esperado, "El texto modificado no coincide con el esperado."

    def test_detectar_abreviaturas(self):
        texto_prueba = "Por ejemplo (e.g.) y es decir (i.e.) son abreviaturas comunes."
        abreviaturas_esperadas = ["e.g.", "i.e."]
        resultado = self.instancia_abreviaturas.detectar_abreviaturas(texto_prueba)
        assert all(item in resultado for item in abreviaturas_esperadas), "No se detectaron correctamente todas las abreviaturas."
        assert len(resultado) == len(abreviaturas_esperadas), "El número de abreviaturas detectadas no coincide con el esperado."

    def test_sustituir_sin_abreviaturas(self):
        texto_prueba = "Este texto no contiene abreviaturas."
        assert self.instancia_abreviaturas.sustituir_abreviaturas(texto_prueba) == texto_prueba, "El texto no debería haber cambiado."

    def test_detectar_sin_abreviaturas(self):
        texto_prueba = "Este texto no contiene abreviaturas."
        assert len(self.instancia_abreviaturas.detectar_abreviaturas(texto_prueba)) == 0, "No deberían detectarse abreviaturas."
