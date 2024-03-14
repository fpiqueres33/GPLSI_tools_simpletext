import re


class Superlativos:
    def __init__(self):
        self.superlative_pattern = r'\b\w+(?:ísimo|ísima|ísimos|ísimas|bérrimo|bérrima|bérrimos|bérrimas)\b'
        #self.superlative_pattern = r'\b\w+(?:ísimo|ísima|ísimos|ísimas|bérrimo|bérrima|bérrimos|bérrimas)(?=\W|\b)'

        self.superlatives = []
        #self.stemmer = SnowballStemmer("spanish")
        self.ending_map = {
            'ísimo': 'o',
            'bérrimo': 'o',
            'ísima': 'a',
            'bérrima': 'a',
            'ísimos': 'os',
            'bérrimos': 'os',
            'ísimas': 'as',
            'bérrimas': 'as',
        }
        self.special_cases = {
            'buen': 'bueno', 'mal': 'malo',
            'grando': 'grande', 'granda': 'grande', 'grandos': 'grandes', 'grandas': 'grandes',
            'friísimo': 'frío', 'friísimos':'fríos', 'friísima': 'fría', 'friísimas': 'frías',
            'sucísimo': 'sucio', 'sucísima': 'sucia','sucísimos': 'sucios', 'sucísimas': 'sucia',
            'lacísimo': 'lacio', 'lacísimos': 'lacios', 'lacísima': 'lacia', 'lacísimas': 'lacias',
            'vaciísimo': 'vacío', 'vaciísima': 'vacía', 'vaciísimos': 'vacíos', 'vaciísimas': 'vacías',
            'fortísimo': 'fuerte', 'fortísimos': 'fuertes', 'fortísima': 'fuerte', 'fortísimas': 'fuertes',
            'novísimo': 'nuevo', 'novísima': 'nueva','novísimos': 'nuevos','novísimas': 'nuevas',
            'sapientísimo': 'sabio', 'sapientísima': 'sabia', 'sapientísimos': 'sabios', 'sapientísimas': 'sabias',
            'recentísimo': 'reciente', 'recentísima': 'reciente', 'recentísimos': 'recientes','recentísimas': 'recientes',
            'fuertísimo': 'fuerte', 'fuertísima': 'fuerte', 'fuertísimos': 'fuertes', 'fuertísimas': 'fuertes',
            'Futbolísimos': 'Futbolísimos', 'Santísima': 'Santísima'
        }

    def detectar_superlativos(self, text):
        self.superlatives = re.findall(self.superlative_pattern, text, flags=re.IGNORECASE)
        return self.superlatives

    def get_base_adjective(self, superlative):
        # Convertir a minúsculas para manejar uniformemente, guardando el caso original
        original_case = superlative
        superlative = superlative.lower()

        # Comprueba si el superlativo está en casos especiales
        if superlative in self.special_cases:
            base = self.special_cases[superlative]
        elif superlative.endswith(('érrimo', 'érrimos', 'érrima', 'érrimas')):
            base = superlative.replace('érrim', 're')
        else:
            for end, replacement in self.ending_map.items():
                if superlative.endswith(end):
                    base = superlative[:-len(end)] + replacement
                    break
            else:
                # Si no se encuentra ninguna coincidencia, mantener la base original
                base = superlative

        # Ajustar finales especiales
        base = self.adjust_qu_endings(base)

        # Manejar el caso original
        if original_case.isupper():
            # Si el superlativo original estaba todo en mayúsculas
            return base.upper()
        elif original_case[0].isupper():
            # Si el superlativo original comenzaba con mayúscula
            return base.capitalize()
        else:
            # Superlativo en minúsculas
            return base

    def adjust_qu_endings(self, word):
        qu_endings = {
            'quos': 'cos', 'quas': 'cas',
            'quo': 'co', 'qua': 'ca',
            'zas': 'ces',
            'bilos': 'bles', 'bilas': 'bles',
            'bilo': 'ble', 'bila': 'ble',
            'alos': 'ales', 'alo': 'al',
            'elo': 'el', 'elos': 'eles',
            'ica': 'iz',
            'breos': 'bres',
            'breas': 'bres',
            'breo' : 'bre',
            'brea': 'bre',
            'guos': 'gos',
            'guo': 'go',
            'gua': 'ga',
            'guas': 'gas',
            'plo': 'ple', 'plos':'ples',
            'iento': 'iente', 'ientos': 'ientes', 'ienta': 'iente', 'ientas': 'ientes',
            'cilo': 'cil', 'cilos': 'ciles',
            'bro': 'bre', 'bros': 'bres', 'bra': 'bre', 'bras': 'bres',
            'anta': 'ante', 'antas': 'antes', 'antos': 'antes', 'anto': 'ante',
            'loca': 'loz', 'loco': 'loz', 'locas': 'loces', 'locos': 'loces',
            'egro': 'egre', 'egra': 'egre', 'egros': 'egres', 'egras': 'egres'
        }
        for end, replacement in qu_endings.items():
            if word.endswith(end):
                return word[:-len(end)] + replacement
        return word

    def find_superlative_lemmas(self, text):
        superlative_lemmas = []
        for word in self.superlatives:
            base_adjective = "muy "+self.get_base_adjective(word)
            superlative_lemmas.append((word, base_adjective))
        return superlative_lemmas

    def reemplazar_superlativos(self, text):
        superlatives_detected = self.detectar_superlativos(text)
        for superlative in superlatives_detected:
            print(superlative)
            print(superlative.isupper())
            base_adjective = self.get_base_adjective(superlative)
            print(base_adjective)
            # Comprueba si el superlativo está en mayúsculas
            if superlative.isupper():
                replacement = "MUY " + base_adjective.upper()
            # Comprueba si el superlativo comienza con una letra mayúscula
            elif superlative[0].isupper():
                replacement = "Muy " + base_adjective.lower()
            else:
                replacement = "muy " + base_adjective.lower()
            text = re.sub(re.escape(superlative), replacement, text)
        return text

