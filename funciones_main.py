import json

# Formato docstring para copiar (esta linea no)
#     '''
#     ==> Recibe
#     <== Devuelve
#     '''


def int_val(msg):
    '''
    Validador de valor numerico
    ==> Recibe String
    <== Devuelve Numero entero
    '''
    while True:
        try:
            prompt = int(input(msg))
            return prompt
        except:
            input("Error de ingreso \nIntente nuevamente\n(Enter para continuar)")


def msgs(op):
    '''
    Visualizador de mensajes para el algoritmo
    ==> Recibe Numero entero
    <== Devuelve None
    '''
    if op == 0:
        print("Para inicializar ingrese la ruta relativa actual de este scprit 'main.py: ")
    elif op == 1:
        print("=" * 6 + " CLARAMENTE ACME - PROGRAMA GESTOR v1 " + "=" * 6 +
              "\nPara iniciar porfavor asegurese de tener un archivo .json con el cual trabajar.")
    elif op == 2:
        print("=" * 6 + " MENU " + "=" * 6 +
              "\n1 - Registro y Gestión de Usuarios\n2 - Seguimiento del Historial de Usuarios\n3 - Personalización de Servicios\n4 - Gestión de las ventas\n0 - Salir")
    elif op == 3:
        print("\n(Enter, regresar)")


def validar_ruta_main(msg):
    '''
    Validador de archivo "main.py·
    ==> Recibe String
    <== Devuelve String
    '''
    while True:
        msgs(0)
        try:
            ruta = str(input(msg))
            if ruta.endswith("main.py"):
                return ruta
            else:
                raise ValueError
        except:
            input("Asegurese de que la ruta es del archivo 'main.py'. \nIntente nuevamente\n(Enter para continuar)")


def validar_ruta_json():
    '''   Validador de ruta y formato .json de archivo
    <== Devuelve Str
    '''
    msgs(1)
    while True:
        ruta = str(
            input("> Ingrese la ruta relativa del archivo de datos a procesar: "))
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


def menu_selector(*opcs, **kwargs):
    '''
    Menu generico, recibe funciones y argumentos para estas como argumentos a las cuales se accede a solicitud del usuario 
    ==> Recibe (Argumentos de longitud variable, Argumentos de palabra clave)
    <== Devuelve None
    '''
    msgs(2)
    while True:
        try:
            op = int_val("> ")
            if op == 0:
                break
            elif op <= len(opcs):
                opcs[op-1](kwargs)
            else:
                raise ValueError
        except:
            input("Ingrese valor valido. \nIntente nuevamente\n(Enter para continuar)")
