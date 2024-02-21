class API_Lectura_Facilitada:
    def __init__(self, habilitar_lexico=True, habilitar_sintactico=True, **kwargs):
        # kwargs puede incluir configuraciones específicas para léxico y sintáctico
        self.api_lexico = API_Lexico(**kwargs) if habilitar_lexico else None
        self.api_sintactico = API_Sintactico(**kwargs) if habilitar_sintactico else None

    def transformar_texto(self, texto):
        texto_transformado = texto
        if self.api_lexico:
            texto_transformado = self.api_lexico.transformar_lexico(texto_transformado)
        if self.api_sintactico:
            texto_transformado = self.api_sintactico.transformar_sintactico(texto_transformado)
        return texto_transformado

    def detecciones_texto(self, texto):
        detecciones = {}
        if self.api_lexico:
            detecciones['lexico'] = self.api_lexico.detecciones_lexico(texto)
        if self.api_sintactico:
            detecciones['sintactico'] = self.api_sintactico.detecciones_sintactico(texto)
        return detecciones
