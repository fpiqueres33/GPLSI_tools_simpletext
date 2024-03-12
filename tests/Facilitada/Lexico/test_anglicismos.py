import pytest
from Facilitada.Lexico.Anglicismos import Anglicismos

class TestAnglicismos:
    # Diccionario de anglicismos para usar en las pruebas
    diccionario_prueba = {
        "email": "correo electrónico",
        "feedback": "retroalimentación",
        "marketing": "mercadotecnia",
        "coach": "entrenador",
        "smartphone": "teléfono inteligente",
        "podcasts": "audios",
        "selfies": "autofotos"
    }

    def setup_method(self):
        """Método para crear una instancia de la clase Anglicismos con un diccionario de prueba antes de cada prueba."""
        self.instancia_anglicismos = Anglicismos(self.diccionario_prueba)

    def test_sustituir_anglicismos(self):
        texto_prueba = "Para mejorar tu marketing, considera enviar un email con feedback a tu coach."
        resultado_esperado = "Para mejorar tu mercadotecnia, considera enviar un correo electrónico con retroalimentación a tu entrenador."
        assert self.instancia_anglicismos.sustituir_anglicismos(texto_prueba) == resultado_esperado, "El texto modificado no coincide con el esperado."

    def test_detectar_anglicismos(self):
        texto_prueba = "Un smartphone puede ser útil para escuchar podcasts y hacer selfies."
        anglicismos_esperados = ["smartphone", "podcasts", "selfies"]
        resultado = self.instancia_anglicismos.detectar_anglicismos(texto_prueba)
        assert all(item in resultado for item in anglicismos_esperados), "No se detectaron correctamente todos los anglicismos."
        assert len(resultado) == len(anglicismos_esperados), "El número de anglicismos detectados no coincide con el esperado."

    def test_sustituir_sin_anglicismos(self):
        texto_prueba = "Este texto no contiene anglicismos."
        assert self.instancia_anglicismos.sustituir_anglicismos(texto_prueba) == texto_prueba, "El texto no debería haber cambiado."

    def test_detectar_sin_anglicismos(self):
        texto_prueba = "Este texto no contiene anglicismos."
        assert len(self.instancia_anglicismos.detectar_anglicismos(texto_prueba)) == 0, "No deberían detectarse anglicismos."
