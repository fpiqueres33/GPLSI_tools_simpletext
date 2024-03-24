from flask import Flask, request, render_template, Response
from Resumen.ClearTextTS import ClearTextTS
from Parser_documents import Parser_Documents
from Facilitada.Lexico.API_F_Lexico import API_Lexico
from Facilitada.Sintactico.API_F_Sintactico import ApiSintactico
from Facilitada.Topicos.Topicos import Topicos


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    result_text = ""
    input_text = ""  # Variable para almacenar el texto introducido
    detected_number = None  # Variable para almacenar las detecciones.

    if request.method == 'POST':
        action = request.form.get('action')
        mostrar_deteccion = request.form.get(
            'mostrarDeteccion') == 'on'  # Captura el estado del checkbox "Mostrar Detección"

        # Comprobar si hay un archivo cargado
        file = request.files.get('file')
        if file and file.filename:
            parser = Parser_Documents(file)
            try:
                input_text = parser.parse()
            except ValueError as e:
                return str(e)

        else:
            # Si no hay archivo, usar el texto del textarea
            input_text = request.form.get('inputText', '')

        if not input_text.strip():
            # Si no hay texto para procesar
            return "No hay texto para procesar"

        if action == 'simplify':
            # Captura los valores de las casillas de verificación
            #Funciones Léxicas
            use_adverbios = request.form.get('useAdverbios') == 'on'
            use_numeros = request.form.get('useNumero') == 'on'
            use_romanos = request.form.get('useRomanos') == 'on'
            use_superlativos = request.form.get('useSuperlativos') == 'on'
            use_abreviaturas = request.form.get('useAbreviaturas') == 'on'
            use_anglicismos = request.form.get('useAnglicismos') == 'on'

            #Funciones sintácticas
            use_complejos = request.form.get('useComplejos') == 'on'
            use_impersonal = request.form.get('useImpersonal') == 'on'
            use_nominalizacion = request.form.get('useNominalizacion') == 'on'

            # Aquí se procesa el texto con las opciones seleccionadas
            result_text, detecciones = process_simplify(input_text, use_adverbios, use_complejos, use_numeros, use_romanos,
                                           use_superlativos, use_abreviaturas, use_anglicismos, use_impersonal, use_nominalizacion)
            if mostrar_deteccion:
                result_text += "\n\nElementos detectados:\n" + str(detecciones)


        #Lógica para la generación de resumen
        elif action == 'resumen':
            clear_text_ts = ClearTextTS()
            if file and file.filename:
                # Si hay un archivo, usa el archivo
                parser = Parser_Documents(file)
                try:
                    parsed_text = parser.parse()
                except ValueError as e:
                    return str(e)

                result = clear_text_ts.generate_summary(parsed_text)

            else:
                # Si no hay archivo, usa el texto ingresado directamente
                result = clear_text_ts.generate_summary(input_text)
            result_text = result['summary']

        elif action == 'Topicos':
            topicos = Topicos()
            result_text = topicos.procesar_texto(input_text)



    return render_template('index.html', result_text=result_text, input_text=input_text)


def process_simplify(input_text, use_adverbios, use_numeros, use_romanos, use_superlativos, use_abreviaturas,
                     use_anglicismos, use_complejos, use_impersonal, use_nominalizacion):
    # Configurar las opciones para API_Lexico y API_Sintactico
    opciones_lexico = {
        "habilitar_adverbios": use_adverbios,
        "habilitar_superlativos": use_superlativos,
        "habilitar_numeros": use_numeros,
        "habilitar_romanos": use_romanos,
        "habilitar_complejos": use_complejos,
        "habilitar_abreviaturas": use_abreviaturas,
        "habilitar_anglicismos": use_anglicismos
    }

    opciones_sintactico = {
        "habilitar_nominalizacion": use_nominalizacion,
        "habilitar_impersonales": use_impersonal,
        "habilitar_complejos": use_complejos
    }

    #Asegurar los valores marcados en el check-box de index.html
    use_adverbios = request.form.get('useAdverbios') == 'on'
    use_numeros = request.form.get('useNumero') == 'on'
    use_romanos = request.form.get('useRomanos') == 'on'
    use_superlativos = request.form.get('useSuperlativos') == 'on'
    use_abreviaturas = request.form.get('useAbreviaturas') == 'on'
    use_anglicismos = request.form.get('useAnglicismos') == 'on'

    # Funciones sintácticas
    use_complejos = request.form.get('useComplejos') == 'on'
    use_impersonal = request.form.get('useImpersonal') == 'on'
    use_nominalizacion = request.form.get('useNominalizacion') == 'on'

    # Crear instancias de API_Lexico y API_Sintactico
    api_lexico = API_Lexico(habilitar_adverbios=use_adverbios, habilitar_superlativos=use_superlativos,
                            habilitar_numeros=use_numeros, habilitar_romanos=use_romanos,
                            habilitar_abreviaturas=use_abreviaturas, habilitar_anglicismos=use_anglicismos)

    api_sintactico = ApiSintactico(habilitar_nominalizacion=use_nominalizacion,  # O cualquier valor por defecto que desees
                                   habilitar_impersonales=use_impersonal,  # O cualquier valor por defecto que desees
                                   habilitar_complejos=use_complejos)

    # Procesar el texto utilizando las API
    texto_transformado_lexico, glosario_lexico = api_lexico.transformar_lexico(input_text)
    texto_transformado_sintactico, glosario_sintactico = api_sintactico.transformar_sintactico(texto_transformado_lexico)

    #Procesar el texto final y añadir los glosarios.
    texto_final = texto_transformado_sintactico
    if glosario_lexico:
        texto_final += "\nGLOSARIO ANGLICISMOS:\n" + glosario_lexico
    if glosario_sintactico:
        texto_final += "\nGLOSARIO ORACIONES COMPLEJAS:\n" + glosario_sintactico

    # Ejecutar las detecciones
    detecciones_lexico = api_lexico.detecciones_lexico(input_text)
    detecciones_sintactico = api_sintactico.detecciones_sintactico(input_text)


    # Formatear las detecciones para la salida
    detecciones = {
        "lexico": detecciones_lexico,
        "sintactico": detecciones_sintactico
    }

    return texto_final, detecciones



@app.route('/download')
def download():
    content = request.args.get('content', default='')
    return Response(
        content,
        mimetype="text/plain",
        headers={"Content-Disposition": "attachment;filename=result.txt"}
    )


if __name__ == "__main__":
    app.run(debug=True)
