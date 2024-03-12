import re


class Complejos:
    def __init__(self):
        # La bandera 're.IGNORECASE' hace que la búsqueda no sea sensible a mayúsculas/minúsculas
        self.locuciones_complejas = {
            'a pesar de que': 'aunque',
            'en cuanto a': 'sobre',
            'por lo tanto': 'así que',
            'así como': 'y',
            'tan pronto como': 'cuando',
            'no obstante': 'pero',
            'por consiguiente': 'también',
            'sin embargo': 'además',
            'en consecuencia': 'por lo tanto'
        }

    def detectar_y_sustituir_conectores(self, texto):
        # print("Texto a procesar:", texto)  # Esto es solo para depuración
        if not isinstance(texto, str):
            raise ValueError("El texto proporcionado debe ser una cadena de caracteres.")

        def reemplazar_locucion(match):
            locucion_encontrada = match.group(0)
            # Verificamos si la primera letra es mayúscula
            if locucion_encontrada[0].isupper():
                # Si es mayúscula, capitalizamos la locución simple correspondiente
                locucion_simple = self.locuciones_complejas[locucion_encontrada.lower()].capitalize()
            else:
                locucion_simple = self.locuciones_complejas[locucion_encontrada.lower()]

            return locucion_simple

        # Creamos una expresión regular que detecta todas las locuciones complejas
        locuciones_pattern = re.compile(
            r'\b(' + '|'.join(re.escape(loc) for loc in self.locuciones_complejas.keys()) + r')\b',
            re.IGNORECASE
        )

        # Reemplazamos las locuciones complejas en el texto
        texto_transformado = locuciones_pattern.sub(reemplazar_locucion, texto)
        return texto_transformado

    def detectar_conectores_complejos(self, texto):
        # Creamos una lista para almacenar los complejos detectados
        complejos_detectados = []

        # Creamos una expresión regular que detecta todas las locuciones complejas
        locuciones_pattern = re.compile(
            r'\b(' + '|'.join(re.escape(loc) for loc in self.locuciones_complejas.keys()) + r')\b',
            re.IGNORECASE
        )

        # Buscamos todas las coincidencias en el texto
        for match in locuciones_pattern.finditer(texto):
            complejo = match.group(0)
            complejos_detectados.append(complejo)

        return complejos_detectados
