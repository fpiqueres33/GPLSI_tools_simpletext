class Anglicismos:
    def __init__(self, diccionario=None):
        if diccionario is None:
            diccionario = {
                "email": "correo electrónico", "emails": "correos electrónicos",
                "feedback": "retroalimentación",
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
                "parking": "aparcamiento",
                "camping": "campamento",
                "disc-jokey": "pinchadiscos",
                "ferry": "transbordador",
                "gin": "ginebra",
                "show": "espectáculo",
                "self-service": "autoservicio",
                "sponsor": "patrocinador", "sponsors": "patrocinadores",
                "bay-sitter": "canguro",
                "free lance": "autónomo",
                "gang": "banda",
                "look": "imagen",
                "lunch": "aperitivo",
                "overbooking": "sobreventa",
                "speech": "discurso",
                "chic": "elegante",
                "sweater": "suéter",
                "biopic": "película biográfica",
                "detox": "desintoxicación",
                "fake": "falso",
                "runner": "corredor",
                "footing": "correr",
                "pole position": "primera posición",
                "safety car": "coche de seguridad",
                "stop and go": "pare y siga",
                "doping": "dopaje",
                "team": "equipo",
                "wellness": "bienestar",
                "personal trainer": "entrenador personal",
                "personal shopper": " asesor de compras"
            }

        self.diccionario = diccionario

    def sustituir_anglicismos(self, texto):
        # Reemplaza los anglicismos en el texto por sus traducciones
        anglicismos_ordenados = sorted(self.diccionario.keys(), key=len, reverse=True)
        texto_original = texto  # Guardamos el texto original para preservar las mayúsculas
        texto = texto.lower()  # Trabajamos con una versión en minúsculas del texto para la búsqueda

        for anglicismo in anglicismos_ordenados:
            inicio = 0
            while inicio < len(texto):
                inicio = texto.find(anglicismo.lower(), inicio)
                if inicio == -1:
                    break
                fin = inicio + len(anglicismo)
                if (inicio == 0 or not texto[inicio - 1].isalnum()) and (fin == len(texto) or not texto[fin].isalnum()):
                    # Verificar si la palabra en el texto original estaba capitalizada
                    if texto_original[inicio].isupper():
                        reemplazo = self.diccionario[anglicismo.lower()].capitalize()
                    else:
                        reemplazo = self.diccionario[anglicismo.lower()]

                    texto_original = texto_original[:inicio] + reemplazo + texto_original[fin:]
                    texto = texto[:inicio] + reemplazo.lower() + texto[
                                                                 fin:]  # Actualizamos también la versión en minúsculas para mantener la coherencia
                    inicio += len(reemplazo)
                else:
                    inicio += len(anglicismo)
        return texto_original


    def detectar_anglicismos(self, texto):
        # Detecta anglicismos en el texto y los devuelve capitalizados si se encuentran
        anglicismos_detectados = []
        anglicismos_ordenados = sorted(self.diccionario.keys(), key=len, reverse=True)
        for anglicismo in anglicismos_ordenados:
            inicio = 0
            while inicio < len(texto):
                inicio = texto.lower().find(anglicismo.lower(), inicio)
                if inicio == -1:
                    break
                fin = inicio + len(anglicismo)
                if (inicio == 0 or not texto[inicio - 1].isalnum()) and (fin == len(texto) or not texto[fin].isalnum()):
                    anglicismos_detectados.append(anglicismo)
                    inicio += len(anglicismo)
                else:
                    inicio += len(anglicismo)
        return anglicismos_detectados
