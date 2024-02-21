class Abreviaturas:
    def __init__(self, diccionario = None):
        if diccionario == None:
            diccionario = {
                "(a)": "alias",
                "a D. g.": "a Dios gracias",
                "C.C.": "Centro Comercial",
                "C/": "Calle",
                "c/": "calle",
                "avda.": "avenida",
                "Avda.": "Avenida",
                "a. C.": "antes de Cristo",
                "A. D.": "anno Domini (lat.: 'en el año del Señor')",
                "a. de J. C.": "antes de Jesucristo",
                "a. e. c.": "antes de la era común",
                "a. i.": "ad interim (lat.: 'de manera provisional o interina')",
                "A. I.": "alteza imperial",
                "a. J. C.": "antes de Jesucristo",
                "a. m.": "ante meridiem (lat.: 'antes del mediodía')"
            }

        self.diccionario = diccionario

    def sustituir_abreviaturas(self, texto):
        # Ordenar las abreviaturas por longitud en orden descendente para manejar primero las más largas
        abreviaturas_ordenadas = sorted(self.diccionario.keys(), key=len, reverse=True)
        for abreviatura in abreviaturas_ordenadas:
            # Buscar todas las ocurrencias de la abreviatura en el texto
            inicio = 0
            while inicio < len(texto):
                inicio = texto.find(abreviatura, inicio)
                if inicio == -1:
                    break
                # Verificar si la abreviatura está adecuadamente delimitada
                fin = inicio + len(abreviatura)
                if (inicio == 0 or not texto[inicio-1].isalnum()) and (fin == len(texto) or not texto[fin].isalnum()):
                    texto = texto[:inicio] + self.diccionario[abreviatura] + texto[fin:]
                    inicio += len(self.diccionario[abreviatura])
                else:
                    inicio += len(abreviatura)
        return texto

    def detectar_abreviaturas(self, texto):
        abreviaturas_detectadas = []
        abreviaturas_ordenadas = sorted(self.diccionario.keys(), key=len, reverse=True)
        for abreviatura in abreviaturas_ordenadas:
            inicio = 0
            while inicio < len(texto):
                inicio = texto.find(abreviatura, inicio)
                if inicio == -1:
                    break
                fin = inicio + len(abreviatura)
                if (inicio == 0 or not texto[inicio - 1].isalnum()) and (fin == len(texto) or not texto[fin].isalnum()):
                    abreviaturas_detectadas.append(abreviatura)
                    inicio += len(abreviatura)
                else:
                    inicio += len(abreviatura)
        return abreviaturas_detectadas

"""
# Ejemplo de uso
diccionario = {
    "(a)": "alias",
    "a D. g.": "a Dios gracias",
    "C.C.": "Centro Comercial",
    "C/": "Calle",
    "c/": "calle",
    "avda.": "avenida",
    "Avda.": "Avenida",
    "a. C.": "antes de Cristo",
    "A. D.": "anno Domini (lat.: 'en el año del Señor')",
    "a. de J. C.": "antes de Jesucristo",
    "a. e. c.": "antes de la era común",
    "a. i.": "ad interim (lat.: 'de manera provisional o interina')",
    "A. I.": "alteza imperial",
    "a. J. C.": "antes de Jesucristo",
    "a. m.": "ante meridiem (lat.: 'antes del mediodía')"
}


texto_ejemplo = "A. D. y a. m. son abreviaturas comunes. El C.C. se ubica en la c/ Pascual Pérez"
abreviaturas = Abreviaturas(diccionario)
texto_modificado = abreviaturas.sustituir_abreviaturas(texto_ejemplo)
print(texto_modificado)
abreviaturas_detectadas = abreviaturas.detectar_abreviaturas(texto_ejemplo)
print("Abreviaturas detectadas:", abreviaturas_detectadas)
"""