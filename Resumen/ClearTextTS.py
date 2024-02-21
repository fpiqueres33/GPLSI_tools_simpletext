from Resumen.TextNer import TextNer
from Resumen.TextPreprocessor import *
from Resumen.TextSummarizer import TextSummarizer


class ClearTextTS:
    def __init__(self):
        self.preprocessor = TextPreprocessor()
        self.summarizer = TextSummarizer(self.preprocessor)
        self.ner = TextNer()

    def generate_summary(self, text, summary_length_percentage=20, topics_count=20, include_ner=False):
        # Procesar el texto y preparar para el resumen
        doc = self.preprocessor.process_text(text)
        sentences = self.preprocessor.sentence_segment(text)
        non_redundant_sentences, _ = self.preprocessor.detect_redundancy(sentences)
        tokens = self.preprocessor.word_tokenization(non_redundant_sentences)
        lemmas = self.preprocessor.lemmatization(tokens)
        main_topics = self.preprocessor.generate_topics(lemmas, num_topics=topics_count, include_freq=True)

        # Calcular la relevancia de cada oración con respecto a los tópicos principales
        sentence_weights = self.summarizer.calculate_relevance_score(non_redundant_sentences, lemmas, main_topics)

        # Establecer el percentil basado en el porcentaje deseado de resumen
        percentile = summary_length_percentage

        # Encontrar las oraciones más relevantes
        top_sentences = self.summarizer.find_top_sentences(sentence_weights, non_redundant_sentences,
                                                           percentile=percentile)

        # Generar el resumen
        summary = ' '.join([sentence for sentence, _ in top_sentences])

        # Incluir NER
        ner_info = self.ner.named_entity_recognition(doc) if include_ner else None

        return {
            'summary': summary,
            'ner': ner_info

        }
