import spacy
from collections import Counter

class Topicos:
    def __init__(self):
        # Cargar el modelo de spaCy en español
        self.nlp = spacy.load("es_core_news_sm")
        # Definir las stopwords
        self.stopwords = self.nlp.Defaults.stop_words

    def procesar_texto(self, texto):
        # Procesar el texto con spaCy
        doc = self.nlp(texto)
        # Filtrar tokens que no son stopwords, no son puntuación y no son espacios
        tokens_filtrados = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct and not token.is_space]
        # Contar y ordenar los tokens por su frecuencia de aparición
        frecuencia_tokens = Counter(tokens_filtrados).most_common(10)
        return frecuencia_tokens


