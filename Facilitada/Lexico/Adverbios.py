import spacy


class Adverbios:
    def __init__(self):
        self.nlp = spacy.load("es_core_news_sm")
        self.diccionario_adverbios = {
            "normalmente": "a menudo",
            "raramente": "pocas veces",
            "habitualmente": "de manera habitual",
            "frecuentemente": "de manera frecuente",
            "reiteradamente": "de manera reiterada",
            "cotidianamente": "de manera cotidiana",
            "ocasionalmente": "de manera ocasional",
            "esporádicamente": "de manera esporádica",
            "excepcionalmente": "de manera excepcional",
            "infrecuentemente": "de manera poco frecuente",
            "mensualmente": "cada mes",
            "anualmente": "cada año",
            "diariamente": "cada día",
            "cuatrimestralmente": "cada cuatro meses",
            "quincenalmente": "cada quincena",
            "semanalmente": "cada semana",
            "trimestralmente": "cada trimestre",
            "semestralmente": "cada seis meses",
            "primeramente": "en primer lugar",
            "segundamente": "en segundo lugar",
            "finalmente": "por último",
            "consecuentemente": "por eso",
            "resumidamente": "en resumen",
            "actualmente": "ahora",
            "antiguamente": "antes",
            "recientemente": "hace poco",
            "últimamente": "hace poco",
            "posteriormente": "después",
            "previamente": "antes",
            "inmediatamente": "en seguida",
            "afortunadamente": "por fortuna",
            "desgraciadamente": "por desgracia",
            "lamentablemente": "por desgracia",
            "solamente": "solo",
            "justamente": "justo",
            "efectivamente": "en efecto"
        }

    '''
    def detectar_tokens_spacy(self, texto):
        # Procesar el texto utilizando spaCy desde la instancia de Preproceso_texto
        doc = self.nlp(texto)
        tokens_info = [(token.text, token.pos_) for token in doc]
        return tokens_info
    '''

    def detectar_adverbios_mente(self, tokens_info):
        doc = self.nlp(tokens_info)
        adverbios_mente = [(token.text, token.pos_) for token in doc if
                           token.text.endswith("mente") and token.pos_ == "ADV"]
        return adverbios_mente


    def sustituir_adverbios(self, texto):
        doc = self.nlp(texto)
        texto_modificado = ""

        for token in doc:
            texto_token = token.text
            if token.pos_ == 'ADV' and (texto_token.endswith('mente') or texto_token in self.diccionario_adverbios):
                if texto_token in self.diccionario_adverbios:
                    sustitucion = self.diccionario_adverbios[texto_token]
                else:
                    adjetivo = texto_token[:-5]  # Quitar 'mente'
                    sustitucion = f'de forma {adjetivo}'
                sustitucion = sustitucion if not texto_token[0].isupper() else sustitucion.capitalize()

                # Añadir espacio antes del token si es necesario
                if not token.is_punct and not texto_modificado.endswith(' '):
                    texto_modificado += ' '
                texto_modificado += sustitucion

                # Añadir espacio después del token si el siguiente token no es de puntuación
                if token.whitespace_:
                    texto_modificado += ' '
            else:
                # Añadir espacio antes del token si es necesario
                if not token.is_punct and not texto_modificado.endswith(' '):
                    texto_modificado += ' '
                texto_modificado += texto_token

                # Añadir espacio después del token si el siguiente token no es de puntuación
                if token.whitespace_:
                    texto_modificado += ' '

        return texto_modificado




