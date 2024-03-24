from Facilitada.Sintactico.Complejos import Complejos
from Facilitada.Sintactico.Impersonal import Impersonal
from Facilitada.Sintactico.Nominalizacion import Nominalizacion


class ApiSintactico:

    def __init__(self, habilitar_nominalizacion=True, habilitar_impersonales=True, habilitar_complejos=True):
        # Configuraciones iniciales para cada tipo de transformación
        self.habilitar_nominalizacion = habilitar_nominalizacion
        self.habilitar_impersonales = habilitar_impersonales
        self.habilitar_complejos = habilitar_complejos

        # Inicializar las clases para cada transformación
        self.nominalizacion = Nominalizacion() if habilitar_nominalizacion else None
        self.impersonales = Impersonal() if habilitar_impersonales else None
        self.complejos = Complejos() if habilitar_complejos else None

    def transformar_sintactico(self, texto):
        # Aquí se aplicarán las transformaciones según la configuración
        texto_transformado = texto
        oraciones_impersonales = []
        sentence_impersonales = ""

        if self.habilitar_nominalizacion and self.nominalizacion:
            texto_transformado = self.nominalizacion.reemplazar_nominalizacion(texto_transformado)

        if self.habilitar_impersonales and self.impersonales:
            texto_transformado = self.impersonales.reemplazar_impersonal(texto_transformado)
            oraciones_impersonales = self.impersonales.detectar_impersonal_oraciones_completas(texto)

        if self.habilitar_complejos and self.complejos:
            texto_transformado = self.complejos.detectar_y_sustituir_conectores(texto_transformado)

        if oraciones_impersonales:  # Aseguramos agregar el glosario solo si hay oraciones impersonales
            sentence_impersonales = "\n".join(oraciones_impersonales)
            # texto_transformado += "\nORACIONES IMPERSONALES:\n" + oraciones

        return texto_transformado, sentence_impersonales

    def detecciones_sintactico(self, texto):
        detecciones = {}

        if self.habilitar_nominalizacion and self.nominalizacion:
            detecciones['nominalizaciones'] = self.nominalizacion.detectar_nominalizacion_solo_frases(texto)

        if self.habilitar_impersonales and self.impersonales:
            detecciones['impersonales'] = self.impersonales.detectar_impersonal_solo_frases(texto)

        if self.habilitar_complejos and self.complejos:
            detecciones['complejos'] = self.complejos.detectar_conectores_complejos(texto)

        return detecciones



