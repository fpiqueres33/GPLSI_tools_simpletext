
from Facilitada.Lexico.DiccionarioPalabrasDificiles import dict_palabras_dificiles
import re

class PalabrasDificiles:
    """
    Clase para detectar y manejar palabras difíciles de un texto.

    Permite la utilización de un diccionario personalizado de palabras difíciles,
    pero utiliza un diccionario predeterminado si no se proporciona ninguno.
    """

    def __init__(self, diccionario=None):
        """
        Inicializa la instancia con un diccionario de palabras difíciles.

        :param diccionario: Un diccionario personalizado de palabras difíciles.
                            Si es None, se utilizará el diccionario predeterminado.
        """
        if diccionario is None:
            self.diccionario = dict_palabras_dificiles
        else:
            self.diccionario = diccionario


    def detectar_palabras_dificiles(self, texto):
        # Detecta palabras dificiles en el texto y los devuelve capitalizados si se encuentran
        palabras_dificles = []
        palabras_dificiles_ordenadas = sorted(self.diccionario.keys(), key=len, reverse=True)

        for palabra_dificil in palabras_dificiles_ordenadas:
            inicio = 0
            while inicio < len(texto):
                inicio = texto.lower().find(palabra_dificil.lower(), inicio)
                if inicio == -1:
                    break
                fin = inicio + len(palabra_dificil)
                if (inicio == 0 or not texto[inicio - 1].isalnum()) and (fin == len(texto) or not texto[fin].isalnum()):
                    palabras_dificles.append(palabra_dificil.capitalize())
                    inicio += len(palabra_dificil)
                else:
                    inicio += len(palabra_dificil)
        return palabras_dificles

    def glosario_palabras_dificiles(self, texto):
        texto_tokens = re.findall(r'\b\w+\b', texto.lower())
        glosario_list = []
        palabras_dificiles_ordenadas = sorted(self.diccionario.keys(), key=len, reverse=True)

        for palabra_dificil in palabras_dificiles_ordenadas:
            palabra_dificil_lower = palabra_dificil.lower()
            for token in texto_tokens:
                if palabra_dificil_lower == token:
                    entrada_glosario = f"{palabra_dificil.capitalize()}: {self.diccionario[palabra_dificil]}"
                    if entrada_glosario not in glosario_list:  # Evita duplicados en el glosario
                        glosario_list.append(entrada_glosario)

        return glosario_list
