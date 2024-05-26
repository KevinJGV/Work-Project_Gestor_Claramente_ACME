import usuarios
import reportes
import ventas
import json
import re
import datetime
import copy

# Formato docstring para copiar (esta linea no)
#     '''
#     ==> Recibe
#     <== Devuelve
#     '''


def int_val(msg, op_menu=0):
    '''
    Validador de valor numerico
    ==> Recibe String
    <== Devuelve Numero entero
    '''
    while True:
        try:
            if op_menu == 0:
                prompt = int(input(msg).strip())
                return prompt
            else:
                msgs(op_menu)
                prompt = int(input(msg).strip())
                return prompt
        except:
            input("Error de ingreso \nIntente nuevamente\n(Enter para continuar)\n")


def alpnum_val(msg):
    '''
    Validador de tipo string
    ==> Recibe String
    <== Devuelve String
    '''
    while True:
        prompt = None
        try:
            prompt = input(msg).strip()
            int(prompt)
            input(
                "Error de ingreso, debe ser alfanumerico \nIntente nuevamente\n(Enter para continuar)")
        except:
            return prompt


def validar_email_regexp(email, es_validado=False):
    '''
    Validador de string en formato de correo electronico
    ==> Recibe String
    <== Devuelve [es_validado = String,not es_validado = Bool]
    '''
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not es_validado:
        return re.match(pattern, email) is not None
    else:
        while True:
            if validar_email_regexp(email):
                return email
            else:
                input(
                    "Ingrese un correo electronico valido\n[Enter - Reintentar]\n")
                email = alpnum_val("> ")


def msgs(op):
    '''
    Visualizador de mensajes para el algoritmo
    ==> Recibe Numero entero
    '''
    try:
        if op == 0:
            print(
                "Para inicializar ingrese la ruta relativa actual de este scprit 'main.py: ")
        elif op == 1:
            print("=" * 6 + " CLARAMENTE ACME - PROGRAMA GESTOR v1 " + "=" * 6 +
                  "\nPara iniciar porfavor asegurese de tener un archivo .json con el cual trabajar.")
        elif op == 2:
            print("=" * 6 + " MENU PRINCIPAL " + "=" * 6 +
                  "\n1 - Gestión de usuarios\n2 - Reportes de usuarios\n3 - Tratador de servicios\n0 - Salir del software")
        elif op == 3:
            print(
                "\n>> Gestión de usuarios\n1 - Visualizar todos los usuarios\n2 - Gestionar usuario\n0 - Volver")
        elif op == 4:
            print("\n>> Reportes de usuarios\n1 - Visualizar todos los reportes\n2 - Gestionar un reporte\n0 - Volver")
        elif op == 5:
            print("\n>> Tratador de servicios\n1 - \n2 - \n0 - Volver")
        elif op == 6:
            print("[1 - Editar Nombre]   [2 - Editar direccion]   [3 - Editar contacto]   [4 - Editar categoria manualmente -NO RECOMENDADO]\n[5 - Contratar/Descontratar Servicio]   [6 - ELIMINAR USUARIO]   [0 - Cancelar]")
        elif op == 7:
            print("[1 - Ingresar: Reportes de Soportes]   [2 - Ingresar: Reportes de Reclamaciones]   [3 - Ingresar: Reportes de Sugerencias]  \n[0 - Cancelar]")
        elif op == 8:
            print("[1 - Agregar reporte]   [2 - Cerrar reporte]\n[0 - Cancelar]")
        elif op == 9:
            print("[1 - Agregar reporte]\n[0 - Cancelar]")
    except:
        print(op)


def validar_ruta_main(msg):
    '''
    Validador de archivo "main.py·
    ==> Recibe String
    <== Devuelve String
    '''
    while True:
        msgs(0)
        try:
            ruta = alpnum_val(msg)
            if ruta.endswith("main.py"):
                return ruta
            else:
                raise ValueError
        except:
            input("Asegurese de que la ruta es del archivo 'main.py'. \nIntente nuevamente\n(Enter para continuar)")


def validar_ruta_json(msg):
    '''   Validador de ruta y formato .json de archivo
    <== Devuelve Str
    '''
    msgs(1)
    while True:
        ruta = alpnum_val(msg)
        try:
            with open(ruta, "r"):
                if ruta.endswith(".json"):
                    print("Archivo json encontrado...")
                    return ruta
                else:
                    input(
                        "Formato de archivo invalido, debe ser .json para este programa. \nIntente nuevamente\n(Enter para continuar)")
        except:
            input("Archivo no encontrado. \nIntente nuevamente\n(Enter para continuar)")


def opener(ruta):
    ''' 
    Abridor de archivo codificado a utf-8
    ==> Recibe String
    <== Devuelve Estructura de datos
    '''
    with open(ruta, encoding="utf-8") as file:
        data = json.load(file)
        print("Base de datos cargados exitosamente...")
        return data


def menu_selector(*opcs, msg_op=None, una_opcion=False, continuar=False, returna= False,**kwargs):
    '''
    Menu generico, recibe funciones y argumentos para estas como argumentos a las cuales se accede a solicitud del usuario 
    ==> Recibe (Argumentos de longitud variable, Argumentos de palabra clave)
    ==> Devuelve lo que devuelve la funcion señalada en ella
    '''
    resultado_menu = None
    while True:
        try:
            if una_opcion:
                resultado_menu = opcs[0](kwargs)
                if continuar:   
                    op = int_val(
                                "¿Desea continuar esta gestion?\nCualquier digito - Continuar    0 - Salir\n> ")
                    if op == 0:
                        return 0
                    else:
                        return resultado_menu
                else:
                    if returna:
                        return resultado_menu
                    else:
                        return 0
            else:
                if continuar:   
                    op = int_val("> ", op_menu=msg_op)
                    if op == 0:
                        if returna:
                            return resultado_menu
                        else:
                            return 0
                    elif op <= len(opcs):
                        resultado_menu = opcs[op-1](kwargs)
                    else:
                        raise ValueError
                    op = int_val(
                                "¿Desea continuar esta gestion?\nCualquier digito - Continuar    0 - Salir\n> ")
                    if op == 0:
                        return 0
                    else:
                        return resultado_menu
                else:
                    op = int_val("> ", op_menu=msg_op)
                    if op == 0:
                        if returna:
                            return resultado_menu
                        else:
                            return 0
                    elif op <= len(opcs):
                        resultado_menu = opcs[op-1](kwargs)
                    else:
                        raise ValueError
        except Exception as e:
            print(e)
            print(type(e).__name__)
            input("Ingrese valor valido. \nIntente nuevamente\n(Enter para continuar)")


def export_file(data_in_kwargs, name_file):
    '''
    Exporta la base de datos
    ==> Recibe Diccionario de datos, Nombre del archivo deseado
    '''
    current_route = data_in_kwargs.get("script_path")
    current_route = current_route.replace("main.py", name_file)
    config = data_in_kwargs.get("db")
    jsonobject = json.dumps(config, indent=4, ensure_ascii=False)
    with open(current_route+".json", "w", encoding="utf-8") as nuevo_archivo:
        nuevo_archivo.write(jsonobject)


def encontrar_en_bdd(bdd, estructura):
    bdd = bdd.get("db")
    if estructura == "usuarios":
        bdd = bdd.get("usuarios")
        while True:
            user_id = int_val(
                "Ingresa ID existente para gestionar usuario o uno no registrado para crear perfil de usuario (0 - Cancelar)\n> ")
            if user_id != 0:
                user_is_finded = False
                for pos, user_reports_in_i in enumerate(bdd):
                    if user_reports_in_i["id"] == user_id:
                        user_is_finded = True
                        print("Usuario encontrado... Procesando...")
                        return [user_is_finded, pos, user_reports_in_i]
                if not user_is_finded:
                    return [False, None, None]
            else:
                return 0
    elif estructura == "reportes":
        bdd = bdd.get("reportes")
        while True:
            user_id = int_val("Ingresa ID del usuario (0 - Cancelar)\n> ")
            if user_id != 0:
                user_is_finded = False
                for pos, user_reports_in_i in enumerate(bdd):
                    if user_reports_in_i["id_usuario"] == user_id:
                        user_is_finded = True
                        print("Reportes encontrados...")
                        return [user_is_finded, pos, user_reports_in_i]
                if not user_is_finded:
                    input("Reporte ID no existe en la base de datos\nNo existe un usuario con dicho ID en la base de datos\n [Enter - Reintentar]")
            else:
                return 0


def generar_id(data, estructura, complejidad=0, id=None):
    '''
    Funcion pendiente de documentar
    ==> Recibe Diccionario
    <== Devuelve Diccionario
    '''
    if estructura == "usuarios":
        ids = [user["id"] for user in data]
        id = 1
        while True:
            if id not in ids:
                return id
            else:
                id += 1
    elif estructura == "reportes":
        ids = []
        bigger_num = 0
        if complejidad == 0:
            for estado_reporte, reportes in data.items():
                if len(data[estado_reporte]) != 0:
                    for reporte in reportes:
                        ids.append(reporte["id"])
        elif complejidad == "sugerencias":
            if len(data) != 0:
                for reporte in data:
                    ids.append(reporte["id"])
        if len(ids) != 0:
            for i in ids:
                temp_var = i.split("-")
                temp_var = int(temp_var[1])
                if temp_var > bigger_num:
                    bigger_num = temp_var
            id = "-".join([str(id),str(bigger_num+1)])
        else:
            id = "-".join([str(id),"1"])
        return id


def mostrar_en_terminal(data_in_kwargs, es_paginado=True, config=0):
    '''
    Muestra en consola el contenido .json paginadamente por defecto
    ==> Recibe Diccionario
    '''
    data_copy = copy.deepcopy(data_in_kwargs)
    if es_paginado:
        config = data_copy.get("mostrar_cofig")
        if config == 0:
            print("[NO SELECCIONADA CONFIGURACION PARA VISUALIZAR]")
        else:
            print(f">>> Visualizar todos los {config}")
            data_copy = data_copy.get("db").get(config)
            if config == "usuarios":
                keys = [key.upper() for key in data_copy[0].keys()]
                header = " | ".join(keys) + "\n"
                for pos, user in enumerate(data_copy):
                    data_copy[pos]["id"] = str(user["id"])
                    data_copy[pos]["servicios"] = str(len(user["servicios"]))
                paginacion(data_copy, header)
            elif config == "reportes":
                keys = [key.upper() for key in data_copy[0].keys()]
                keys[-1] = "AUN ABIERTOS"
                header = " | ".join(keys) + "\n"
                for pos_report, todos_los_reportes in enumerate(data_copy):
                    acceder = ["soporte", "reclamaciones"]
                    abiertas = 0
                    for clave_in_report, valor_in_report in todos_los_reportes.items():
                        if clave_in_report in acceder:
                            contador = sum(
                                [len(valor_in_report["abiertas"]), len(valor_in_report["cerradas"])])
                            data_copy[pos_report][clave_in_report] = str(
                                contador)
                            abiertas += len(valor_in_report["abiertas"])
                        elif clave_in_report == "id_usuario":
                            data_copy[pos_report][clave_in_report.lower()] = str(
                            data_copy[pos_report][clave_in_report.lower()])
                    data_copy[pos_report]["sugerencias"] = str(
                        len(data_copy[pos_report]["sugerencias"]))
                    data_copy[pos_report]["Cantidad Reportes"] = str(abiertas)
                paginacion(data_copy, header)
    else:
        if isinstance(config,str):
            if config == "usuarios":
                keys = list(data_copy.keys())
                for key in keys:
                    if key != "servicios":
                        print(f"{key.upper()} => {data_copy[key]}")
                print("SERVICIOS ACTUALES DEL USUARIO:")
                if len(data_copy["servicios"]) != 0:
                    for servicio in data_copy["servicios"]:
                        print(f"-> {servicio['servicio']}")
                else:
                    print("[Este usuario no tiene servicios contratados actualemente]")
            elif config == "reportes":
                keys = [key.title() for key in data_copy.keys()]
                header = " | ".join(keys) + "\n"
                acceder = ["soporte", "reclamaciones"]
                for clave_in_report, valor_in_report in data_copy.items():
                    if clave_in_report in acceder:
                        data_copy[clave_in_report] = str(
                            sum([len(valor_in_report["abiertas"]), len(valor_in_report["cerradas"])]))
                    elif clave_in_report == "sugerencias":
                        data_copy[clave_in_report] = str(len(valor_in_report))
                    else:
                        data_copy[clave_in_report] = str(valor_in_report)
                line = " | ".join(list(data_copy.values())) + "\n"
                print(header + "\n" + line)
        elif isinstance(config,list):
            if config[0] == "s&r&s":
                config[1] -= 1
                op = ["soporte", "reclamaciones", "sugerencias"]
                print(f">>>> Reportes de {op[config[1]].title()}")
                header = "ID REPORTE | DESCRIPCIÓN | ESTADO\n"
                body = ""
                if config[1] != 2:
                    if len(data_copy[op[config[1]]]["abiertas"]) != 0 or len(data_copy[op[config[1]]]["cerradas"]) != 0:
                        for tipo_reportes, lista_reportes in data_copy[op[config[1]]].items():
                            for reporte in lista_reportes:
                                body += f"{reporte["id"]} | {reporte["descripcion"]} | {tipo_reportes[:-1].capitalize()}\n"
                    else:
                        body = "[USUARIO SIN REPORTES]"
                else:
                    if len(data_copy[op[config[1]]]) != 0:
                        for reporte in data_copy[op[config[1]]]:
                                body += f"{reporte["id"]} | {reporte["descripcion"]}\n"
                    else:
                        body = "[USUARIO SIN REPORTES]"
                print(header + body)


def paginacion(dict_to_print, header):
    start = 0
    pag_size = 5
    while True:
        end = start + pag_size
        print(header)
        if end > len(dict_to_print):
            end = len(dict_to_print)
        if start < 0:
            start = 0
        seccion = dict_to_print[start:end]
        current_page = ""
        for dic in seccion:
            line = " | ".join(list(dic.values())) + "\n"
            current_page += line
        print(current_page)
        print(
            f"\t< {start} / {end} >\n[0 - Pagina anterior]    [1 - Pagina siguiente]\n[2 - Volver]")
        movimiento = int_val("> ")
        if movimiento == 2:
            break
        elif movimiento == 1:
            start += pag_size
            if start > end:
                start -= pag_size
        elif movimiento == 0:
            if start != 0:
                start -= pag_size


def logica_gestiones(gestion, var_data_is_finded, var_data_in_i, var_pos, data_in_kwargs):
    if var_data_is_finded != 0:
        if gestion == "usuarios":
            if var_data_is_finded[0]:
                while True:
                    mostrar_en_terminal(
                        var_data_in_i, es_paginado=False, config=gestion)
                    op = int_val("> ", 6)
                    if op >= 0 and op <= 6:
                        if op == 1 or op == 2 or op == 3:
                            res = menu_selector(usuarios.editar_perfil_usuario,una_opcion=True, continuar=True,op=op,data_in_kwargs=data_in_kwargs,pos_user=var_pos)
                            if res == 0:
                                break
                        elif op == 4:
                            res = menu_selector(usuarios.editar_categoria,una_opcion=True,continuar=True, data_in_kwargs=data_in_kwargs,pos_user=var_pos)
                            if res == 0:
                                break
                        elif op == 5:
                            print("funcionalidad_en_desarrollo")
                            if res == 0:
                                break
                        elif op == 6:
                            menu_selector(usuarios.eliminar_usuario,una_opcion=True,continuar=True, data_in_kwargs=data_in_kwargs,pos_user=var_pos)
                            break
                        else:
                            break
                    else:
                        input(
                            "Seleccione una opcion dada\n[Enter - Reintentar]\n")
            else:
                usuarios.agregar_usuario(data_in_kwargs)
        elif gestion == "reportes":
            if var_data_is_finded[0]:
                while True:
                    mostrar_en_terminal(
                        var_data_in_i, es_paginado=False, config="reportes")
                    op_estructura = int_val("> ", 7)
                    if op_estructura == 0:
                        break
                    elif op_estructura >= 1 and op_estructura <= 3:
                        while True:
                            mostrar_en_terminal(var_data_in_i,es_paginado=False,config=["s&r&s",op_estructura])
                            if op_estructura == 1 or op_estructura == 2:
                                res = menu_selector(reportes.agregar_reporte, reportes.cerrar_reporte, msg_op=8, continuar=True,data_in_kwargs=data_in_kwargs, pos_report=var_pos, op_estructura=op_estructura)
                                if res == 0:
                                    break
                            elif op_estructura == 3:
                                res = menu_selector(reportes.agregar_reporte, msg_op=9, continuar=True,data_in_kwargs=data_in_kwargs, pos_report=var_pos, op_estructura=op_estructura)
                                if res == 0:
                                    break
                    else:
                        input(
                            "Seleccione una opcion dada\n[Enter - Reintentar]\n")
    else:
        print("> Cancelando...")
