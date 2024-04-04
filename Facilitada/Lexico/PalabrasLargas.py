import spacy

class PalabrasLargas:

    def __init__(self):
        # Cargar modelo de spaCy para español
        self.nlp = spacy.load("es_core_news_sm")

    def dividir_texto_en_segmentos(self, texto, longitud_maxima=1000000):
        """
        Divide el texto en segmentos más pequeños para evitar sobrepasar el límite de spaCy.
        """
        for inicio in range(0, len(texto), longitud_maxima):
            yield texto[inicio:inicio+longitud_maxima]

    def detectar_palabras_largas(self, texto):
        palabras_largas = []

        # Procesar el texto en segmentos para evitar el error de longitud máxima
        for segmento in self.dividir_texto_en_segmentos(texto):
            doc = self.nlp(segmento)
            for token in doc:
                if token.like_num:
                    continue
                if not token.is_punct and not token.is_space and len(token.text) >= 12:
                    palabras_largas.append(token.text)

        return palabras_largas
