from Facilitada.Lexico.Adverbios import Adverbios
from Facilitada.Lexico.Numeros import Numero
from Facilitada.Lexico.Superlativos import Superlativos
from Facilitada.Lexico.Abreviaturas import Abreviaturas
from Facilitada.Lexico.Acronimos import Acronimos
from Facilitada.Lexico.Romanos2 import Romanos2
from Facilitada.Lexico.Anglicismos import Anglicismos
from Facilitada.Lexico.PalabrasLargas import PalabrasLargas
from Facilitada.Lexico.PalabrasDificiles import PalabrasDificiles

class API_Lexico:
    def __init__(self, habilitar_adverbios=True, habilitar_superlativos=True, habilitar_numeros=True,
                 habilitar_romanos=True, habilitar_abreviaturas=True, habilitar_acronimos=True,
                 habilitar_anglicismos=True,
                 habilitar_palabras_largas=True, habilitar_palabras_dificiles=True ):
        # Configuraciones iniciales para cada tipo de transformación
        self.habilitar_adverbios = habilitar_adverbios
        self.habilitar_superlativos = habilitar_superlativos
        self.habilitar_numeros = habilitar_numeros
        self.habilitar_romanos = habilitar_romanos
        self.habilitar_abreviaturas = habilitar_abreviaturas
        self.habilitar_acronimos = habilitar_acronimos
        self.habilitar_anglicismos = habilitar_anglicismos
        self.habilitar_palabras_largas = habilitar_palabras_largas
        self.habilitar_palabras_dificiles = habilitar_palabras_dificiles

        # Inicializar las clases para cada transformación
        self.adverbios = Adverbios() if habilitar_adverbios else None
        self.superlativos = Superlativos() if habilitar_superlativos else None
        self.numeros = Numero() if habilitar_numeros else None
        self.romanos = Romanos2() if habilitar_romanos else None
        self.abreviaturas = Abreviaturas() if habilitar_abreviaturas else None
        self.acronimos = Acronimos() if habilitar_acronimos else None
        self.anglicismos = Anglicismos() if habilitar_anglicismos else None
        self.palabras_largas = PalabrasLargas() if habilitar_palabras_largas else None
        self.palabras_dificiles = PalabrasDificiles() if habilitar_palabras_dificiles else None

    def transformar_lexico(self, texto):
        # Aquí se aplicarán las transformaciones según la configuración
        texto_transformado = "\n"+texto
        glosario_lines = []
        glosario = ""

        if self.habilitar_abreviaturas and self.abreviaturas:
            texto_transformado = self.abreviaturas.sustituir_abreviaturas(texto_transformado)

        if self.habilitar_acronimos and self.acronimos:
            texto_transformado = self.acronimos.sustituir_acronimos(texto_transformado)

        if self.habilitar_anglicismos and self.anglicismos:
            glosario_lines += self.anglicismos.glosario_anglicismos(texto)

        if self.habilitar_adverbios and self.adverbios:
            texto_transformado = self.adverbios.sustituir_adverbios(texto_transformado)

        if self.habilitar_superlativos and self.superlativos:
            texto_transformado = self.superlativos.reemplazar_superlativos(texto_transformado)

        if self.habilitar_numeros and self.numeros:
            texto_transformado = self.numeros.reemplazar_numeros(texto_transformado)

        if self.habilitar_romanos and self.romanos:
            texto_transformado = self.romanos.reemplazar_romanos(texto_transformado)
            texto_transformado = self.romanos.reemplazar_ordinales_en_nombres(texto_transformado)

        # Añadir las palabras difíciles al glosario sin modificar el texto transformado
        if self.habilitar_palabras_dificiles and self.palabras_dificiles:
            glosario_lines += self.palabras_dificiles.glosario_palabras_dificiles(texto)

        if glosario_lines:  # Aseguramos agregar el glosario solo si hay detecciones.
            glosario = "\n\n".join(glosario_lines)

        return texto_transformado.lstrip('\n'), glosario

    def detecciones_lexico(self, texto):
        detecciones = {}

        if self.habilitar_abreviaturas and self.abreviaturas:
            detecciones['abreviaturas'] = self.abreviaturas.detectar_abreviaturas(texto)

        if self.habilitar_acronimos and self.acronimos:
            detecciones['acrónimos'] = self.acronimos.detectar_acronimos(texto)

        if self.habilitar_anglicismos and self.anglicismos:
            detecciones['anglicismos'] = self.anglicismos.detectar_anglicismos(texto)

        if self.habilitar_adverbios and self.adverbios:
            detecciones['adverbios'] = self.adverbios.detectar_adverbios_mente(texto)

        if self.habilitar_superlativos and self.superlativos:
            detecciones['superlativos'] = self.superlativos.detectar_superlativos(texto)

        if self.habilitar_numeros and self.numeros:
            detecciones['números'] = self.numeros.detectar_numeros(texto)

        if self.habilitar_romanos and self.romanos:
            detecciones['romanos'] = self.romanos.detectar_romanos(texto)

        if self.palabras_largas and self.palabras_largas:
            detecciones['palabras_largas'] = self.palabras_largas.detectar_palabras_largas(texto)

        if self.habilitar_palabras_dificiles and self.palabras_dificiles:
            detecciones['palabras_difíciles'] = self.palabras_dificiles.detectar_palabras_dificiles(texto)

        return detecciones


