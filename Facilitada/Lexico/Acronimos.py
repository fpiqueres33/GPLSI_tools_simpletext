import spacy
import string

class Acronimos:
    def __init__(self, dict_acronimos=None):
        if dict_acronimos==None:
            dict_acronimos = {
                'AENOR': 'Asociación Española para la Normalización y Racionalización',
                'ALCA': 'Área de Libre Comercio de las Américas,',
                'AMPA': 'asociación de madres y padres de alumnos',
                'ANECA': 'Agencia Nacional de Evaluación de la Calidad y Acreditación',
                'APA': 'Asociación de Padres de Alumnos',
                'AVE': 'Alta Velocidad Española',
                'BENELUX': 'Belgium, the Netherlands, and Luxembourg (Unión Económica entre Bélgica, Holanda y Luxemburgo)',
                'BUP': 'Bachillerato Unificado Polivalente',
                'CA': 'Comunidad Autónoma',
                'CAM': 'Caja de Ahorros del Mediterraneo',
                'CAP': 'Certificado de Aptitud Pedagógica',
                'CEIP': 'colegio de enseñanza infantil y primaria',
                'CEPYME': 'Confederación Española de la Pequeña y Mediana Empresa',
                'CERMI': 'Comité Español de Representantes de Personas con Discapacidad',
                'CIA': 'Central Intelligence Agency (Servicio Central de Información)',
                'CIF': 'Código de Identificación fiscal.',
                'Conacyt': 'Consejo Nacional de Ciencia y Tecnología',
                'COPE': 'Cadena de Ondas Populares Españolas',
                'CORDE': 'Corpus Diacrónico del Español',
                'CREA': 'Corpus de referencia del español actual',
                'DIU': 'dispositivo intrauterino',
                'DRAE': 'Diccionario de la lengua española',
                'ELE': 'Español como lengua extranjera',
                'ENDESA': 'Empresa Nacional de Electricidad, S.A.',
                'ERE': 'Expediente de regulación de empleo',
                'ERTE': 'expediente de regulación temporal de empleo.',
                'ESO': 'Enseñanza Secundaria Obligatoria',
                'FARC-EP': 'Fuerzas Armadas Revolucionarias de Colombia - Ejército del Pueblo',
                'FEDER': 'Fondos Europeos de Desarrollo Regional',
                'FEMSA': 'Fábrica Española de Magnetos, S.A.',
                'FIB': 'Festival Internacional de Benicasim',
                'FIFA': 'Federación Internacional de Fútbol Asociació',
                'FITUR': 'Feria Internacional del Turismo',
                'Gestapo': 'Geheime Staatspolizei (Policía Secreta del Estado Nazi)',
                'IBI ': 'Impuesto sobre bienes inmuebles',
                'ICE': 'Instituto de Ciencias de la Educación',
                'IFEMA': 'Instituto Ferial de Madrid.',
                'Imserso': 'Instituto de Migraciones y Servicios Sociales; Instituto Municipal de Servicios Sociales',
                'Inem': 'Instituto Nacional de Empleo',
                'INTERPOL': 'Organización Internacional de Policía Criminal',
                'IVA': 'Impuesto sobre el Valor Añadido',
                'láser': 'light amplification by stimulated emission of radiation (luz amplificada por la emisión estimulada de radiación)',
                'LOE': 'Ley Orgánica del Estado',
                'LOGSE': 'Ley Ordenación General del Sistema Educativo',
                'MEC': 'Ministerio de Educación y Ciencia',
                'Mercosur': 'Mercado Común del Sur',
                'MIR': 'médico interno y residente',
                'módem': 'modulator-demodulator (modulador-demodulador)',
                'MUFACE': 'Mutualidad General de Funcionarios Civiles del Estado',
                'NASA': 'National Aeronautics and Space Administration (Administración Nacional de Aeronáutica y del Espacio)',
                'NIE': 'Número de Identidad de Extranjero',
                'NIF': 'Número de identificación Fiscal',
                'NU': 'Naciones Unidas',
                'OCU': 'Organización de Consumidores y Usuarios',
                'ONU': 'Organización de las Naciones Unidas',
                'OTAN': 'Organización del Tratado del Atlántico Norte',
                'OVNI': 'objeto volador/volante no identificado',
                'PIB': 'Producto interior bruto',
                'PIN': 'personal identification number (Número de Identificación Personal)',
                'PYME': 'pequeña y mediana empresa',
                'RAE': 'Real Academia Española',
                'RENFE': 'Red Nacional de los Ferrocarriles Españoles',
                'RR.HH': 'recursos humanos',
                'RR.PP': 'relaciones públicas',
                'TIC': 'Tecnologías de la información y la comunicación',
                'UEFA': 'Unión of European Football Associations (Unión de Asociaciones Europeas de Fútbol)',
                'UNED': 'Universidad Nacional de Educación a Distancia',
                'UNESCO, Unesco': 'United Nations Educational, Scientific and Cultural Organization (Organización de las Naciones Unidas para la Educación, la Ciencia y la Cultura)',
                'UNICEF, Unicef': "United Nations Children's Fund(Fondo de las Naciones Unidas para la Infancia",
                'Unesco': 'United Nations Educational, Scientific and Cultural Organization (Organización de las Naciones Unidas para la Educación, la Ciencia y la Cultura)',
                'Unicef': "United Nations Children's Fund(Fondo de las Naciones Unidas para la Infancia",
                'UVI':'Unidad de Vigilancia Intensiva',
                'VIP': 'Very Important Person (persona muy importante)',
                'VOSE': 'Versión original subtitulada en español',
                'VOSI': 'Versión original subtitulada en inglés',
                'Edusi': 'significa Estrategia de Desarrollo Urbano Sostenible e Integrado ',
                'MACA': 'Museo de Arte Contemporáneo de Alicanet',
                'MoMA': 'Museum of Modern Art',
                'IVAM': "INSTITUT VALENCIÀ D'ART MODERN",
                'MAG': 'Museo Arqueológico de Guardamar del Segura',
                'MARQ': 'MUSEO ARQUEOLÓGICO PROVINCIAL DE ALICANTE ',
                'MAF': 'MUSEU ALCOIÀ DE LA FESTA ',
                'MAGa': 'Museu Arqueològic de Gandia ',
                'MUSA': "MUSEU DE LA CIUTAT D'ALACANT",
                'MUA': "MUSEU DE LA UNIVERSITAT D'ALACANT",
                'MUMA': "MUSEU MUNICIPAL D'ALZIRA",
                'MUVIM': 'MUSEU VALENCIÀ DE LA IL·LUSTRACIÓ I DE LA MODERNITAT '

            }

        self.dict_acronimos = dict_acronimos
        self.nlp = spacy.load("es_core_news_sm")
        self.marker = "XCRTEDWSSSSD"  # Marcador para saltos de línea
        self.puntuacion = string.punctuation #ajustar los signos de puntuación por si está justo después del acrónimo


    def sustituir_acronimos(self, texto):
        # Reemplazar saltos de línea con un marcador para procesar el texto correctamente
        texto = texto.replace('\n\n', f' {self.marker} {self.marker} ')
        texto = texto.replace('\n', f' {self.marker} ')
        doc = self.nlp(texto)
        acronimos_expandidos = set()
        nuevas_oraciones = []
        for sent in doc.sents:
            oracion = sent.text.strip()
            palabras = oracion.split()
            oracion_modificada = []
            expansiones = []
            for palabra in palabras:
                # Limpiar la palabra de puntuación al final
                palabra_limpia = palabra.rstrip(self.puntuacion)
                if palabra_limpia in self.dict_acronimos and palabra_limpia not in acronimos_expandidos:
                    expansiones.append(f"{palabra_limpia} {self.dict_acronimos[palabra_limpia]}.")
                    acronimos_expandidos.add(palabra_limpia)
                oracion_modificada.append(palabra)
            if expansiones:
                nuevas_oraciones.append(' '.join(oracion_modificada))
                nuevas_oraciones.extend(expansiones)
            else:
                nuevas_oraciones.append(' '.join(oracion_modificada))
        resultado = ' '.join(nuevas_oraciones)
        # Revertir los marcadores a saltos de línea, manejar correctamente los dobles saltos de línea
        resultado = resultado.replace(f' {self.marker} {self.marker} ', '\n\n')
        resultado = resultado.replace(f' {self.marker} ', '\n')
        if resultado.endswith(self.marker):
            resultado = resultado[:-len(self.marker)].strip()

        # Asegurar que no queden marcadores en el texto
        resultado = resultado.replace(self.marker, '')

        return resultado

    def detectar_acronimos(self, texto):
        acronimos_detectadas = []
        acronimos_ordenadas = sorted(self.dict_acronimos.keys(), key=len, reverse=True)
        for acronimos in acronimos_ordenadas:
            inicio = 0
            while inicio < len(texto):
                inicio = texto.find(acronimos, inicio)
                if inicio == -1:
                    break
                fin = inicio + len(acronimos)
                if (inicio == 0 or not texto[inicio - 1].isalnum()) and (fin == len(texto) or not texto[fin].isalnum()):
                    acronimos_detectadas.append(acronimos)
                    inicio += len(acronimos)
                else:
                    inicio += len(acronimos)
        return acronimos_detectadas
