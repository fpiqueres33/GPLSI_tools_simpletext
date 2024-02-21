import spacy
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

class Preproceso_texto:
    def __init__(self):
        # Cargar el modelo de procesamiento de lenguaje de spaCy para español
        self.nlp = spacy.load("es_core_news_sm")
        # Descargar los recursos necesarios de NLTK para el tokenizado de oraciones y palabras
        nltk.download("punkt")   #SOLO LA PRIMERA VEZ DE EJECUCION DEL PROGRAMA

    def procesar_texto_spacy(self, texto):
        # Procesar el texto utilizando spaCy
        doc = self.nlp(texto)
        tokens_spacy = [token.text for token in doc]
        return tokens_spacy

    def procesar_texto_nltk(self, texto):
        # Tokenizar el texto en oraciones utilizando NLTK
        oraciones = sent_tokenize(texto)

        # Tokenizar cada oración en palabras utilizando NLTK
        tokens_nltk = []
        for oracion in oraciones:
            palabras = word_tokenize(oracion)
            tokens_nltk.extend(palabras)

        return tokens_nltk