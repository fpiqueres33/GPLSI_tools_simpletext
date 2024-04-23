import spacy

class Nominalizacion:
    def __init__(self, modelo='es_core_news_sm'):
        self.nlp = spacy.load(modelo)
        self.excepciones = {
            'primer': True, 'azúcar': True, 'lugar': True, 'oscar': True,
            'óscar': True, 'mujer': True, 'taller': True, 'trailer': True,
            'ayer': True, 'mayer': True, 'camper': True,
        }

    def detectar_nominalizacion(self, texto):
        doc = self.nlp(texto)
        posiciones = []

        for token in doc:
            # Comprobar que el token es un verbo o que está precedido por "el"
            if token.text.lower().endswith(('ar', 'er', 'ir')) and not self.excepciones.get(token.text.lower(), False):
                if token.pos_ == "VERB" or (token.i > 0 and doc[token.i - 1].lower_ == 'el'):
                    inicio = doc[token.i - 1].idx if (token.i > 0 and doc[token.i - 1].lower_ == 'el') else token.idx
                    fin = doc[token.i].idx + len(doc[token.i].text)
                    es_capitalizado = doc[token.i - 1].text[0].isupper() if (
                        token.i > 0 and doc[token.i - 1].lower_ == 'el') else token.text[0].isupper()
                    posiciones.append((inicio, fin, es_capitalizado, token.text))

        return posiciones

    def reemplazar_nominalizacion(self, texto):
        posiciones = self.detectar_nominalizacion(texto)
        texto_modificado = texto

        for inicio, fin, es_capitalizado, verbo in sorted(posiciones, reverse=True):
            verbo_extraido = verbo.capitalize() if es_capitalizado else verbo

            # Realizar el reemplazo en el texto
            texto_modificado = texto_modificado[:inicio] + verbo_extraido + texto_modificado[fin:]

        return texto_modificado

    def detectar_construcciones(self, texto):
        doc = self.nlp(texto)
        nominalizaciones = []
        impersonales = []

        for token in doc:
            if token.text.lower().endswith(('ar', 'er', 'ir')) and token.pos_ == "VERB":
                if token.i > 0 and doc[token.i - 1].lower_ == 'el':
                    nominalizaciones.append(f'{doc[token.i - 1].text} {token.text}')
            elif token.lower_ == 'se' and token.head.pos_ == 'VERB' and token.head.i > token.i:
                impersonales.append(f'{token.text} {token.head.text}')

        return {'nominalizaciones': nominalizaciones, 'impersonales': impersonales}

    def detectar_nominalizacion_solo_frases(self, texto):
        doc = self.nlp(texto)
        nominalizaciones = []

        for token in doc:
            if token.text.lower().endswith(('ar', 'er', 'ir')) and not self.excepciones.get(token.text.lower(), False):
                if token.i > 0 and doc[token.i - 1].lower_ == 'el':
                    nominalizacion = f'{doc[token.i - 1].text} {token.text}'
                    nominalizaciones.append(nominalizacion)

        return nominalizaciones

