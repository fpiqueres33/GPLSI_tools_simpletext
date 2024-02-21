from Facilitada.Lexico.Adverbios import Adverbios
from Facilitada.Lexico.Numeros import Numero
from Facilitada.Lexico.Romanos import Romanos
from Facilitada.Lexico.Superlativos import Superlativos
from Facilitada.Lexico.Abreviaturas import Abreviaturas


class API_Lexico:
    def __init__(self, habilitar_adverbios=True, habilitar_superlativos=True, habilitar_numeros=True,
                 habilitar_romanos=True, habilitar_abreviaturas=True):
        # Configuraciones iniciales para cada tipo de transformación
        self.habilitar_adverbios = habilitar_adverbios
        self.habilitar_superlativos = habilitar_superlativos
        self.habilitar_numeros = habilitar_numeros
        self.habilitar_romanos = habilitar_romanos
        self.habilitar_abreviaturas = habilitar_abreviaturas

        # Inicializar las clases para cada transformación
        self.adverbios = Adverbios() if habilitar_adverbios else None
        self.superlativos = Superlativos() if habilitar_superlativos else None
        self.numeros = Numero() if habilitar_numeros else None
        self.romanos = Romanos() if habilitar_romanos else None
        self.abreviaturas = Abreviaturas() if habilitar_abreviaturas else None

    def transformar_lexico(self, texto):
        # Aquí se aplicarán las transformaciones según la configuración
        texto_transformado = texto

        if self.habilitar_abreviaturas and self.abreviaturas:
            texto_transformado = self.abreviaturas.sustituir_abreviaturas(texto_transformado)

        if self.habilitar_adverbios and self.adverbios:
            texto_transformado = self.adverbios.sustituir_adverbios(texto_transformado)

        if self.habilitar_superlativos and self.superlativos:
            texto_transformado = self.superlativos.reemplazar_superlativos(texto_transformado)

        if self.habilitar_numeros and self.numeros:
            texto_transformado = self.numeros.reemplazar_numeros(texto_transformado)

        if self.habilitar_romanos and self.romanos:
            texto_transformado = self.romanos.reemplazar_romanos(texto_transformado)
            texto_transformado = self.romanos.reemplazar_ordinales_en_nombres(texto_transformado)

        return texto_transformado

    def detecciones_lexico(self, texto):
        detecciones = {}

        if self.habilitar_abreviaturas and self.abreviaturas:
            detecciones['abreviaturas'] = self.abreviaturas.detectar_abreviaturas(texto)

        if self.habilitar_adverbios and self.adverbios:
            detecciones['adverbios'] = self.adverbios.detectar_adverbios_mente(texto)

        if self.habilitar_superlativos and self.superlativos:
            detecciones['superlativos'] = self.superlativos.detectar_superlativos(texto)

        if self.habilitar_numeros and self.numeros:
            detecciones['numeros'] = self.numeros.detectar_numeros(texto)

        if self.habilitar_romanos and self.romanos:
            detecciones['romanos'] = self.romanos.detectar_romanos_sin_loc(texto)

        return detecciones


