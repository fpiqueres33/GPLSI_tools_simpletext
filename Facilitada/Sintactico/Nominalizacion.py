import spacy
import re

class Nominalizacion:
    def __init__(self, modelo='es_core_news_sm'):
        self.nlp = spacy.load(modelo)
        # Diccionario de excepciones
        self.excepciones = {'primer': True,
                            'azúcar': True,
                            'lugar': True,
                            'oscar': True,
                            'óscar': True,
                            'mujer': True,  #en principio no es necesaria al ser femenimo La mujer no entraría en el código de detección.
                            'taller': True,
                            'trailer': True,
                            'ayer': True,
                            'mayer': True,
                            'camper': True,
                            }

    def detectar_nominalizacion(self, texto):
        doc = self.nlp(texto)
        posiciones = []

        for token in doc:
            if token.text.lower().endswith(('ar', 'er', 'ir')) and not self.excepciones.get(token.text.lower(), False):
                if token.pos_ == "VERB" or (token.i > 0 and doc[token.i - 1].lower_ == 'el'):
                    inicio = doc[token.i - 1].idx if (token.i > 0 and doc[token.i - 1].lower_ == 'el') else token.idx
                    fin = inicio + len(doc[token.i - 1].text) + len(token.text) if (
                        token.i > 0 and doc[token.i - 1].lower_ == 'el') else token.idx + len(token.text)
                    es_capitalizado = doc[token.i - 1].text[0].isupper() if (
                        token.i > 0 and doc[token.i - 1].lower_ == 'el') else token.text[0].isupper()
                    posiciones.append((inicio, fin, es_capitalizado, token.text))

        return posiciones

    def reemplazar_nominalizacion(self, texto):
        posiciones = self.detectar_nominalizacion(texto)
        texto_modificado = texto

        for inicio, fin, es_capitalizado, verbo in sorted(posiciones, reverse=True):
            # Comprobar si hay un punto justo después del verbo y ajustar `fin` si es necesario
            preservar_punto = texto[fin] == '.' if fin < len(texto) else False
            fin_ajustado = fin + 1 if preservar_punto else fin

            # Extraer el verbo correctamente y aplicar las transformaciones necesarias
            verbo_extraido = texto[inicio:fin].strip()
            if es_capitalizado:
                verbo_extraido = verbo_extraido.capitalize()

            # Aplicar re.sub para asegurar que no duplicamos 'r'
            verbo_extraido = re.sub(r'rr$', 'r', verbo_extraido)

            reemplazo = verbo_extraido + ('.' if preservar_punto else '')

            # Realizar el reemplazo en el texto
            texto_modificado = texto_modificado[:inicio] + reemplazo + texto_modificado[fin_ajustado:]

        return texto_modificado

    def detectar_construcciones(self, texto):
        doc = self.nlp(texto)
        nominalizaciones = []
        impersonales = []

        for token in doc:
            if token.text.lower().endswith(('ar', 'er', 'ir')) and token.pos_ == "VERB":
                if token.i > 0 and doc[token.i - 1].lower_ == 'el':
                    nominalizaciones.append(f'{doc[token.i-1].text} {token.text}')
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
