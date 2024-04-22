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
            "cero": 0, "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
            "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10,
            "once": 11, "doce": 12, "trece": 13, "catorce": 14, "quince": 15,
            "dieciséis": 16, "diecisiete": 17, "dieciocho": 18, "diecinueve": 19,
            "veinte": 20, "veintiuno": 21, "veintidós": 22, "veintidos": 22, "veintitrés": 23, "veintitres": 23, "veinticuatro": 24,
            "veinticinco": 25, "veintiséis": 26, "veintiseis": 26, "veintisiete": 27, "veintiocho": 28, "veintinueve": 29,
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
            "quinientos": 500, "seiscientos": 600, "setecientos": 700, "ochocientos": 800, "novecientos": 900,
            "primero": 1, "primera": 1, "segundo": 2, "segunda": 2, "tercero": 3, "tercera": 3,
            "cuarto": 4, "cuarta": 4, "quinto": 5, "quinta": 5, "sexto": 6, "sexta": 6, "séptimo": 7, "séptima": 7,
            "octavo": 8, "octava": 8, "noveno": 9, "novena": 9,
            "décimo": 10, "décima": 10, "undécimo": 11, "undécima": 11,
            "duodécimo": 12, "duodécima": 12, "decimotercero": 13, "decimotercera": 13,
            "decimocuarto": 14, "decimocuarta": 14, "decimoquinto": 15, "decimoquinta": 15,
            "decimosexto": 16, "decimosexta": 16, "decimoséptimo": 17, "decimoséptima": 17,
            "decimoctavo": 18, "decimoctava": 18, "decimonoveno": 19, "decimonovena": 19,
            "vigésimo": 20, "vigésima": 20, "vigésimo primero": 21, "vigésima primera": 21,
            "vigésimo segundo": 22, "vigésima segunda": 22, "vigésimo tercero": 23, "vigésima tercera": 23,
            "vigésimo cuarto": 24, "vigésima cuarta": 24, "vigésimo quinto": 25, "vigésima quinta": 25,
            "vigésimo sexto": 26, "vigésima sexta": 26, "vigésimo séptimo": 27, "vigésima séptima": 27,
            "vigésimo octavo": 28, "vigésima octava": 28, "vigésimo noveno": 29, "vigésima novena": 29,
            "trigésimo": 30, "trigésima": 30

        }

        self.date_pattern = re.compile(r'(\d{2})[-/](\d{2})[-/](\d{2,4})')
        self.hour_pattern = re.compile(r'([01]?[0-9]|2[0-3]):([0-5][0-9])')
        self.phone_number_pattern = re.compile(r'\b\d{9}\b')
        self.number_pattern = re.compile(r'\b\d{1,3}(?:\.\d{3})*(?:,\d+)?\b|\b\d+(?:,\d+)?\b')
        self.percentage_pattern = re.compile(r'%')

        # Se crean marcas para los saltos de línea mediante las 2 funciones siguientes.
    def marcar_saltos_de_linea(self, text):
        return text.replace('\n', 'ZQRTESqwuio')

    def restaurar_saltos_de_linea(self, text):
        return text.replace('ZQRTESqwuio', '\n')


    def reemplazar_numeros(self, text):
        # transformamos los números escritos como primer paso del pipeline para las siguientes transformaciones
        texto_marcado = self.marcar_saltos_de_linea(text)
        text = self.transformar_numeros_escritos(texto_marcado)

        # ejecutamos pipeline de lectura simplificada
        sentences = sent_tokenize(text)
        transformed_sentences = []
        eliminar_siguiente_token = False  # Variable para controlar la eliminación del siguiente token
        palabras_a_eliminar = ["horas", "hora", "h", "Horas", "Hora", "h", "H", "h.",
                               "H."]  # Lista de palabras clave a eliminar

        for sentence in sentences:
            tokens = word_tokenize(sentence)
            transformed_words = []

            for i, word in enumerate(tokens):

                if eliminar_siguiente_token:
                    eliminar_siguiente_token = False
                    continue  # Omitir este token

                if self.date_pattern.fullmatch(word):
                    word = self.transform_dates(word)

                elif self.hour_pattern.fullmatch(word):
                    # word = self.transformar_horas(word)
                    hour, minutes = self.hour_pattern.fullmatch(word).groups()
                    if hour == "13" and i > 0 and tokens[i - 1].lower() == "las":
                        transformed_words[-1] = "la"
                    word = self.transformar_horas(word)
                    if i + 1 < len(tokens) and tokens[i + 1].lower() in palabras_a_eliminar:
                        eliminar_siguiente_token = True

                elif self.phone_number_pattern.fullmatch(word):
                    if self.check_phone_context(tokens, i):
                        word = self.transform_phone_number(word)
                elif '%' in word and i > 0 and self.number_pattern.fullmatch(tokens[i - 1]):
                    # Procesar primero los porcentajes
                    transformed_words[-1] = self.transform_percentage(tokens[i - 1])
                    continue  # Omitir añadir el símbolo de porcentaje
                elif self.number_pattern.fullmatch(word):
                    if not self.is_in_date_context(tokens, i):
                        word = self.transform_numbers(word)

                transformed_words.append(word)

            transformed_sentence = ' '.join(transformed_words)
            transformed_sentence = self.correct_spaces_around_punctuation(transformed_sentence)
            transformed_sentences.append(transformed_sentence)
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
    def transform_percentage(self, word):
        # Asumimos que 'word' es un número
        number = float(word.replace(',', '.'))
        rounded_number = round(number)
        if rounded_number % 10 == 0:
            return f"{rounded_number // 10} de cada 10"
        else:
            return f"{rounded_number} de cada 100"

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
            # Usar la representación especial si el número es un caso especial
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

            elif rounded_number_int >= millon:
                cantidad = rounded_number_int // millon
                unidad = "millón" if cantidad == 1 else "millones"

            elif rounded_number_int >= mil:
                cantidad = rounded_number_int // mil
                unidad = "mil"

            else:
                return f"{prefix}{num2words(rounded_number_int, lang='es')}"

            return f"{prefix}{cantidad} {unidad}"

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


