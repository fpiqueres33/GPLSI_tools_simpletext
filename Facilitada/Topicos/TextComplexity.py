import syllables
import spacy

class TextComplexityCalculator:
    def __init__(self):
        self.nlp = spacy.load("es_core_news_sm")

    def calculate_complexity(self, text):
        # Procesa el texto para convertirlo en un documento spaCy
        processed_doc = self.nlp(text)

        total_sentences = len(list(processed_doc.sents))
        total_words = len([token for token in processed_doc if not token.is_punct])
        total_syllables = sum(syllables.estimate(token.text) for token in processed_doc if not token.is_punct)
        complex_words = sum(1 for token in processed_doc if not token.is_punct and syllables.estimate(token.text) > 2)


        # Fórmula de Flesch-Kincaid
        fk_score = round(.39 * words_per_sentence + 11.8 * syllables_per_word - 15.59, 2)
        # Índice de Gunning Fog
        gf_score = round(0.4 * (words_per_sentence + complex_words_percentage), 2)
        # Fórmula de Fernández Huerta
        fh_score = round(206.835 - 1.015 * words_per_sentence - 84.6 * syllables_per_word, 2)
        # Fórmula simplificada de la fórmula de Fernández Huerta para demostrar la similitud
        fs_score = round(206.835 - words_per_sentence - 62.3 * syllables_per_word, 2)

        return fk_score, gf_score, fh_score, fs_score
import spacy

class TextComplexityCalculator:
    def __init__(self):
        # Carga el modelo de spaCy al inicializar la clase
        self.nlp = spacy.load("es_core_news_sm")

    def calculate_complexity(self, text):
        # Procesa el texto para convertirlo en un documento spaCy
        processed_doc = self.nlp(text)

        total_sentences = len(list(processed_doc.sents))
        total_words = len([token for token in processed_doc if not token.is_punct])
        total_syllables = sum(syllables.estimate(token.text) for token in processed_doc if not token.is_punct)
        complex_words = sum(1 for token in processed_doc if not token.is_punct and syllables.estimate(token.text) > 2)

        fk_score = round(.39 * (total_words / total_sentences) + 11.8 * (total_syllables / total_words) - 15.59, 2)
        gf_score = round(0.4 * ((total_words / total_sentences) + 100 * (complex_words / total_words)), 2)
        fh_score = round(206.835 - 1.015 * (total_words / total_sentences) - 84.6 * (total_syllables / total_words), 2)


        return fk_score, gf_score, fh_score
