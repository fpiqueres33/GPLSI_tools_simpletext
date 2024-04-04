import re

class Abreviaturas:
    def __init__(self, diccionario = None):
        if diccionario == None:
            diccionario = {
                "(a)": "alias", "a/a":"aire acondicionado", "A/A":" a la atención", "aa. vv.":"autores varios",
            "AA.VV.":"autores varios", "Abg.": "abogado", "Abg.do":"abogado", "Abg.da":"abogada",
            "a.C.":"antes de Cristo", "a/c": "a cuenta", "acept.":"aceptación", "a. de C.":"antes de Cristo",
            "a. de J. C.":"antes de Jesucristo",
            "d.C.":"después de Cristo", "admón.":"administración",
            "adm. or":"administrador", "adm.ora":"administradora",
            "admr.":"administrador", "a/f":"a favor",
            "a.i.":"de manera provisional", "a. J. C.": "antes de Jesucristo",
            "Alc.":"alcalde", "Alfz.":"alférez",
            "Almte.":"almirante", "apdo.": "apartado",
            "apénd.":"apéndice", "aprox.": "aproximadamente",
            "A.R. ":"Alteza Real", "arch.": "archivo",
            "Arq.":"arquitecto", "art.":"artículo",
            "Arz.":"arzobispo", "Asoc.":"asociación",
            "atte.":"atentamente", "atto.":"atento",
            "atta.":"atenta", "av.":"avenida",
            "avd.":"avenida", "avda.":"avenida",
            "ayte.":"ayudante", "Ayto.":"Ayuntamiento",
            "b.c.c.":"con copia oculta", "Bco.":"Banco",
            "Bibl.":"biblioteca", "b. l. m.":"besa la mano", "blvr.":"bulevar", "Bmo.":"Beatísimo",
            "Bma.":"Beatísima", "b/n":"blanco y negro", "Bo.":"barrio", "B.º":"barrio",
            "bol.":"boletín", "Br.":"bachiller", "Brig.":"Brigada", "c.":"calle", "c/":"calle", "cap.":"capítulo",
            "Cap.":"capital", "Cap. Fed.":"Capital Federal", "cap.º":"capítulo", "Card.":"cardenal",
            "C.C.": "casilla de correo", "c/c":"cuenta corriente", "cta.cte.":"cuenta corriente",
            "c.c.o.":"con copia oculta", "c.c.p.":"con copia para", "Cdad.":"ciudad", "cdra.":"cuadra",
            "c. e.":"correo electrónico", "cént.":"céntimo", "cts.":"céntimos", "c.f.s.":"coste, flete y seguro",
            "cgo.":"cargo", "ch /":"cheque", "Cía.":"compañía", "cje.":"corretaje", "Cmdt.":"Comandante",
            "Cnel.":"Coronel", "cód.":"código",
            "Comod.":"Comodoro", "com.ón":"comisión",
            "Comp.":"Compañía", "Comte.":"comandante ", "coop.": "cooperativa",
            "Contralmte.":"Contralmirante", "coord.": 'coordinador', "coord.ª": "coordinadora",
            "C.P.":"código postal", "C. P. N.":"contador público nacional", "C.por A.":"Compañía por Acciones",
            "cra.":"carrera", "crec.":"creciente", "cta.":"cuenta", "cta.cte.":"cuenta corriente",
            "Cte.":"comandante", "ctra.":"carretera", "ctv.":"centavo", "ctvo.":"centavo", "c/u":"cada uno",
            "D.":"don", "D.ª":"doña", "d.C.":"después de Cristo", "dcho.":"derecho", "dcha.":"derecha",
            "d. de C.":"después de Cristo", "d.de J.C.":"después de Jesucristo", "del.":"delegación",
            "D.E.P.":"descanse en paz", "depto.":"departamento", "desct.º":"descuento",
            "d/f":"día(s) fecha", "D.F.":"Distrito Federal", "diag.":"diagonal", "dicc.":"diccionario",
            "dir.":"dirección", "Dir. ":"Director - ra", "d. J. C.":"después de Jesucristo",
            "Dña.":"Doña,", "D. O.":"denominación de origen", "doc.":"documento",
            "D. O. C.":"denominación de origen calificada", "D.O.P.":"denominación de origen protegida",
            "dpto.":"departamento", "Dr.":"Doctor - ra", "dto.":"descuento", "dtto.":"distrito",
            "dupdo. ":"duplicado", "d / v":"día(s) vista", "e/":"envío", "e.c.":"era común", "e/c":"en cuenta",
            "ed.":"edición", "edit.":"editorial", "edo.":"estado", "e. g.":"por ejemplo",
            "ej.":"ejemplo", "Em.a":"Eminencia",
            "Emmo.":"Eminentísimo", "Emma.":"Eminentísima",
            "entlo.":"entresuelo", "e. p. d.":"en paz descanse",
            "e.p.m.":"en propia mano", "E. S.": "Estación de Servicio", "e.s.m.":"en sus manos",
            "esq.": "esquina", "et al.": "y otros", "etc.": "etcétera", "Exc.ª": "Excelencia", "excl.":"exclusive",
            "Excmo.": "Excelentísima", "Excma.":"Excelentísima", "f.ª":"factura", "facs.":"facsímil",
            "fasc.":"fascículo", "f. c. ":"ferrocarril",
            "ff.cc.":"ferrocarriles", "F. C.":"Fútbol Club", "F.C.": "Fútbol Club",
            "fca.":"fábrica", "F. de E.":"fe de erratas", "Fdo.":" firmado", "fec.":"hizo",
            "FF.AA.":"Fuerzas Armadas", "fig.":"figura", "Fr.":"Fray", "fra.":"factura", "Gdor. ":"Gobernador",
            "Gdora.":"Gobernadora", "Gob.":"Gobierno", "g. p.":"giro postal", "gr.":"gramo", "gral.":"general",
            "Gral.":"General", "gralm.":"generalmente", "g.t.":"giro telegráfico", "gta.":"glorieta",
            "g.v.":"gran velocidad", "Hble.":"Honorable", "Hno. ":"Hermano", "Hna.":"Hermana",
            "ib.":"en el mismo lugar", "ibid.":"en el mismo lugar", "id.":"el mismo", "i. e.":"esto es",
            "igl.ª":"iglesia", "Il.":"Ilustre", "Ilmo.":"Ilistrísimo", "Ilma.":"Ilustrísima",
            "Iltre.":"ilustre", "imp.":"imprenta", "impr.":"imprenta", "impto.":"impuesto", "incl.":"inclusive",
            "Ing.":"Ingeniero -ra", "Inst.":"Instituto", "izdo.":"izquierdo", "izda.":"izquierda",
            "J. C.":"Jesucristo", "Jhs.":"Jesucristo", "JJ. OO.":"Juegos Olímpicos", "jr.":"júnior", "lám.":"lámina",
            "l.c.":"en el lugar citado", "Lcdo.":"Licenciado", "Lcda.":"Licenciada", "lib.":"libro",
            "Lic.":"Licenciado - a", "loc. cit.":"el el lugar citado",
            "Ltd.":"Limited", "Ltdo. (fem. Ltda.)":"limitado", "Ltda.":"limitada", "Mag.":"Magistrado -a",
            "Magdo.":"Magistrado", "Magda.":"Magistrada",
            "Magfco.":"Magnífico", "Magfca.":"Magnífica",
            "manz.":"manzana ", "máx.":"máximo",
            "M.e":"Madre", "Mgdo. (fem. Mgda.)":"Magistrado",
            "Mgda.":"Magistrada", "Mgtr.":"Magíster",
            "mín.":"mínimo", "m. n.":"moneda nacional",
            "M.º":"Ministerio", "Mons.":"Monseñor",
            "mr.":"mártir", "ms.":"manuscrito",
            "Mtr.":"Máster", "mz.":"manzana",
            "N.ª S.ª":"Nuestra Señora", "nac.":"nacional", "N.B.":"observa bien", "N. del A.":"nota del autor",
            "N. de la A.":"nota de la autora", "N. del T.":"nota del traductor", "N.de la T.":"nota de la traductora",
            "n. e.":"nuestra era", "n.n.":"desconozco el nombre", "n.º":"número", "nro.":"número", "N. T.":"Nuevo Testamento ",
            "ntro.":"nuestro", "ntra.":"nuestra", "núm.":"número", "Ob.":"obispo -pa", "ob.cit.":"obra citada",
            "O. F. M.":"Orden de Frailes Menores", "O.M.":"Orden Ministerial", "op.":"opus", " p.cit.":"en la obra citada",
            "p. a.":"por ausencia","pág.":"página", "párr.":"párrafo", "pass.":"en varios lugares", "Pat.":"patente",
            "Pbro.":"Presbitero", "pdo. ":"pasado", "pda.":"pasada", "Pdte.":"Presidente",
            "Pdta.":"Presidenta", "p. ej.":"por ejemplo",
            "pg.":"página", "p. k.":"punto kilométrico",
            "pl.":"plaza", "plta.":"planta",
            "plza.":"plaza", "p. m.":"después del mediodía.",
            "P.M.":"Policía Militar", "Pnt.":"Pontícipe.",
            "p.º":"paseo", "pol. ind.":"Polígono Industral", "p.p.":"por poder.", "ppal.":"principal",
            "p.pdo.":"próximo pasado", "pral.":"principal",
            "Presb.":"Presbitero", "Prof.":"Profesor",
            "Prof.ª":"Profesora", "pról.":"prólogo", "prov.":"provincia", "pulg.":"pulgada", "p.v.":"pequeña velocidad",
            "P. V. P.":"precio de venta al público", "pza.":"plaza", "rbla.":"rambla", "R.D.":"Real Decreto",
            "Rdo.":"Reverendo", "Rda.":"Reverenda", "reg.":"registro", "Rep.":"república", "R. I. P.":"descanse en paz",
            "Rmo.(fem.Rma.)":"Reverendísimo", "Rma.":"Reverendísima",
            "r.º":"recto", "R. O.":"Real Orden", "r.p.m.":"revoluciones por minuto",
            "R. S. V. P.":"responda por favor.", "RR.HH.":"Recursos Humanos", "Rte.":"remitente", "Rvd.":"Reverendo - da",
            "Rvdmo.":"Reverendísimo", "Rvdma.":"Reverendísima", "Rvdo.":"Reverendo", "Rvda.":"Reverenda", "S.ª":"Señoría",
            "S.A.":"Sociedad Anónima", "S. A. A.":"Sociedad Anónima Abierta", "S.A.C.":"Sociedad Anómina Cerrada",
            "S. A. D.":"Sociedad Anónima Deportiva", "S.A.de C.V.":"Sociedad Anónima de Capital Variable",
            "S. A. I.":"Su Alteza Imperial", "S.A.L.":"Sociedad Anónima laboral", "S. A. R.":"Su Alteza Real",
            "S.A.S.":"Su Alteza Serenísima", "s/c":"su cuenta", "sc.":"es decir", "S. C.":"Sociedad Colectiva",
            "S.C.P.":"Sociedad Civil Particular", "S. Coop.":"Sociedad Cooporativa", "s.d.":"sin fecha", "Sdad.":"Sociedad",
            "Sdad.Ltda.":"Sociedad Limitada", "S. E.":"su excelencia", "Ser.mo":"Serenísimo - ma",
            "s. e. u o.":"salvo error u omisión", "s.f.;" : "sin fecha", "s / f":"sin fecha", "Sgto.":"sargento",
            "sig.":"siguiente", "S. L.":"Sociedad Limitada",
            "S.M.":"Su Majestad", "SS. MM.": "Sus Majestades", "Smo.":"Santísimo", "Sma.":"Santísima", "s. n.":"sin número", "s / n":"sin número",
            "s. n. m.":"sobre el nivel del mar", "Soc.":"Sociedad", "s. p.":"sin página",
            "S.P.":"Servicio Público", "s. p. i.":"sin pie de imprenta", "sr.":"sénior", "Sr.":"Señor",
            "Sr.ª":"Señora", "Sra.":"Señora", "S.R.C.":"Se Ruega Contestación", "S. R. L.":"Sociedad de Responsabilidad Limitada",
            "S.R.M.":"Su Real Majestad", "Srta.":"Señorita", "S.S.":"Su Santidad", "Sto.":"Santo",
            "Sta.":"Santa", "supl.":"suplemento", "s.v.":"bajo palabra", "tel.":"teléfono",
            "teléf.":"teléfono", "test.o":"testigo",
            "tfno.":"teléfono", "tít.":"título",
            "tlf.":"teléfono", "trad.":"traducción",
            "tte.":"transporte", "Tte.":"Teniente",
            "Ud. ":"usted", "Uds.":"ustedes",
            "Univ.":"Universidad", "urb.":"urbanización",
            "v /":"visto", "V. A.":"Vuestra Alteza",
            "Valmte.":"Vicealmirante", "V. A. R.":"Vuestra Alteza Real",
            "V.B.":"vuestra beatitud", "vcto.":"vencimiento",
            "Vd. ": "Usted", "Vdo.": "viudo",
            "Vda.":"viuda", "V. E.":"Vuestra Excelencia",
            "v.g.":"por ejemplo", "V. I.":"Vuestra Ilustrísima",
            "V.M.":"Vuestra Majestad", "v.º":"vuelto", "V.O.":"versión original", "V.º B.º":"visto bueno",
            "vol.":"volumen", "V. O. S.":"versión original subtitulada",
            "V.P.":"vuestra paternidad", "vs.":"versus", "V.S.":"Vuestra Señoría", "V. S. I.":"Vuestra señora Ilustrísima",
            "vto.":"vuelto", "vv. aa.":"varios autores",
            "VV.AA.":"varios autores", "y cols.":"y colaboradores", "C.C.": "Centro Comercial",
            "MSF": "Médicos Sin Fronteras", "FMI": "Fondo Monetario Internacional",
            "BCE": "Banco Central Europeo", "IRPF": "Impuesto sobre la Renta de las Personas Físicas",
            "OPV": "Oferta Pública de Acciones", "ISBN": "Sistema Internacional de Numeración de Libros",
                "ONG": "Organización No Gubernamental", "CD": "Disco Compacto", "IPC": "Índice de Precios al Consumo",
                "OMS": "Organización Mundial de la Salud", "CPU": "Unidad Central de Procesamiento",
                "CGPJ": "Consejo General del Poder Judicial", "I+D+i": "Investigación, Desarrollo e Innovación",
                "3D" : "Tres dimensiones", "VIH": "Virus de Inmunodeficiencia Humana",
                "DNI": "Documento nacional de Identidad",
                "ALCA": "Área de Libre Comercio de las Américas",
                "AMPA": "Asociación de Madres y Padres de Alumnos",
                "AVE": "Alta Velocidad Española",
                "CONACYT": "Consejo Nacional de Ciencia y Tecnología",
                "ERE": "Expediente de Regulación de Empleo",
                "ERTE": "Expediente de Regulación Temporal de Empleo",
                "FIFA": "Federación Internacional de Fútbol Asociación",
                "MEC": "Ministerio de Educación y Ciencia",
                "MERCOSUR": "Mercando Común del Sur",
                "Mercosus": "Mercado Común del Sur",
                "NIF": "Número de Identificación Fiscal",
                "NIE": "Número de Identificación de Extranjero",
                "ONU": "Organización de Naciones Unidas",
                "OTAN": "Organización del Tratado del Atlántico Norte",
                "PIB": "Producto Interior Bruto",
                "RR.HH": "Recursos Humanos",
                "RR.PP.": "Relaciones Públicas",
                "TIC": "Tecnologías de la Información",
                "UNED": "Universidad Nacional de Educación a Distancia",
                "VOSE": "Versión Original Subtitulada al Español",
                "VOSI": "Versión Original Subtitulada al Inglés",
                "EDUSI": "Estrategia de Desarrollo Urbano Sostenible e Integrado",
                "RTVE": "Radio Televisión Española",
                "ITV": "Inspección Técnica de Vehículos",
                "JJOO": "Juegos Olímpicos",
                "LGTB": "Lesbianas, Gais, Transexuales y Bisexuales",
                "RNE": "Radio Nacional de España",
                "UGT": "Unión General de Trabajdores",
                "TV3": "Televisión Catalana"

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

