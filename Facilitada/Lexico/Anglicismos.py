class Anglicismos:
    def __init__(self, diccionario=None):
        if diccionario is None:
            diccionario = {
                "email": "correo electrónico", "emails": "correos electrónicos",
                "feedback": "retroalimentación",
                "marketing": "mercadotecnia",
                "coach": "entrenador",
                "hobby": "pasatiempo",
                "fitness": "entrenamiento físico",
                "smartphone": "teléfono inteligente",
                "mouse": "ratón",
                "link": "enlace",
                "login": "inicio de sesión",
                "hashtag": "etiqueta",
                "selfie": "autofoto", "selfies": "autofotos",
                "streaming": "transmisión en vivo",
                "layout": "diseño",
                "software": "programa de ordenador",
                "hardware": "ordenador",
                "blog": "diario",
                "download": "descargar",
                "online": "en línea",
            }

        self.diccionario = diccionario

    def sustituir_anglicismos(self, texto):
        anglicismos_ordenados = sorted(self.diccionario.keys(), key=len, reverse=True)
        for anglicismo in anglicismos_ordenados:
            inicio = 0
            while inicio < len(texto):
                inicio = texto.find(anglicismo, inicio)
                if inicio == -1:
                    break
                fin = inicio + len(anglicismo)
                if (inicio == 0 or not texto[inicio-1].isalnum()) and (fin == len(texto) or not texto[fin].isalnum()):
                    texto = texto[:inicio] + self.diccionario[anglicismo] + texto[fin:]
                    inicio += len(self.diccionario[anglicismo])
                else:
                    inicio += len(anglicismo)
        return texto

    def detectar_anglicismos(self, texto):
        anglicismos_detectados = []
        anglicismos_ordenados = sorted(self.diccionario.keys(), key=len, reverse=True)
        for anglicismo in anglicismos_ordenados:
            inicio = 0
            while inicio < len(texto):
                inicio = texto.find(anglicismo, inicio)
                if inicio == -1:
                    break
                fin = inicio + len(anglicismo)
                if (inicio == 0 or not texto[inicio - 1].isalnum()) and (fin == len(texto) or not texto[fin].isalnum()):
                    anglicismos_detectados.append(anglicismo)
                    inicio += len(anglicismo)
                else:
                    inicio += len(anglicismo)
        return anglicismos_detectados
