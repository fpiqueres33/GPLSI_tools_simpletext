import pytest
from Facilitada.Lexico.Romanos import Romanos

class TestRomanos():

    def test_detectar_romanos(self):
        romanos = Romanos()
        texto_prueba = "En el año MMXX se celebraron los Juegos Olímpicos."
        romanos_esperados = ['MMXX']
        assert romanos.detectar_romanos_sin_loc(texto_prueba) == romanos_esperados

    def test_roman_to_arabic(self):
        romanos = Romanos()
        assert romanos.roman_to_arabic("MMXX") == 2020
        assert romanos.roman_to_arabic("IV") == 4

    def test_reemplazar_romanos(self):
        romanos = Romanos()
        texto_prueba = "En el año MMXX se celebraron los Juegos Olímpicos."
        texto_esperado = "En el año 2020 se celebraron los Juegos Olímpicos."
        assert romanos.reemplazar_romanos(texto_prueba) == texto_esperado

    def test_reemplazar_ordinales_en_nombres(self):
        romanos = Romanos()
        # esta función se realiza después de la primera transformación de romanos.
        # Por tanto debe detectar NER (entidad propia) que es PER (persona) con un número arábigo en el token siguiente.
        texto_prueba = "Se fue Juan 5 de la habitación."
        texto_esperado = "Se fue Juan quinto de la habitación."
        assert romanos.reemplazar_ordinales_en_nombres(texto_prueba) == texto_esperado

if __name__ == '__main__':
    pytest.main()
