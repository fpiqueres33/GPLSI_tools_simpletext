from Facilitada.Sintactico.Complejos import Complejos
from Facilitada.Sintactico.Impersonal import Impersonal
from Facilitada.Sintactico.Nominalizacion import Nominalizacion

class API_Sintactico:
    def __init__(self, habilitar_nominalizacion= True, habilitar_impersonales= True, habilitar_complejos= True):
        # Configuraciones iniciales para cada tipo de transformación
        self.habilitar_nominalizacion = habilitar_nominalizacion
        self.habilitar_impersonales = habilitar_impersonales
        self.habilitar_complejos = habilitar_complejos

        # Inicializar las clases para cada transformación
        self.nominalizacion = Nominalizacion() if habilitar_nominalizacion else None
        self.impersonales = Impersonal() if habilitar_impersonales else None
        self.complejos = Complejos() if habilitar_complejos else None

    def transformar_sintactico(self, texto):
        # Aquí se aplicarán las transformaciones según la configuración
        texto_transformado = texto

        if self.habilitar_nominalizacion and self.nominalizacion:
            texto_transformado = self.nominalizacion.reemplazar_nominalizacion(texto_transformado)

        if self.habilitar_impersonales and self.impersonales:
            texto_transformado = self.impersonales.reemplazar_impersonal(texto_transformado)

        if self.habilitar_complejos and self.complejos:
            texto_transformado = self.complejos.detectar_y_sustituir_conectores(texto_transformado)

        return texto_transformado

    def detecciones_sintactico(self, texto):
        detecciones = {}

        if self.habilitar_nominalizacion and self.nominalizacion:
            detecciones['nominalizaciones'] = self.nominalizacion.detectar_nominalizacion_solo_frases(texto)

        if self.habilitar_impersonales and self.impersonales:
            detecciones['impersonales'] = self.impersonales.detectar_impersonal_solo_frases(texto)

        if self.habilitar_complejos and self.complejos:
            detecciones['complejos'] = self.complejos.detectar_conectores_complejos(texto)

        return detecciones


'''
sintactico_Test = API_Sintactico()

# Texto de prueba que contiene al menos un ejemplo de cada tipo de construcción
texto = """
A pesar de que la situación era compleja, se logró resolver con éxito. El hablar de forma clara es importante. 
En cuanto a los detalles, los iremos analizando uno por uno.
"""

# Usamos el método detectar_todo para analizar el texto
transformacion = sintactico_Test.transformar_sintactico(texto)
detecciones = sintactico_Test.detecciones_sintactico(texto)

# Imprimimos los resultados
print("Resultados de la detección:")
for tipo, casos in detecciones.items():
    print(f"{tipo}: {casos}")
print("Texto transformado: ", transformacion)


'''

