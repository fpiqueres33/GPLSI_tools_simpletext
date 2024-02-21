from collections import Counter

import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


class TextPreprocessor:
    def __init__(self):
        self.nlp = spacy.load("es_core_news_sm")

        # Definimos las palabras de parada en español
        self.stop_words = self.nlp.Defaults.stop_words

    def process_text(self, text):
        """
        Procesa el texto usando la librería SpaCy y devuelve un objeto Doc de spaCy.
        """
        return self.nlp(text)

    def sentence_segment(self, text):
        """
        Segmenta el texto en oraciones.
        """
        doc = self.nlp(text)
        return [sent.text for sent in doc.sents]

    def detect_redundancy(self, sentences):
        """
        Detecta y filtra oraciones redundantes mediante similitud coseno utilizando TfidfVectorizer.
        """
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(sentences)

        non_redundant_sentences = [sentences[0]]
        redundant_sentences = set()

        for i in range(1, len(sentences)):
            is_redundant = False
            for non_redundant_sentence in non_redundant_sentences:
                non_redundant_vector = vectorizer.transform([non_redundant_sentence])
                current_vector = vectorizer.transform([sentences[i]])
                cos_sim = linear_kernel(non_redundant_vector, current_vector).flatten()[0]

                if cos_sim > 0.5:
                    is_redundant = True
                    break

            if not is_redundant:
                non_redundant_sentences.append(sentences[i])
            else:
                redundant_sentences.add(sentences[i])

        return non_redundant_sentences, list(redundant_sentences)

    def word_tokenization(self, sentences):
        """
        Tokeniza las oraciones en palabras.
        """
        return [[token for token in self.nlp(sentence)] for sentence in sentences]

    def lemmatization(self, tokens_list):
        """
        Lematiza las palabras.
        """
        return [[token.lemma_ for token in tokens] for tokens in tokens_list]

    def generate_topics(self, lemmas, num_topics=50, include_freq=False):
        """
        Genera temas principales del texto basándose en la frecuencia de los lemas.
        """

        all_lemmas = [lemma for sublist in lemmas for lemma in sublist if
                      lemma.strip() and lemma not in self.stop_words and len(lemma) > 1]
        lemma_count = Counter(all_lemmas)
        common_lemmas = lemma_count.most_common(num_topics)

        if include_freq:
            return common_lemmas
        else:
            return [lemma for lemma, _ in common_lemmas]
