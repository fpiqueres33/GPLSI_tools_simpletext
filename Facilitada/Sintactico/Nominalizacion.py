import spacy

class Nominalizacion:
    def __init__(self, modelo='es_core_news_sm'):
        self.nlp = spacy.load(modelo)


    def detectar_nominalizacion(self, texto):
        doc = self.nlp(texto)
        posiciones = []

        for token in doc:
            if token.text.lower().endswith(('ar', 'er', 'ir')):
                if token.i > 0 and doc[token.i - 1].lower_ == 'el':
                    inicio = doc[token.i - 1].idx  # Inicio debe ser el índice del artículo 'el'
                    fin = inicio + len(doc[token.i - 1].text) + len(
                        token.text)  # Fin debe incluir el artículo y el verbo
                    es_capitalizado = doc[token.i - 1].text == doc[token.i - 1].text.capitalize()
                    posiciones.append((inicio, fin, es_capitalizado, token.text))

        return posiciones

    def reemplazar_nominalizacion(self, texto):
        posiciones = self.detectar_nominalizacion(texto)
        texto_modificado = texto

        for inicio, fin, es_capitalizado, verbo in sorted(posiciones, reverse=True):
            # Calcula la longitud del artículo y el espacio ('el ' o 'El ')
            longitud_articulo = 3 if es_capitalizado else 2
            if es_capitalizado:
                verbo = verbo.capitalize()

            # Elimina solo 'el ' o 'El ' del artículo sin eliminar el verbo
            texto_modificado = texto_modificado[:inicio] + verbo + texto_modificado[fin+1:]

        return texto_modificado

    def detectar_construcciones(self, texto):
        doc = self.nlp(texto)
        nominalizaciones = []
        impersonales = []

        for token in doc:
            if token.text.lower().endswith(('ar', 'er', 'ir')):
                if token.i > 0 and doc[token.i - 1].lower_ == 'el':
                    nominalizaciones.append(f'{doc[token.i-1].text} {token.text}')
            elif token.lower_ == 'se' and token.head.pos_ == 'VERB' and token.head.i > token.i:
                impersonales.append(f'{token.text} {token.head.text}')

        return {'nominalizaciones': nominalizaciones, 'impersonales': impersonales}

    def detectar_nominalizacion_solo_frases(self, texto):
        doc = self.nlp(texto)
        nominalizaciones = []

        for token in doc:
            if token.text.lower().endswith(('ar', 'er', 'ir')):
                if token.i > 0 and doc[token.i - 1].lower_ == 'el':
                    nominalizacion = f'{doc[token.i - 1].text} {token.text}'
                    nominalizaciones.append(nominalizacion)

        return nominalizaciones

    '''
    # Otra opción consitente es utizar re para el pattern artículo +palabra terminada en -ar, -er, -ir. 
    # En los test funciona igual. Las excepciones podrían venir de lenguaje técnico con palabras de otros idiomas.
    
        
        def __init__(self):
        self.articulo_infinitivo_pattern = re.compile(r'\b(el|la|los|las) (\w+ar|\w+er|\w+ir)\b', re.IGNORECASE)

    def detectar_articulo_infinitivo(self, texto):
        # Método para detectar "artículo + infinitivo"
        articulos_infinitivos = self.articulo_infinitivo_pattern.findall(texto)
        return [" ".join(match) for match in articulos_infinitivos]

    def sustituir_articulo_infinitivo(self, text):
        def reemplazo(match):
            # Seleccionar el artículo y el infinitivo de la coincidencia
            articulo, infinitivo = match.groups()
            # Capitalizar el infinitivo si el artículo está en mayúsculas
            if articulo.istitle():
                infinitivo = infinitivo.capitalize()
            return infinitivo

        # Usar una función de reemplazo para verificar cada coincidencia y capitalizar si es necesario
        return self.articulo_infinitivo_pattern.sub(reemplazo, text)

    
    
    
    
    '''