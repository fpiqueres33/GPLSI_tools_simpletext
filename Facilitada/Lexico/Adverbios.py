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
            "efectivamente": "en efecto",
            "únicamente": "solo",
            "posiblemente": "lo mas seguro es que",
            "probablemente": "lo mas seguro es que",
            "seguramente": "lo mas seguro es",
            "seguidamente": "a continuación",
            "igualmente": "además",
            "análogamente": "de igual forma",
            "particularmente": "en particular",
            "realmente": "en verdad",
            "indudablemente": "sin lugar a dudas",
            "evidentemente": "es evidente",
            "apasionadamente": "de forma apasionada"

        }

    def detectar_adverbios_mente(self, texto):
        doc = self.nlp(texto)
        adverbios_mente = []
        for token in doc:
            if token.text.lower() in self.diccionario_adverbios or (
                    token.text.endswith("mente") and token.pos_ == "ADJ"):
                # Añadir el texto del token y su etiqueta POS.
                adverbios_mente.append((token.text, token.pos_))
        return adverbios_mente

    def sustituir_adverbios(self, texto):
        doc = self.nlp(texto)
        texto_modificado = ""
        for token in doc:
            texto_token = token.text

            # Priorizar la sustitución desde el diccionario
            if texto_token.lower() in self.diccionario_adverbios:
                sustitucion = self.diccionario_adverbios[texto_token.lower()]
                sustitucion = sustitucion if not texto_token[0].isupper() else sustitucion.capitalize()
            # Si no está en el diccionario pero termina en 'mente' y es un adverbio, usar transformación general
            elif texto_token.endswith('mente') and token.pos_ == 'ADV':
                adjetivo = texto_token[:-5]  # Quitar 'mente'
                sustitucion = f'de manera {adjetivo}'
                sustitucion = sustitucion if not texto_token[0].isupper() else sustitucion.capitalize()
            else:
                sustitucion = texto_token

            # Añadir el token modificado o no modificado al texto final
            texto_modificado += token.whitespace_ + sustitucion if token.i == 0 else sustitucion + token.whitespace_

        return texto_modificado
