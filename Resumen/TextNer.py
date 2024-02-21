from collections import Counter

import spacy


class TextNer:
    def __init__(self):
        self.nlp = spacy.load("es_core_news_sm")

    def named_entity_recognition(self, text):
        """
        Identifica y filtra entidades nombradas en el texto utilizando spaCy.
        """
        doc = self.nlp(text)
        named_entities = []

        for ent in doc.ents:
            if not ent.text[0].isupper():
                continue
            if ent.label_ != 'MISC':
                if len(ent.text.split()) == 1:
                    token = doc[ent.start]
                    if token.pos_ not in ['PROPN', 'NOUN']:
                        continue
                named_entities.append((ent.text, ent.label_))

        # Contar las frecuencias
        named_entities_freq = Counter(named_entities)

        # Ordenar por tipo de entidad y luego por frecuencia
        sorted_entities = sorted(named_entities_freq.items(), key=lambda x: (x[0][1], -x[1]))

        return sorted_entities
