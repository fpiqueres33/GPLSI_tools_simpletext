import pytest
from Facilitada.Lexico.Numeros import Numero


class TestNumeros():


# Prueba para reemplazar números en un texto
    def test_reemplazar_numeros(self):
        num_instance = Numero()
        input_text = "El precio es de doscientos treinta y cuatro dólares."
        expected_output = "El precio es de más de doscientos dólares."
        assert num_instance.reemplazar_numeros(input_text) == expected_output


    # Prueba para detectar fechas en un texto
    def test_detectar_fechas(self):
        num_instance = Numero()
        input_text = "La fecha de inicio es el 12/03/22 y la fecha de fin es el 25/12/2022."
        expected_dates = ["12/03/22", "25/12/2022"]
        assert num_instance.detectar_numeros(input_text)['fechas'] == expected_dates


    # Prueba para transformar horas en un texto
    def test_transformar_horas(self):
        num_instance = Numero()
        input_text = "La reunión es a las 15:30 horas."
        expected_output = "La reunión es a las 3 y media de la tarde."
        assert num_instance.reemplazar_numeros(input_text) == expected_output


    # Prueba para detectar números de teléfono en un texto
    def test_detectar_numeros_telefono(self):
        num_instance = Numero()
        input_text = "Mi número de teléfono es 111222333."
        expected_phone_numbers = ["111222333"]
        assert num_instance.detectar_numeros(input_text)['números de teléfono'] == expected_phone_numbers


    # Prueba para transformar porcentajes en un texto
    def test_transformar_porcentajes(self):
        num_instance = Numero()
        input_text = "El 20% de los participantes completaron la encuesta."
        expected_output = "El 2 de cada 10 de los participantes completaron la encuesta."
        assert num_instance.reemplazar_numeros(input_text) == expected_output


    # Prueba para detectar otros números en un texto
    def test_detectar_otros_numeros(self):
        num_instance = Numero()
        input_text = "Hay 5000 personas en el evento."
        expected_numbers = ["5000"]
        assert num_instance.detectar_numeros(input_text)['otros números'] == expected_numbers


    # Prueba para transformar números escritos como texto en un texto
    def test_transformar_numeros_escritos(self):
        num_instance = Numero()
        input_text = "veinticinco gatos y doscientos perros estaban en el parque."
        expected_output = "25 gatos y 200 perros estaban en el parque."
        assert num_instance.reemplazar_numeros(input_text) == expected_output


if __name__ == '__main__':
    pytest.main()
