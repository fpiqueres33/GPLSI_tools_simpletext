import re
import spacy
import roman

class Romanos2:
    def __init__(self):
        self.nlp = spacy.load('es_core_news_sm')
        # Ajustamos la expresión regular para detectar posibles números romanos
        self.pattern = r'\bM{0,4}(CM|CD|D?C{0,3})?(XC|XL|L?X{0,3})?(IX|IV|V?I{0,3})\b'
        self.ordinales = {
            1: 'primero', 2: 'segundo', 3: 'tercero', 4: 'cuarto', 5: 'quinto',
            6: 'sexto', 7: 'séptimo', 8: 'octavo', 9: 'noveno', 10: 'décimo',
            11: 'undécimo', 12: 'duodécimo', 13: 'decimotercero', 14: 'decimocuarto',
            15: 'decimoquinto', 16: 'decimosexto', 17: 'decimoséptimo', 18: 'decimoctavo',
            19: 'decimonoveno', 20: 'vigésimo'
        }

    def detectar_romanos(self, text):
        # Divide el texto en tokens basados en espacios y puntuación para una mejor detección
        tokens = text.split()
        matches = []
        for token in tokens:
            # Elimina puntuación al final del token para mejorar la detección
            token_sin_puntuacion = re.sub(r'[.,;:!?"\'()]$', '', token)
            if re.fullmatch(self.pattern, token_sin_puntuacion):
                try:
                    # Valida el número romano con la librería roman
                    roman.fromRoman(token_sin_puntuacion.upper())
                    # Si la validación es exitosa, añade el token original al listado de coincidencias
                    matches.append(token)
                except roman.InvalidRomanNumeralError:
                    continue
        return matches

    def roman_to_arabic(self, roman_numeral):
        try:
            return roman.fromRoman(roman_numeral.upper())
        except roman.InvalidRomanNumeralError:
            return None

    def reemplazar_romanos(self, text):
        # Define una expresión regular que incluya números romanos y opcionalmente puntuación
        pattern_with_punctuation = r'(\bM{0,4}(CM|CD|D?C{0,3})?(XC|XL|L?X{0,3})?(IX|IV|V?I{0,3})\b)([.,;:!?"\'()]?)'

        def replace_roman_with_arabic(match):
            roman_numeral = match.group(1)
            punctuation = match.group(5)
            if roman_numeral:  # Verifica que el numeral romano no esté vacío
                arabic_numeral = str(roman.fromRoman(roman_numeral.upper()))
                return arabic_numeral + punctuation
            return match.group(0)  # Devuelve el texto original si el numeral romano está vacío

        # Usa la expresión regular para reemplazar números romanos conservando la puntuación
        new_text = re.sub(pattern_with_punctuation, replace_roman_with_arabic, text)
        return new_text


    def reemplazar_ordinales_en_nombres(self, text):
        doc = self.nlp(text)
        new_text = text
        for ent in doc.ents:
            if ent.label_ == 'PER':
                tokens = ent.text.split()
                if len(tokens) > 1 and tokens[-1].isdigit():
                    num_arabigo = int(tokens[-1])
                    ordinal = self.ordinales.get(num_arabigo)
                    if ordinal:
                        nuevo_nombre = " ".join(tokens[:-1]) + " " + ordinal
                        new_text = new_text.replace(ent.text, nuevo_nombre)
        return new_text