import pytest
from Facilitada.Sintactico.Impersonal import Impersonal

class TestImpersonal:

    @classmethod
    def setup_class(cls):
        cls.impersonal_instance = Impersonal()

    # Prueba para detectar construcciones impersonales en un texto
    def test_detectar_impersonal(self):
        input_text = "Se dice que el sol es caliente. Se necesita ayuda urgente."
        expected_positions = [(0, 7, True, "dice"), (32, 43, True, "necesita")]
        assert self.impersonal_instance.detectar_impersonal(input_text) == expected_positions

    # Prueba para reemplazar construcciones impersonales en un texto
    def test_reemplazar_impersonal(self):
        input_text = "Se dice que el sol es caliente. Se necesita ayuda urgente."
        expected_output = "La ciudadana o el ciudadano dice que el sol es caliente. La ciudadana o el ciudadano necesita ayuda urgente."
        assert self.impersonal_instance.reemplazar_impersonal(input_text) == expected_output

    # Prueba para detectar construcciones impersonales solo en frases
    def test_detectar_impersonal_solo_frases(self):
        input_text = "Se dice que el sol es caliente. Se necesita ayuda urgente."
        expected_constructions = ["Se dice", "Se necesita"]
        assert self.impersonal_instance.detectar_impersonal_solo_frases(input_text) == expected_constructions
