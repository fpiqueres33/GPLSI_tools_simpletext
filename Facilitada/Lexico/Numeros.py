import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from num2words import num2words


nltk.download('punkt')  # CARGAR LA PRIMERA VEZ QUE SE EJECUTA


class Numero:
    def __init__(self):
        self.months = {
            '01': 'enero', '02': 'febrero', '03': 'marzo',
            '04': 'abril', '05': 'mayo', '06': 'junio',
            '07': 'julio', '08': 'agosto', '09': 'septiembre',
            '10': 'octubre', '11': 'noviembre', '12': 'diciembre'
        }
        self.casos_especiales = {
            100: "cien",
            200: "200", 300: '300', 400: '400', 500: '500', 600: '600', 700: '700', 800: '800', 900: '900',
            1000: 'mil'
        }
        self.numeros_escritos = {
            #Se omiten los ordinales hasta el 10
            "cero": 0, "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
            "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10,
            "once": 11, "doce": 12, "trece": 13, "catorce": 14, "quince": 15,
            "dieciséis": 16, "diecisiete": 17, "dieciocho": 18, "diecinueve": 19,
            "veinte": 20, "veintiuno": 21, "veintidós": 22, "veintidos": 22, "veintitrés": 23, "veintitres": 23,
            "veinticuatro": 24,
            "veinticinco": 25, "veintiséis": 26, "veintiseis": 26, "veintisiete": 27, "veintiocho": 28,
            "veintinueve": 29,
            "treinta": 30, "treinta y uno": 31, "treinta y dos": 32, "treinta y tres": 33, "treinta y cuatro": 34,
            "treinta y cinco": 35, "treinta y seis": 36, "treinta y siete": 37, "treinta y ocho": 38,
            "treinta y nueve": 39,
            "cuarenta": 40, "cuarenta y uno": 41, "cuarenta y dos": 42, "cuarenta y tres": 43, "cuarenta y cuatro": 44,
            "cuarenta y cinco": 45, "cuarenta y seis": 46, "cuarenta y siete": 47, "cuarenta y ocho": 48,
            "cuarenta y nueve": 49,
            "cincuenta": 50, "cincuenta y uno": 51, "cincuenta y dos": 52, "cincuenta y tres": 53,
            "cincuenta y cuatro": 54,
            "cincuenta y cinco": 55, "cincuenta y seis": 56, "cincuenta y siete": 57, "cincuenta y ocho": 58,
            "cincuenta y nueve": 59,
            "sesenta": 60, "sesenta y uno": 61, "sesenta y dos": 62, "sesenta y tres": 63, "sesenta y cuatro": 64,
            "sesenta y cinco": 65, "sesenta y seis": 66, "sesenta y siete": 67, "sesenta y ocho": 68,
            "sesenta y nueve": 69,
            "setenta": 70, "setenta y uno": 71, "setenta y dos": 72, "setenta y tres": 73, "setenta y cuatro": 74,
            "setenta y cinco": 75, "setenta y seis": 76, "setenta y siete": 77, "setenta y ocho": 78,
            "setenta y nueve": 79,
            "ochenta": 80, "ochenta y uno": 81, "ochenta y dos": 82, "ochenta y tres": 83, "ochenta y cuatro": 84,
            "ochenta y cinco": 85, "ochenta y seis": 86, "ochenta y siete": 87, "ochenta y ocho": 88,
            "ochenta y nueve": 89,
            "noventa": 90, "noventa y uno": 91, "noventa y dos": 92, "noventa y tres": 93, "noventa y cuatro": 94,
            "noventa y cinco": 95, "noventa y seis": 96, "noventa y siete": 97, "noventa y ocho": 98,
            "noventa y nueve": 99,
            "cien": 100, "ciento": 100, "doscientos": 200, "trescientos": 300, "cuatrocientos": 400,
            "quinientos": 500, "seiscientos": 600, "600": 700, "700": 800, "800": 900,
            # Se omiten ordinales hasta el 10
            # "primero": 1, "primera": 1, "primer": 1, "segundo": 2, "segunda": 2, "según": 2,
            # "tercer": 3, "tercero": 3,
            # "tercera": 3,
            # "primeros": 1, "primeras": 1, "segundos": 2, "segundas": 2,
            # "terceros": 3, "terceras": 3,
            # "cuarto": 4, "cuarta": 4, "quinto": 5, "quinta": 5,
            # "sexto": 6, "sexta": 6, "sextos": 6, "sextas": 6,
            # "séptimo": 7, "séptima": 7, "séptimos": 7, "séptimas": 7,
            # "octavo": 8, "octava": 8, "noveno": 9, "novena": 9,
            # "octavos": 8, "octavas": 8, "novenos": 9, "novenas": 9,
            # "décimo": 10, "décima": 10, "décimos": 10, "décimas": 10,
            "undécimo": 11, "undécima": 11, "undécimos": 11, "undécimas": 11,
            "duodécimo": 12, "duodécima": 12, "decimotercero": 13, "decimotercera": 13, "duodécimos": 12,
            "duodécimas": 12, "decimoterceros": 13, "decimoterceras": 13,
            "decimocuarto": 14, "decimocuarta": 14, "decimoquinto": 15, "decimoquinta": 15,
            "decimocuartos": 14, "decimocuartas": 14, "decimoquintos": 15, "decimoquintas": 15,
            "decimosexto": 16, "decimosexta": 16, "decimoséptimo": 17, "decimoséptima": 17,
            "decimosextos": 16, "decimosextas": 16, "decimoséptimos": 17, "decimoséptimas": 17,
            "decimoctavo": 18, "decimoctava": 18, "decimonoveno": 19, "decimonovena": 19,
            "decimoctavos": 18, "decimoctavas": 18, "decimonovenos": 19, "decimonovenas": 19,
            "décimo_primero": 11, "décimo_primera": 11, "décimo_primeros": 11, "décimo_primeras": 11,
            "décimo_segundo": 12, "décimo_segunda": 12, "décimo_segundos": 12, "décimo_segundas": 12,
            "décimo_tercero": 13, "décimo_tercera": 13, "décimo_terceros": 13, "décimo_terceras": 13,
            "décimo_cuarto": 14, "décimo_cuarta": 14, "décimo_cuartos": 14, "décimo_cuartas": 14,
            "décimo_quinto": 15, "décimo_quinta": 15, "décimo_quintos": 15, "décimo_quintas": 15,
            "décimo_sexto": 16, "décimo_sexta": 16, "décimo_sextos": 16, "décimo_sextas": 16,
            "décimo_séptimo": 17, "décimo_séptima": 17, "décimo_séptimos": 17, "décimo_séptimas": 17,
            "décimo_octavo": 18, "décimo_octava": 18, "décimo_octavos": 18, "décimo_octavas": 18,
            "décimo_noveno": 19, "décimo_novena": 19, "décimo_novenos": 19, "décimo_novenas": 19,
            "vigésimo": 20, "vigésima": 20, "vigésimo_primero": 21, "vigésimo_primera": 21,
            "vigésimos": 20, "vigésimas": 20, "vigésimo_primeros": 21, "vigésimo_primeras": 21,
            "vigésimo_segundo": 22, "vigésimo_segunda": 22, "vigésimo_tercero": 23, "vigésima_tercera": 23,
            "vigésimo_segundos": 22, "vigésimo_segundas": 22, "vigésimo_terceros": 23, "vigésimo_terceras": 23,
            "vigésimo_cuarto": 24, "vigésimo_cuarta": 24, "vigésimo_quinto": 25, "vigésimo_quinta": 25,
            "vigésimo_cuartos": 24, "vigésimo_cuartas": 24, "vigésimo_quintos": 25, "vigésimo_quintas": 25,
            "vigésimo_sexto": 26, "vigésimo_sexta": 26, "vigésimo_séptimo": 27, "vigésimo_séptima": 27,
            "vigésimo_sextos": 26, "vigésimo_sextas": 26, "vigésimo_séptimos": 27, "vigésimo_séptimas": 27,
            "vigésimo_octavo": 28, "vigésimo_octava": 28, "vigésimo_noveno": 29, "vigésimo_novena": 29,
            "vigésimo_octavos": 28, "vigésimo_octavas": 28, "vigésimo_novenos": 29, "vigésimo_novenas": 29,
            "trigésimo": 30, "trigésima": 30, "trigésimos": 30, "trigésimas": 30

        }

        self.date_pattern = re.compile(
            r'(\d{2})[-/.](\d{2})[-/.](\d{2,4})')  #Se establece el patrón de separación con - / .
        self.hour_pattern = re.compile(r'([01]?[0-9]|2[0-3]):([0-5][0-9])')
        self.phone_number_pattern = re.compile(r'\b\d{9}\b')
        self.number_pattern = re.compile(r'\b\d{1,3}(?:\.\d{3})*(?:,\d+)?\b|\b\d+(?:,\d+)?\b')
        #self.percentage_pattern = re.compile(r'%')
        self.percentage_pattern = re.compile(r'\b(el\s+)?(\d{1,3}(?:,\d+)?%)', re.IGNORECASE)

    # Se crean marcas para los saltos de línea mediante las 2 funciones siguientes.

    def marcar_saltos_de_linea(self, text):
        return text.replace('\n', 'ZQRTESqwuio')

    def restaurar_saltos_de_linea(self, text):
        return text.replace('ZQRTESqwuio', '\n')

    #Preproceso inicial para las palabras de diccionario con dos o mas tokens
    def sustituir_ordinales_compuestos(self, text):
        # Diccionario de ordinales compuestos a sus valores numéricos consolidados
        ordinales_compuestos = {
            'décimo primero': 'décimo_primero', 'décimo primer': 'décimo_primer',
            'décima primera': 'décima_primera',
            'décimo primeros': 'décimo_primeros',
            'décima primeras': 'décima_primeras',
            'décimo segundo': 'décimo_segundo', 'décimo segun': 'décimo_segun',
            'décima segunda': 'décima_segunda',
            'décimo segundos': 'décimo_segundos',
            'décimo segundas': 'décimo_segundas',
            'décimo tercero': 'décimo_tercero', 'décimo tercer': 'décimo_tercer',
            'décima tercera': 'décima_tercera',
            'décimo terceros': 'décimo_terceros',
            'décimo terceras': 'décimo_terceras',
            'décimo cuarto': 'décimo_cuarto',
            'décima cuarta': 'décima_cuarta',
            'décimo cuartos': 'décimo_cuartos',
            'décimo cuartas': 'décimo_cuartas',
            'décimo quinto': 'décimo_quinto',
            'décima quinta': 'décima_quinta',
            'décimo quintos': 'décimo_quintos',
            'décimo quintas': 'décimo_quintas',
            'décimo sexto': 'décimo_sexto',
            'décima sexta': 'décima_sexta',
            'décimo sextos': 'décimo_sextos',
            'décimo sextas': 'décimo_sextas',
            'décimo séptimo': 'décimo_séptimo',
            'décima séptima': 'décima_séptima',
            'décimo séptimos': 'décimo_séptimos',
            'décimo séptimas': 'décimo_séptimas',
            'décimo octavo': 'décimo_octavo',
            'décima octava': 'décima_octava',
            'décimo octavos': 'décimo_octavos',
            'décimo octavas': 'décimo_octavas',
            'décimo noveno': 'décimo_noveno',
            'décimo novena': 'décimo_novena',
            'décimo novenos': 'décimo_novenos',
            'décimo novenas': 'décimo_novenas',
            'vigésimo primero': 'vigésimo_primero', 'vigésimo primer': 'vigésimo_primer',
            'vigésima primera': 'vigésima_primera',
            'vigésimos primeros': 'vigésimos_primeros',
            'vigésimas primeras': 'vigésimas_primeras',
            'vigésimo segundo': 'vigésimo_segundo', 'vigésimo segun': 'vigésimo_segun',
            'vigésima segunda': 'vigésima_segunda',
            'vigésimos segundos': 'vigésimos_segundos',
            'vigésimas segundas': 'vigésimas_segundas',
            'vigésimo tercero': 'vigésimo_tercero', 'vigésimo tercer': 'vigésimo_tercer',
            'vigésima tercera': 'vigésima_tercera',
            'vigésimos terceros': 'vigésimos_terceros',
            'vigésimas terceras': 'vigésimas_terceras',
            'vigésimo cuarto': 'vigésimo_cuarto',
            'vigésima cuarta': 'vigésima_cuarta',
            'vigésimos cuartos': 'vigésimos_cuartos',
            'vigésimas cuartas': 'vigésimas_cuartas',
            'vigésimo quinto': 'vigésimo_quinto',
            'vigésima quinta': 'vigésima_quinta',
            'vigésimos quintos': 'vigésimos_quintos',
            'vigésimas quintas': 'vigésimas_quintas',
            'vigésimo sexto': 'vigésimo_sexto',
            'vigésima sexta': 'vigésima_sexta',
            'vigésimos sextos': 'vigésimos_sextos',
            'vigésimas sextas': 'vigésimas_sextas',
            'vigésimo séptimo': 'vigésimo_séptimo',
            'vigésima séptima': 'vigésima_séptima',
            'vigésimos séptimos': 'vigésimos_séptimos',
            'vigésimas séptimas': 'vigésimas_séptimas',
            'vigésimo octavo': 'vigésimo_octavo',
            'vigésima octava': 'vigésima_octava',
            'vigésimos octavos': 'vigésimos_octavos',
            'vigésimas octavas': 'vigésimas_octavas',
            'vigésimo noveno': 'vigésimo_noveno',
            'vigésima novena': 'vigésima_novena',
            'vigésimos novenos': 'vigésimos_novenos',
            'vigésimas novenas': 'vigésimas_novenas'
        }

        # Consolidar ordinales compuestos en un solo token

        for ordinal, consolidado in ordinales_compuestos.items():
            text = re.sub(r'\b' + re.escape(ordinal) + r'\b', consolidado, text, flags=re.IGNORECASE)

        return text


    def reemplazar_numeros(self, text):
        # Transformación inicial de ordinales compuestos y marcado de saltos de línea
        text = self.sustituir_ordinales_compuestos(text)
        text = self.marcar_saltos_de_linea(text)
        text = self.transformar_numeros_escritos(text)

        # Aplicar transformaciones de porcentajes
        matches = list(self.percentage_pattern.finditer(text))
        for match in reversed(matches):
            text = self.transform_percentage(text, match)

        # Procesamiento adicional si es necesario
        sentences = sent_tokenize(text)
        transformed_sentences = []
        for sentence in sentences:
            tokens = word_tokenize(sentence)
            transformed_words = []

            for i, word in enumerate(tokens):
                # Procesar fechas, horas, números de teléfono y otros números según sea necesario
                if self.date_pattern.fullmatch(word):
                    word = self.transform_dates(word)
                elif self.hour_pattern.fullmatch(word):
                    hour, minutes = self.hour_pattern.fullmatch(word).groups()
                    if hour == "13" and i > 0 and tokens[i - 1].lower() == "las":
                        transformed_words[-1] = "la"
                    word = self.transformar_horas(word)
                elif self.phone_number_pattern.fullmatch(word):
                    if self.check_phone_context(tokens, i):
                        word = self.transform_phone_number(word)
                elif self.number_pattern.fullmatch(word):
                    if not self.is_in_date_context(tokens, i):
                        word = self.transform_numbers(word)
                transformed_words.append(word)

            transformed_sentence = ' '.join(transformed_words)
            transformed_sentence = self.correct_spaces_around_punctuation(transformed_sentence)
            transformed_sentences.append(transformed_sentence)

        # Restaurar saltos de línea y retornar el texto final
        texto_final = self.restaurar_saltos_de_linea(' '.join(transformed_sentences))
        return texto_final

    def correct_spaces_around_punctuation(self, text):
        # Reemplazar espacios incorrectos alrededor de la puntuación
        corrected_text = re.sub(r'\s([?.!",](?:\s|$))', r'\1', text)
        return corrected_text

    def transform_dates(self, word):
        match = self.date_pattern.fullmatch(word)
        day, month, year = match.groups()
        if len(year) == 2:
            year = "20" + year

        month_name = self.months.get(month, "mes desconocido")
        return f"{day} de {month_name} de {year}"

    def transformar_horas(self, word):
        match = self.hour_pattern.fullmatch(word)
        hours, minutes = match.groups()
        hours_int = int(hours)
        minutes_int = int(minutes)
        periodo = "de la noche"
        minutes_str = f"{minutes_int} minutos"  # Valor por defecto para los minutos

        # Asignar el período del día
        if hours_int < 6:
            periodo = "de la madrugada"
        elif hours_int < 13:
            periodo = "de la mañana"
        elif hours_int < 20:
            periodo = "de la tarde"

        # Convertir la hora al formato de 12 horas si es necesario
        if hours_int > 12:
            hours_int -= 12

        # Reglas especiales para "la una" y "las"
        hora_str = "la" if hours_int == 1 else "las"
        hora_conjuncion = "horas y "

        # Reglas especiales para los minutos
        if minutes_int == 15:
            minutes_str = "cuarto"
            hora_conjuncion = "y "
        elif minutes_int == 30:
            minutes_str = "media"
            hora_conjuncion = "y "
        elif minutes_int == 45:
            hours_int = (hours_int % 12) + 1  # Aumentar una hora si son las "menos cuarto"
            minutes_str = "menos cuarto"
            hora_conjuncion = ""
        elif minutes_int == 0:
            minutes_str = "en punto"
            hora_conjuncion = ""

        # Devolver la cadena de texto transformada con la hora y el período correspondiente
        # hora_conjuncion = "" if minutes_int == 0 else "horas y "

        return f"{hours_int} {hora_conjuncion}{minutes_str} {periodo}"




    def check_phone_context(self, tokens, index):
        prev_context = tokens[max(index - 2, 0):index]
        next_context = tokens[index + 1:min(index + 3, len(tokens))]
        telefonos = ['móvil', 'teléfono', 'Teléfono', 'Móvil']
        return any(keyword in prev_context + next_context for keyword in telefonos)

    def transform_phone_number(self, word):
        # Formatear el número de teléfono al formato XXX XX XX XX
        return f"{word[0:3]} {word[3:5]} {word[5:7]} {word[7:9]}"

    # Método para la conversión de porcentajes
    def transform_percentage(self, text, match):
        # Extraer el grupo completo y el porcentaje del match
        full_text, el_prefix, percentage = match.group(0), match.group(1), match.group(2)
        number = float(percentage.replace('%', '').replace(',', '.'))
        rounded_number = round(number)

        # Caso especial para 50%
        if rounded_number == 50:
            result = "la mitad"
        elif rounded_number % 10 == 0:
            result = f"{rounded_number // 10} de cada 10"
        else:
            result = f"{rounded_number} de cada 100"

        # Reemplazar en el texto según el match, eliminando "el " si está presente
        start, end = match.span(0)
        return text[:start] + result + text[end:]

    # Métodos para el tratamiento del número entero y números con decimales.
    def _clean_and_convert_number(self, word):
        clean_number = word.replace('.', '').replace(',', '.')
        number = float(clean_number) if '.' in clean_number else int(clean_number)
        # print(f"Cleaned number: {number}")  # Debug print
        return number

    def _custom_round(self, number):
        # Definir umbrales
        billon = 1_000_000_000
        millon = 1_000_000
        mil = 1000

        # Aplicar redondeo basado en el tamaño del número
        if number < 100:
            rounded = round(number)
        elif 100 <= number < 1000:
            rounded = round(number, -2)
        elif number < mil:
            rounded = round(number)
        elif number < millon:
            rounded = round(number / mil) * mil
        elif number < billon:
            rounded = round(number / millon) * millon
        else:
            rounded = round(number / billon) * billon

        # Determinar si el redondeo fue hacia arriba o hacia abajo
        if rounded < number:
            prefix = "más de "
        elif rounded > number:
            prefix = "casi "
        else:
            prefix = ""

        return rounded, prefix

    def is_in_date_context(self, tokens, index):
        # Comprobar si uno de los dos tokens anteriores es un mes
        if index > 1 and (
                tokens[index - 2].lower() in self.months.values() or tokens[index - 1].lower() in self.months.values()):
            return True
        return False

    def transform_numbers(self, word):
        number = self._clean_and_convert_number(word)
        # Aplicamos casos especiales para los números indicados en el algoritmo de __init__
        if number in self.casos_especiales:
            return self.casos_especiales[number]

            # Si el número es menor que 100 y es un entero, lo devolvemos tal cual.
        if number < 100:
            number = int(round(number, 0))
            return str(number)  # Convertimos el número a entero y luego a cadena
        else:
            # Para números con decimales o mayores o iguales a 100, aplicamos redondeo.
            rounded_number, prefix = self._custom_round(number)
            rounded_number_int = int(rounded_number)

            # Definir umbrales
            billon = 1_000_000_000
            millon = 1_000_000
            mil = 1000

            # Manejar números cercanos a billones, millones o mil
            if rounded_number_int >= billon:
                cantidad = rounded_number_int // billon
                unidad = "billón" if cantidad == 1 else "billones"
                return f"{prefix}{cantidad} {unidad}"
            elif rounded_number_int >= millon:
                cantidad = rounded_number_int // millon
                unidad = "millón" if cantidad == 1 else "millones"
                return f"{prefix}{cantidad} {unidad}"
            elif rounded_number_int >= mil:
                cantidad = rounded_number_int // mil
                unidad = "mil"
                return f"{prefix}{cantidad} {unidad}"
            elif 100 <= number < 1000:
                # Para los números entre 100 y 1000, usar números directamente
                return f"{prefix}{rounded_number_int}"

            return f"{prefix}{num2words(rounded_number_int, lang='es')}"

        # Diccionario con las detecciones:

    def transformar_numeros_escritos(self, texto):
        palabras = texto.split()
        texto_transformado = []
        i = 0

        while i < len(palabras):
            palabra = palabras[i].lower()
            numero = self.numeros_escritos.get(palabra)

            # Manejar números compuestos con cientos
            if numero is not None and numero >= 100 and i + 1 < len(palabras):
                total_compuesto = numero
                j = i + 1
                while j < len(palabras) and self.numeros_escritos.get(palabras[j].lower(), 0) < 100:
                    if palabras[j] in [',', '.']:  # Tratar la puntuación como separador
                        break

                    siguiente_numero = self.numeros_escritos.get(palabras[j].lower())
                    if siguiente_numero is not None:
                        total_compuesto += siguiente_numero
                        j += 1
                        if j < len(palabras) and palabras[j].lower() == "y":
                            j += 1  # Saltar "y"
                    else:
                        break
                numero = total_compuesto
                i = j - 1
            elif palabra in ["treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta",
                             "noventa"] and i + 2 < len(palabras) and palabras[i + 1].lower() == "y":
                numero_compuesto = self.numeros_escritos.get(palabra + " y " + palabras[i + 2].lower())
                if numero_compuesto is not None:
                    numero = numero_compuesto
                    i += 2  # Saltar los siguientes dos tokens

            if numero is not None:
                texto_transformado.append(str(numero))
            else:
                texto_transformado.append(palabras[i])

            i += 1

        return ' '.join(texto_transformado)

    def detectar_numeros(self, text):
        sentences = sent_tokenize(text)
        detected_elements = {
            'fechas': [],
            'horas': [],
            'números de teléfono': [],
            'porcentajes': [],
            'otros números': [],
            'números escritos': []  # Nueva categoría para números escritos como texto
        }

        for sentence in sentences:
            tokens = word_tokenize(sentence)

            for i, word in enumerate(tokens):
                if self.date_pattern.fullmatch(word):
                    detected_elements['fechas'].append(word)

                elif self.hour_pattern.fullmatch(word):
                    detected_elements['horas'].append(word)

                elif self.phone_number_pattern.fullmatch(word):
                    if self.check_phone_context(tokens, i):
                        detected_elements['números de teléfono'].append(word)

                elif '%' in word and i > 0 and self.number_pattern.fullmatch(tokens[i - 1]):
                    detected_elements['porcentajes'].append(tokens[i - 1] + '%')

                elif self.number_pattern.fullmatch(word):
                    # if not self.is_in_date_context(tokens, i): # Ver si queremos detección
                    detected_elements['otros números'].append(word)

                # Agregar lógica para detectar números escritos como texto
                elif word.lower() in self.numeros_escritos:
                    numero_escrito = self.numeros_escritos[word.lower()]
                    detected_elements['números escritos'].append(f"{word} ({numero_escrito})")

        return detected_elements


