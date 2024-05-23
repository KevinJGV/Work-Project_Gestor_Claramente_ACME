import json
import re
import datetime
# Formato docstring para copiar (esta linea no)
#     '''
#     ==> Recibe
#     <== Devuelve
#     '''


def int_val(msg,es_menu=None,op_menu=0):
    '''
    Validador de valor numerico
    ==> Recibe String
    <== Devuelve Numero entero
    '''
    while True:
        try:
            if es_menu is None:
                prompt = int(input(msg))
                return prompt
            else:
                msgs(op_menu)
                prompt = int(input(msg))
                return prompt
        except:
            input("Error de ingreso \nIntente nuevamente\n(Enter para continuar)\n")


def str_val(msg):
    '''
    Validador de tipo string
    ==> Recibe String
    <== Devuelve String
    '''
    while True:
        try:
            prompt = str(input(msg).strip())
            return prompt
        except:
            input("Error de ingreso, debe ser alfanumerico \nIntente nuevamente\n(Enter para continuar)")


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
                input("Ingrese un correo electronico valido\n[Enter - Reintentar]\n")
                email = str_val("> ")



def msgs(op):
    '''
    Visualizador de mensajes para el algoritmo
    ==> Recibe Numero entero
    '''
    try:
        if op == 0:
            print("Para inicializar ingrese la ruta relativa actual de este scprit 'main.py: ")
        elif op == 1:
            print("=" * 6 + " CLARAMENTE ACME - PROGRAMA GESTOR v1 " + "=" * 6 +
                "\nPara iniciar porfavor asegurese de tener un archivo .json con el cual trabajar.")
        elif op == 2:
            print("=" * 6 + " MENU PRINCIPAL " + "=" * 6 +
                "\n1 - Registro y Gestión de Usuarios\n2 - Reportes de usuarios\n3 - Personalización de Servicios\n4 - Gestión de las ventas\n0 - Salir")
        elif op == 3:
            print("\n>> Registro y Gestión de Usuarios\n1 - Visualizar todos los usuarios\n2 - Gestionar usuario\n0 - Volver")
        elif op == 4:
            print("\n>> Reportes de usuarios\n1 - Visualizar todos los reportes\n2 - Gestionar un reporte\n0 - Volver")
        elif op == 5:
            print("\n>> Reportes de usuarios\n1 - Visualizar todos los reportes\n2 - Gestionar un reporte\n0 - Volver")
        elif op == 9:
            print("\n(Enter, regresar)")
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
            ruta = str_val(msg)
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
        ruta = str_val(msg)
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


def menu_selector(*opcs, msg_op=None,**kwargs):
    '''
    Menu generico, recibe funciones y argumentos para estas como argumentos a las cuales se accede a solicitud del usuario 
    ==> Recibe (Argumentos de longitud variable, Argumentos de palabra clave)
    ==> Devuelve lo que devuelve la funcion señalada en ella
    '''
    resultado_menu = None
    while True:
        try:
            if msg_op is None:
                op = int_val("> ")
                if op == 0:
                    break
                elif op <= len(opcs):
                    return opcs[op-1](kwargs)
                else:
                    raise ValueError
            else:
                op = int_val("> ",es_menu=True,op_menu=msg_op)
                if op == 0:
                    return resultado_menu
                elif op <= len(opcs):
                    resultado_menu = opcs[op-1](kwargs)
                else:
                    raise ValueError
        except:
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

def encontrar_en_bdd(bdd,estructura):
    if estructura == "usuarios":
        while True:
            user_id = int_val("Ingresa ID existente para gestionar usuario o uno no registrado para crear perfil de usuario (0 - Cancelar)\n> ")
            if user_id != 0:
                user_is_finded = False
                for pos, user_in_i in enumerate(bdd):
                        if user_in_i["id"] == user_id:
                            user_is_finded = True
                            print("Usuario encontrado... Procesando...")
                            return [user_is_finded,pos, user_in_i]
                if not user_is_finded:
                    return [False,None,None]
            else:
                return 0
    elif estructura == "reportes":
        return "PENDIENTE"