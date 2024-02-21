import syllables

class TextComplexityCalculator:
    def __init__(self, doc):
        self.processed_doc = doc

    def calculate_complexity(self):
        """Calcula varios índices de legibilidad para evaluar la complejidad del texto."""
        total_sentences = len(list(self.processed_doc.sents))
        total_words = len([token for token in self.processed_doc if not token.is_punct])
        total_syllables = sum(syllables.estimate(token.text) for token in self.processed_doc if not token.is_punct)
        complex_words = sum(
            1 for token in self.processed_doc if not token.is_punct and syllables.estimate(token.text) > 2)

        fk_score = round(.39 * (total_words / total_sentences) + 11.8 * (total_syllables / total_words) - 15.59, 2)
        gf_score = round(0.4 * ((total_words / total_sentences) + 100 * (complex_words / total_words)), 2)
        fh_score = round(206.835 - 1.2 * (total_words / total_sentences) - 60 * (total_syllables / total_words), 2)
        fs_score = round(206.835 - (total_words / total_sentences) - 62.3 * (total_syllables / total_words), 2)

        return fk_score, gf_score, fh_score, fs_score