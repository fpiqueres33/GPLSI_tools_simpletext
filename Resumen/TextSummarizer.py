class TextSummarizer:
    def __init__(self, text_preprocessor):
        self.text_preprocessor = text_preprocessor  # Guarda la referencia a TextPreprocessor

    def calculate_relevance_score(self, sentences, lemmas, main_topics):
        """
        Calcula los puntajes de relevancia para cada oración basándose en los temas principales y las características del texto.
        """
        sentence_weights = {}

        for idx, sentence in enumerate(sentences):
            doc = self.text_preprocessor.nlp(sentence)  # Usa nlp de TextPreprocessor
            np_count = sum(1 for chunk in doc.noun_chunks)
            lemma_list = lemmas[idx]

            # Convertir todas las palabras en lemma_list a minúsculas
            lemma_list_lower = [word.lower() for word in lemma_list]

            # Convertir todas las palabras en main_topics a minúsculas
            main_topics_lower = [(topic[0].lower(), topic[1]) for topic in main_topics]

            # Calcular tfw_sum usando las versiones en minúsculas de las palabras
            tfw_sum = sum(lemma_list_lower.count(topic[0]) * topic[1] for topic in main_topics_lower)

            if np_count == 0:
                sentence_weights[sentence] = 0
            else:
                sentence_weights[sentence] = tfw_sum / np_count

        return sentence_weights

    def find_top_sentences(self, sentence_weights, sentences, percentile=20):
        """
        Encuentra las oraciones principales según los pesos de relevancia y un percentil dado.
        """
        # Asegúrate de que el percentil esté en un rango válido
        percentile = max(0, min(100, percentile))

        # Calcula el número de oraciones a seleccionar
        num_sentences = len(sentences)
        num_to_select = max(1, int((percentile / 100) * num_sentences))  # Asegúrate de seleccionar al menos una oración

        # En lugar de ordenar todas las oraciones por peso y seleccionar las primeras num_to_select,
        # Selecciona las oraciones cuyos pesos están en el top num_to_select porcentajes de los pesos,
        # Se mantiene el orden de aparición en el texto. No ordenamos por relevancia.

        # Encuentra los valores de umbral para seleccionar las oraciones
        weights = list(sentence_weights.values())
        threshold = sorted(weights, reverse=True)[min(num_to_select, len(weights)) - 1]

        # Selecciona las oraciones que tienen un peso por encima del umbral y mantenlas en el orden original
        top_sentences = [(sentence, weight) for sentence, weight in sentence_weights.items() if weight >= threshold]

        return top_sentences

    def generate_summary(self, top_sentences):
        """
        Genera un resumen a partir de las oraciones seleccionadas.
        """
        summary = ' '.join([sentence for sentence, _ in top_sentences])
        return summary
