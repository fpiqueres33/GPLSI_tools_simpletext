import spacy

class Impersonal:
    def __init__(self, modelo='es_core_news_sm'):
        self.nlp = spacy.load(modelo)

    def detectar_impersonal(self, texto):
        doc = self.nlp(texto)
        posiciones = []

        for token in doc:
            if token.lower_ == 'se' and token.head.pos_ == 'VERB' and token.head.i > token.i:
                inicio = token.idx
                fin = token.head.idx + len(token.head.text)
                es_capitalizado = token.text == token.text.capitalize()
                posiciones.append((inicio, fin, es_capitalizado, token.head.text))

        return posiciones

    def reemplazar_impersonal(self, texto):
        posiciones = self.detectar_impersonal(texto)
        texto_modificado = texto
        for inicio, fin, es_capitalizado, verbo in sorted(posiciones, reverse=True):
            ciudadano = 'La ciudadana o el ciudadano' if es_capitalizado else 'la ciudadana o el ciudadano'
            sustitucion = f'{ciudadano} {verbo}'
            texto_modificado = texto_modificado[:inicio] + sustitucion + texto_modificado[fin:]

        return texto_modificado

    def detectar_impersonal_solo_frases(self, texto):
        doc = self.nlp(texto)
        construcciones_impersonales = []

        for token in doc:
            if token.lower_ == 'se' and token.head.pos_ == 'VERB' and token.head.i > token.i:
                construccion = f'{token.text} {token.head.text}'
                construcciones_impersonales.append(construccion)

        return construcciones_impersonales
