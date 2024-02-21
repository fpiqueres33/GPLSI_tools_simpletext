import pytest
from Facilitada.Sintactico.Nominalizacion import Nominalizacion

class TestNominalizacion:

    @classmethod
    def setup_class(cls):
        cls.nominalizacion_instance = Nominalizacion()

    # Prueba para detectar nominalizaciones en un texto
    def test_detectar_nominalizacion(self):
        input_text = "El nadar es un buen ejercicio. El correr es saludable."
        expected_positions = [(0, 7, True, "nadar"), (31, 39, True, "correr")]
        assert self.nominalizacion_instance.detectar_nominalizacion(input_text) == expected_positions

    # Prueba para reemplazar nominalizaciones en un texto
    def test_reemplazar_nominalizacion(self):
        input_text = "El nadar es un buen ejercicio. El correr es saludable."
        expected_output = "Nadar es un buen ejercicio. Correr es saludable."
        assert self.nominalizacion_instance.reemplazar_nominalizacion(input_text) == expected_output

    # Prueba para detectar construcciones de nominalizaciones e impersonales en un texto
    def test_detectar_construcciones(self):
        input_text = "El nadar es un buen ejercicio. Se dice que el correr es saludable."
        expected_constructions = {'nominalizaciones': ["El nadar", "el correr"], 'impersonales': ["Se dice"]}
        assert self.nominalizacion_instance.detectar_construcciones(input_text) == expected_constructions

    # Prueba para detectar nominalizaciones solo en frases en un texto
    def test_detectar_nominalizacion_solo_frases(self):
        input_text = "El nadar es un buen ejercicio. El correr es saludable."
        expected_nominalizations = ["El nadar", "El correr"]
        assert self.nominalizacion_instance.detectar_nominalizacion_solo_frases(input_text) == expected_nominalizations
