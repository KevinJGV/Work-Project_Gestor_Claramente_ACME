import usuarios
import reportes
import ventas
import json
import re
import copy
from datetime import datetime


# Formato docstring para copiar (esta linea no)
#     '''
#     ==> Recibe
#     <== Devuelve
#     '''


def int_val(msg, data_in_kwargs, op_msg=0):
    '''
    Validador de valor numerico
    ==> Recibe String
    <== Devuelve Numero entero
    '''
    while True:
        try:
            if op_msg == 0:
                prompt = int(input(msg).strip())
                return prompt
            else:
                msgs(op_msg)
                prompt = int(input(msg).strip())
                return prompt
        except:
            reportes_txt("Intento de ingreso con valor alfanumerico donde se requeria valor numerico",data_in_kwargs)
            input("Error de ingreso \nIntente nuevamente\n(Enter para continuar)\n")


def alpnum_val(msg, data_in_kwargs):
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
            reportes_txt("Intento de ingreso con valor numerico donde se requeria valor alfanumerico",data_in_kwargs)
            input(
                "Error de ingreso, debe ser alfanumerico \nIntente nuevamente\n(Enter para continuar)")
        except:
            return prompt


def validar_email_regexp(email, data_in_kwargs,es_validado=False):
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
            if validar_email_regexp(email, data_in_kwargs):
                return email
            else:
                reportes_txt("Mal ingreso de contacto, no es un correo electronico valido",data_in_kwargs)
                input(
                    "Ingrese un correo electronico valido\n[Enter - Reintentar]\n")
                email = alpnum_val("> ", data_in_kwargs)


def msgs(op):
    '''
    Visualizador de mensajes para el algoritmo
    ==> Recibe Numero entero
    '''
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
        print("[1 - Editar Nombre]   [2 - Editar direccion]   [3 - Editar contacto]\n[4 - Editar categoria manualmente -NO RECOMENDADO] [5 - ELIMINAR USUARIO]   [0 - Cancelar]")
    elif op == 7:
        print("[1 - Ingresar: Reportes de Soportes]   [2 - Ingresar: Reportes de Reclamaciones]   [3 - Ingresar: Reportes de Sugerencias]  \n[0 - Cancelar]")
    elif op == 8:
        print("[1 - Agregar reporte]   [2 - Cerrar reporte]\n[0 - Cancelar]")
    elif op == 9:
        print("[1 - Agregar reporte]\n[0 - Cancelar]")
    elif op == 10:
        print("[1 - Contratacion / Descontratacion de Servicio]   [2 - Visualizar historial de ventas]\n[0 - Cancelar]")
    elif op == 11:
        print("[1 - Contratar servicio]   [2 - Descontratar servicio]\n[0 - Cancelar]")
    elif op == "input":
        print("Selecciona una opcion para continuar (0 - cancelar)")


def validar_ruta_main(msg):
    '''
    Validador de archivo "main.py·
    ==> Recibe String
    <== Devuelve String
    '''
    while True:
        msgs(0)
        try:
            ruta = alpnum_val(msg, "main.py")
            if ruta.endswith("main.py"):
                return ruta
            else:
                raise ValueError
        except:
            reportes_txt("Ruta main.py incorrecta")
            input("Asegurese de que la ruta es del archivo 'main.py'. \nIntente nuevamente\n(Enter para continuar)")


def validar_ruta_json(msg, script_path):
    '''   Validador de ruta y formato .json de archivo
    <== Devuelve Str
    '''
    msgs(1)
    while True:
        ruta = alpnum_val(msg, script_path)
        try:
            with open(ruta, "r"):
                if ruta.endswith(".json"):
                    print("Archivo json encontrado...")
                    return ruta
                else:
                    input(
                        "Formato de archivo invalido, debe ser .json para este programa. \nIntente nuevamente\n(Enter para continuar)")
        except:
            reportes_txt("Ruta db.json incorrecta", data_in_kwargs=script_path)
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


def menu_selector(*opcs, msg_op=None, una_opcion=False, continuar=False, envia_op=None,op_externa=False, limitador=False,contenido_terminal=False,**kwargs):
    '''
    Menu generico, recibe funciones y argumentos para estas como argumentos a las cuales se accede a solicitud del usuario 
    ==> Recibe (Argumentos de longitud variable, Argumentos de palabra clave)
    ==> Devuelve lo que devuelve la funcion señalada en ella
    '''
    resultado_menu = 0
    contador = 0
    data_in_kwargs = None
    data_in_kwargs = kwargs.get("script_path")
    if data_in_kwargs is None:
        data_in_kwargs = kwargs.get("data_in_kwargs")
    while True:
        try:
            op = op_externa
            if contador == 1:
                break
            elif op_externa == False:
                op = int_val("> ", data_in_kwargs, op_msg=msg_op)
                if contenido_terminal:
                    contador = 1
            if una_opcion:
                if op == 0:
                    return resultado_menu
                elif op >= 1 and op <= limitador:
                    if envia_op:
                        resultado_menu = opcs[0](op,kwargs)
                        if op_externa:
                            break
                    else:
                        resultado_menu = opcs[0](kwargs)
                        if op_externa:
                            break
                else:
                    raise ValueError
            else:
                if op == 0:
                    return resultado_menu
                elif op >= 1 and op <= len(opcs):
                    if envia_op:
                        resultado_menu = opcs[op-1](op,kwargs)
                    else:
                        resultado_menu = opcs[op-1](kwargs)
                else:
                    raise ValueError
            if continuar:
                op = int_val(
                            "¿Desea continuar esta gestion?\nCualquier digito - Continuar    0 - Salir\n> ", data_in_kwargs)
                if op == 0:
                    if resultado_menu is None:
                        resultado_menu = 0
                    return resultado_menu
                else:
                    return resultado_menu
        except:
            reportes_txt("Opcion fuera de rango en menu generico",kwargs)
            input("Ingrese valor valido. \nIntente nuevamente\n(Enter para continuar)")


def export_file(data_in_kwargs, name_file,no_kwargs=False):
    '''
    Exporta la base de datos
    ==> Recibe Diccionario de datos, Nombre del archivo deseado
    '''
    current_route = None
    config = None
    if not no_kwargs:
        current_route = data_in_kwargs.get("script_path")
        current_route = current_route.replace("main.py", name_file)
        config = data_in_kwargs.get("db")
    else:
        current_route = name_file
        config = data_in_kwargs
    jsonobject = json.dumps(config, indent=4, ensure_ascii=False)
    with open(current_route+".json", "w", encoding="utf-8") as nuevo_archivo:
        nuevo_archivo.write(jsonobject)



def gestor(op,data_in_kwargs):
    estructura = ["usuarios","reportes","ventas"]
    if estructura[op-1] == "usuarios" or estructura[op-1] == "reportes":
        print(f">>> Gestionar {estructura[op-1]}")
        data_is_finded = encontrar_en_bdd(
            data_in_kwargs, estructura[op-1])
        if data_is_finded != 0:
            if data_is_finded[0] is not False:
                data_in_i = data_is_finded[2]
                pos = data_is_finded[1]
                logica_gestiones(
                    estructura[op-1], data_in_kwargs,var_data_is_finded=data_is_finded, var_data_in_i=data_in_i, var_pos=pos)
            else:
                reportes_txt("Intento de ingreso a perfil de usuario no creado",data_in_kwargs)
                input("Usuario sin perfil, inicie modulo de ventas para crear su perfil\n[Enter - Regresar]\n")
    else:
        print(">>> Tratador de ventas")
        data_is_finded = encontrar_en_bdd(
            data_in_kwargs, estructura[op-1])
        logica_gestiones(estructura[op-1],data_in_kwargs, var_data_is_finded=data_is_finded)



def encontrar_en_bdd(data_in_kwargs, estructura, alt=None):
    bdd = data_in_kwargs.get("db")
    if estructura == "usuarios":
        bdd = bdd.get("usuarios")
        while True:
            user_id = None
            if alt == "venta":
                user_id = int_val(
                "Ingresar ID para esta gestion o una inexistente para crear perfil de usuario y continuar (0 - Cancelar)\n> ", data_in_kwargs)
            else:
                user_id = int_val(
                "Ingresar ID existente para esta gestion (0 - Cancelar)\n> ", data_in_kwargs)
            if user_id != 0:
                user_is_finded = False
                for pos, user_reports_in_i in enumerate(bdd):
                    if user_reports_in_i["id"] == user_id:
                        user_is_finded = True
                        print("Usuario encontrado... Procesando...")
                        return [user_is_finded, pos, user_reports_in_i]
                if not user_is_finded:
                    return [False, user_id]
            else:
                return 0
    elif estructura == "reportes":
        bdd = bdd.get("reportes")
        while True:
            user_id = int_val("Ingresa ID del usuario (0 - Cancelar)\n> ", data_in_kwargs)
            if user_id != 0:
                user_is_finded = False
                for pos, user_reports_in_i in enumerate(bdd):
                    if user_reports_in_i["id_usuario"] == user_id:
                        user_is_finded = True
                        print("Reportes encontrados...")
                        return [user_is_finded, pos, user_reports_in_i]
                if not user_is_finded:
                    reportes_txt("Intento de ingreso a reportes de usuario sin registrar",data_in_kwargs)
                    input("Reporte ID no existe en la base de datos\nNo existe un usuario con dicho ID en la base de datos\n [Enter - Reintentar]")
            else:
                return 0
    else:
        return bdd.get("ventas")



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


def mostrar_en_terminal(data_in_kwargs, requiere_mostrar_config=True,es_paginado=True, config=0):
    '''
    Muestra en consola el contenido .json paginadamente por defecto
    ==> Recibe Diccionario
    '''
    data_copy = copy.deepcopy(data_in_kwargs)
    body = ""
    if es_paginado:
        if requiere_mostrar_config:
            config = data_copy.get("mostrar_cofig")
        if config == 0:
            print("[NO SELECCIONADA CONFIGURACION PARA VISUALIZAR]")
        elif config == "historial":
            body = []
            header = " FECHA DE VENTA | SERVICIO "
            line = ""
            for venta in data_in_kwargs:
                line += f' {venta["fecha"]} | {venta["venta"]}\n'
                body.append(line)
            paginacion(body,header, data_in_kwargs)
        else:
            print(f">>> Visualizar todos los {config}")
            data_copy = data_copy.get("db").get(config)
            if config == "usuarios":
                keys = [key.upper() for key in data_copy[0].keys()]
                header = " | ".join(keys) + "\n"
                for pos, user in enumerate(data_copy):
                    data_copy[pos]["id"] = str(user["id"])
                    data_copy[pos]["servicios"] = str(len(user["servicios"]))
                paginacion(data_copy, header, data_in_kwargs)
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
                paginacion(data_copy, header, data_in_kwargs)
    else:
        if isinstance(config,str):
            if config == "usuarios":
                keys = list(data_copy.keys())
                for key in keys:
                    if key != "servicios":
                        line = f"{key.upper()} => {data_copy[key]}\n"
                        body += line
                body += "SERVICIOS ACTUALES DEL USUARIO:\n"
                if len(data_copy["servicios"]) != 0:
                    for servicio in data_copy["servicios"]:
                        line = f"-> {servicio['servicio']}\n"
                        body += line
                else:
                    body += "[Este usuario no tiene servicios contratados actualemente]"
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
                body = header + "\n" + line
            elif config == "servicios":
                body += " SERVICIOS PARA OFRECER | TARIFA MENSUAL ESTANDAR\n"
                for servicio in data_copy:
                    body += f' {servicio["servicio"]} | ${servicio["tarifa"]} COP\n'
            elif config == "descontratar":
                body += " # | SERVICIO DEL USUARIO \n"
                for pos, servicio in enumerate(data_copy):
                    body += f' {pos+1} | {servicio["servicio"]}\n'
        elif isinstance(config,list):
            if config[0] == "s&r&s":
                config[1] -= 1
                op = ["soporte", "reclamaciones", "sugerencias"]
                print(f">>>> Reportes de {op[config[1]].title()}")
                body += "ID REPORTE | DESCRIPCIÓN | ESTADO\n"
                if config[1] != 2:
                    if len(data_copy[op[config[1]]]["abiertas"]) != 0 or len(data_copy[op[config[1]]]["cerradas"]) != 0:
                        for tipo_reportes, lista_reportes in data_copy[op[config[1]]].items():
                            for reporte in lista_reportes:
                                body += f'{reporte["id"]} | {reporte["descripcion"]} | {tipo_reportes[:-1].capitalize()}\n'
                    else:
                        body += "[USUARIO SIN REPORTES]"
                else:
                    if len(data_copy[op[config[1]]]) != 0:
                        for reporte in data_copy[op[config[1]]]:
                            body += f'{reporte["id"]} | {reporte["descripcion"]}\n'
                    else:
                        body += "[USUARIO SIN REPORTES]"
            elif config[0] == "contratar":
                body += " # | SERVICIO | TARIFA ESTANDAR | TARIFA PERSONALIZADA\n"
                for pos, servicio in enumerate(data_copy):
                    body += f' {pos+1} | {servicio["servicio"]} | ${servicio["tarifa"]} COP | ${round((int(servicio["tarifa"])*config[1]-int(servicio["tarifa"]))*(-1))} COP (-%{config[1]*100}Dcto)\n'
        print(body)
        return body


def paginacion(structure_to_print, header, data_in_kwargs):
    start = 0
    pag_size = 5
    while True:
        end = start + pag_size
        print(header)
        if end > len(structure_to_print):
            end = len(structure_to_print)
        if start < 0:
            start = 0
        seccion = structure_to_print[start:end]
        current_page = ""
        for componente in seccion:
            line = ""
            if isinstance(structure_to_print,dict):
                line = " | ".join(list(componente.values())) + "\n"
            else:
                line = "".join(componente)
            current_page += line
        print(current_page)
        print(
            f"\t< {start} / {end} >\n[0 - Pagina anterior]    [1 - Pagina siguiente]\n[2 - Volver]")
        movimiento = int_val("> ", data_in_kwargs)
        if movimiento == 2:
            break
        elif movimiento == 1:
            start += pag_size
            if start > end:
                start -= pag_size
        elif movimiento == 0:
            if start != 0:
                start -= pag_size


def logica_gestiones(gestion, data_in_kwargs, var_data_is_finded=None, var_data_in_i=None, var_pos=None):
    if var_data_is_finded != 0:
        terminal = None
        if gestion == "usuarios":
            if var_data_is_finded[0]:
                while True:
                    terminal = mostrar_en_terminal(
                        var_data_in_i, es_paginado=False, config=gestion)
                    op = int_val("> ", data_in_kwargs,6)
                    if op == 0:
                        break
                    elif op >= 1 and op <= 5:
                        if op == 1 or op == 2 or op == 3:
                            res = menu_selector(usuarios.editar_perfil_usuario,una_opcion=True, continuar=True,op=op,data_in_kwargs=data_in_kwargs,pos_user=var_pos, contenido_terminal=terminal, op_externa=op, limitador=3)
                            if res == 0:
                                break
                        elif op == 4:
                            res = menu_selector(usuarios.editar_categoria,una_opcion=True,continuar=True, op_externa=op, data_in_kwargs=data_in_kwargs,pos_user=var_pos, limitador=4)
                            if res == 0:
                                break
                        elif op == 5:
                            usuarios.eliminar_usuario(data_in_kwargs,var_pos)
                            break
                    else:
                        reportes_txt("Opcion fuera de rango dentro de logica de gestiones",data_in_kwargs)
                        input(
                            "Seleccione una opcion dada\n[Enter - Reintentar]\n")
            else:
                reportes_txt("Intento de ingreso a perfil de usuario no creado",data_in_kwargs)
                input("Usuario sin perfil, inicie modulo de ventas para crear su perfil\n[Enter - Regresar]\n")
        elif gestion == "reportes":
            if var_data_is_finded[0]:
                while True:
                    mostrar_en_terminal(
                        var_data_in_i, es_paginado=False, config="reportes")
                    op_estructura = int_val("> ", data_in_kwargs, 7)
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
                        reportes_txt("Opcion fuera de rango dentro de logica de gestiones",data_in_kwargs)
                        input(
                            "Seleccione una opcion dada\n[Enter - Reintentar]\n")
        else:
            while True:
                mostrar_en_terminal(var_data_is_finded["servicios"],es_paginado=False, config="servicios")
                res = menu_selector(ventas.contratacion_descontratacion,ventas.historial_ventas,msg_op=10,contenido_terminal=True, data_in_kwargs=data_in_kwargs,)
                if res == 0:
                    break
    else:
        print("> Cancelando...")

def reportes_txt(msg,data_in_kwargs="main.py"):
    try:
        script_path = data_in_kwargs.get("script_path")
        current_route = script_path.replace("main.py", "reportes.txt")
        fecha = datetime.now()
        fecha = datetime.strftime(fecha,"%d/%m/%Y - %H:%M:%S")
        with open(current_route, "a",encoding="utf-8") as file:
            file.write(fecha + "Reporte - " + msg + "\n")
    except:
        current_route = data_in_kwargs.replace("main.py", "reportes.txt")
        fecha = datetime.now()
        fecha = datetime.strftime(fecha,"%d/%m/%Y - %H:%M:%S")
        with open(current_route, "a",encoding="utf-8") as file:
            file.write(fecha + " Reporte - " + msg + "\n")