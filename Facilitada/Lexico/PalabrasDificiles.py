from Facilitada.Lexico.DiccionarioPalabrasDificiles import dict_palabras_dificiles, dict_10000
from Facilitada.Lexico.Desambiguar import Disambiguator
import re

class PalabrasDificiles:
    def __init__(self, diccionario=None):
        self.diccionario_dificiles = diccionario if diccionario else dict_palabras_dificiles
        self.diccionario_uso_frecuente = dict_10000
        self.disambiguator = Disambiguator()

    def detectar_palabras_dificiles(self, texto):

        palabras_dificiles = []
        palabras_dificiles_ordenadas = sorted(self.diccionario_dificiles.keys(), key=len, reverse=True)

        for palabra_dificil in palabras_dificiles_ordenadas:
            inicio = 0
            while inicio < len(texto):
                inicio = texto.lower().find(palabra_dificil.lower(), inicio)
                if inicio == -1:
                    break
                fin = inicio + len(palabra_dificil)
                if (inicio == 0 or not texto[inicio - 1].isalnum()) and (fin == len(texto) or not texto[fin].isalnum()):
                    palabras_dificiles.append(palabra_dificil.capitalize())
                    inicio += len(palabra_dificil)
                else:
                    inicio += len(palabra_dificil)

        palabras_ordenadas_uso_frecuente = [palabra for palabra, datos in self.diccionario_uso_frecuente.items()
                                            if eval(datos)[0] <= 1750]
        for palabra_comun in palabras_ordenadas_uso_frecuente:
            inicio = 0
            while inicio < len(texto):
                inicio = texto.lower().find(palabra_comun.lower(), inicio)
                if inicio == -1:
                    break
                fin = inicio + len(palabra_comun)
                if (inicio == 0 or not texto[inicio - 1].isalnum()) and (fin == len(texto) or not texto[fin].isalnum()):
                    if palabra_comun.capitalize() not in palabras_dificiles:
                        sinonimos = self.disambiguator.disambiguate(palabra_comun, texto)
                        palabras_dificiles.append(f"{palabra_comun.capitalize()} (sinónimos: {', '.join(sinonimos['Palabras de contexto'])})")
                    inicio += len(palabra_comun)
                else:
                    inicio += len(palabra_comun)
        return palabras_dificiles

    def glosario_palabras_dificiles(self, texto):
        texto_tokens = re.findall(r'\b\w+\b', texto.lower())
        glosario_list = []

        palabras_dificiles_ordenadas = sorted(self.diccionario_dificiles.keys(), key=len, reverse=True)
        for palabra_dificil in palabras_dificiles_ordenadas:
            palabra_dificil_lower = palabra_dificil.lower()
            for token in texto_tokens:
                if palabra_dificil_lower == token:
                    entrada_glosario = f"{palabra_dificil.capitalize()}: {self.diccionario_dificiles[palabra_dificil]}"
                    if entrada_glosario not in glosario_list:
                        glosario_list.append(entrada_glosario)

        palabras_ordenadas_uso_frecuente = [palabra for palabra, datos in self.diccionario_uso_frecuente.items()
                                            if eval(datos)[0] <= 1750]
        for palabra_comun in palabras_ordenadas_uso_frecuente:
            palabra_comun_lower = palabra_comun.lower()
            for token in texto_tokens:
                if palabra_comun_lower == token:
                    sinonimos = self.disambiguator.disambiguate(palabra_comun, texto)
                    entrada_glosario = f"{palabra_comun.capitalize()}: sinónimos: {', '.join(sinonimos['Palabras de contexto'])}"
                    if entrada_glosario not in glosario_list:
                        glosario_list.append(entrada_glosario)

        return glosario_list
