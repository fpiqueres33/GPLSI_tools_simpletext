from Facilitada.Lexico.Adverbios import Adverbios
from Facilitada.Lexico.Numeros import Numero
from Facilitada.Lexico.Romanos import Romanos
from Facilitada.Lexico.Superlativos import Superlativos

from Facilitada.Sintactico.Impersonal import Impersonal
from Facilitada.Sintactico.Complejos import Complejos

class TextProcessorAPI:
    def __init__(self, use_adverbios=True, use_complejos=True, use_numero=True, use_romanos=True,
                 use_superlativos=True, use_impersonales=True, preprocesador=None):
        # Inicializar todos los detectores
        self.use_adverbios = use_adverbios
        self.use_complejos = use_complejos
        self.use_numero = use_numero
        self.use_romanos = use_romanos
        self.use_superlativos = use_superlativos
        self.use_impersonales = use_impersonales

        if use_adverbios:
            self.detector_adverbios = Adverbios(preprocesador)
        if use_complejos:
            self.detector_complejos = Complejos()
        if use_numero:
            self.detector_numero = Numero()
        if use_romanos:
            self.detector_romanos = Romanos()
        if use_superlativos:
            self.detector_superlativos = Superlativos()
        if use_impersonales:
            self.detector_impersonales = Impersonal()

    def process_text(self, text):
        processed_text = text

        if self.use_adverbios:
            processed_text = self.detector_adverbios.sustituir_adverbios(processed_text)
        if self.use_complejos:
            processed_text = self.detector_complejos.sustituir_articulo_infinitivo(processed_text)
            processed_text = self.detector_complejos.detectar_y_sustituir_conectores(processed_text)
        if self.use_romanos:
            processed_text = self.detector_romanos.reemplazar_romanos(processed_text)
            processed_text = self.detector_romanos.reemplazar_ordinales_en_nombres(processed_text)
        if self.use_superlativos:
            processed_text = self.detector_superlativos.reemplazar_superlativos(processed_text)
        if self.use_numero:
            processed_text = self.detector_numero.reemplazar_numeros(processed_text)
        #if self.use_impersonales:
        #    processed_text = self.detector_impersonales.reemplazar_nominalizacion(processed_text)
        #    processed_text = self.detector_impersonales.reemplazar_impersonal(processed_text, posiciones)

        return processed_text