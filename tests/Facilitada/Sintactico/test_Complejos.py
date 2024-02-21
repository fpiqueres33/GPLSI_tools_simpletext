import pytest
from Facilitada.Sintactico.Complejos import Complejos

class TestComplejos:

    @classmethod
    def setup_class(cls):
        cls.complejos_instance = Complejos()

    # Prueba para detectar y sustituir conectores complejos en un texto
    def test_detectar_y_sustituir_conectores(self):
        input_text = "A pesar de que hizo frío, salimos. Sin embargo, no nevó."
        expected_output = "Aunque hizo frío, salimos. Además, no nevó."
        assert self.complejos_instance.detectar_y_sustituir_conectores(input_text) == expected_output

    # Prueba para detectar conectores complejos en un texto
    def test_detectar_conectores_complejos(self):
        input_text = "En cuanto a la reunión, por lo tanto, será a las 3. Tan pronto como llegues, avísame."
        expected_connectors = ["En cuanto a", "por lo tanto", "Tan pronto como"]
        assert self.complejos_instance.detectar_conectores_complejos(input_text) == expected_connectors

if __name__ == '__main__':
    pytest.main()
