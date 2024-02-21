import re

import spacy


class Romanos:
    def __init__(self):
        self.nlp = spacy.load('es_core_news_sm')  # Cargando el modelo de spaCy para español
        # Expresión regular para detectar números romanos
        self.pattern = r'\bM{0,4}(CM|CD|D?C{0,3})?(XC|XL|L?X{0,3})?(IX|IV|V?I{0,3})\b'
        # Mapeo de números romanos a arábigos
        self.roman_arabic_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        self.ordinales = {
            1: 'primero', 2: 'segundo', 3: 'tercero', 4: 'cuarto', 5: 'quinto',
            6: 'sexto', 7: 'séptimo', 8: 'octavo', 9: 'noveno', 10: 'décimo',
            11: 'undécimo', 12: 'duodécimo', 13: 'decimotercero', 14: 'decimocuarto',
            15: 'decimoquinto', 16: 'decimosexto', 17: 'decimoséptimo', 18: 'decimoctavo',
            19: 'decimonoveno', 20: 'vigésimo'
        }

        # Método para convertir un número romano a arábigo

    def detectar_romanos(self, text):
        return [(match.group(), match.start(), match.end()) for match in re.finditer(self.pattern, text) if
                match.group()]

    def detectar_romanos_sin_loc(self, text):
        return [match.group() for match in re.finditer(self.pattern, text) if
                match.group()]

    def roman_to_arabic(self, roman_numeral):
        arabic_num = 0
        prev_value = 0
        for letter in reversed(roman_numeral):
            value = self.roman_arabic_map.get(letter, 0)
            arabic_num += value if value >= prev_value else -value
            prev_value = value
        return arabic_num

    def reemplazar_romanos(self, text):
        new_text = text
        for roman_numeral, start_pos, end_pos in reversed(self.detectar_romanos(text)):
            arabic_num = self.roman_to_arabic(roman_numeral)
            new_text = new_text[:start_pos] + str(arabic_num) + new_text[end_pos:]
        return new_text

    def reemplazar_ordinales_en_nombres(self, text):
        doc = self.nlp(text)
        new_text = text
        for ent in doc.ents:
            if ent.label_ == 'PER':
                print(ent)
                tokens = ent.text.split()
                if len(tokens) > 1 and tokens[-1].isdigit():  # Verificar si el último token es un número
                    num_arabigo = int(tokens[-1])
                    ordinal = self.ordinales.get(num_arabigo)
                    if ordinal:
                        # Construir el nuevo nombre con el ordinal
                        nuevo_nombre = " ".join(tokens[:-1]) + " " + ordinal
                        # Reemplazar en el texto
                        new_text = new_text.replace(ent.text, nuevo_nombre)
        return new_text


