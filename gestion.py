from funciones_main import *
from imports_reportes import *


# Formato docstring para copiar (esta linea no)
#     '''
#     ==> Recibe
#     <== Devuelve
#     '''

def gestiones(data_in_kwargs):
    '''
    Funcion para dar como argumento de longitud variable a funcion Menu_selector()
    ==> Recibe Argumentos de palabra clave
    '''
    unpacked_data = data_in_kwargs.get("db")
    msgs(3)
    menu_selector(mostrar_usuario_s, gestion_usuario, db=unpacked_data)
    msgs(2)

def mostrar_usuario_s(data_in_kwargs, es_paginado=True):
    '''
    Muestra en consola el contenido .json paginadamente por defecto
    ==> Recibe Diccionario
    '''
    if es_paginado:
        print(">>> Visualizar todos los usuarios")
        unpacked_data = data_in_kwargs.get("db")
        users_data = unpacked_data["usuarios"]
        keys = [key.upper() for key in users_data[0].keys()]
        header = " | ".join(keys) + "\n"
        for pos, user in enumerate(users_data):
            users_data[pos]["id"] = str(user["id"])
            users_data[pos]["servicios"] = str(len(user["servicios"]))
        start = 0
        pag_size = 5
        while True:
            end = start + pag_size
            print(header)
            if end > len(users_data):
                end = len(users_data)
            if start < 0:
                start = 0
            seccion = users_data[start:end]
            current_page = ""
            for dic in seccion:
                line = " | ".join(list(dic.values())) + "\n"
                current_page += line
            print(current_page)
            print(f"\t< {
                start} / {end} >\n[0 - Pagina anterior]    [1 - Pagina siguiente]\n[2 - Volver]")
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
        msgs(3)
    else:
        keys = list(data_in_kwargs.keys())
        for key in keys:
            if key != "servicios":
                print(f"{key.upper()} => {data_in_kwargs[key]}")
        print("SERVICIOS ACTUALES DEL USUARIO:")
        for servicio in data_in_kwargs["servicios"]:
            print(f"-> {servicio["servicio"]}")

def gestion_usuario(data_in_kwargs):
    print(">>> Gestionar usuario")
    unpacked_data = data_in_kwargs.get("db")
    user_id = int_val("Ingresa ID existente para gestionar usuario o uno no registrado para crear perfil de usuario (0 - Cancelar)\n> ")
    while True:
        if user_id != 0:
            user = None
            for user_in_i in unpacked_data:
                if user_in_i["id"] == user_id:
                    user = user_in_i
                    break
            if user is not None:
                while True:
                    mostrar_usuario_s(user, es_paginado=False)
                    op = int_val("[1 - Editar Nombre]   [2 - Editar direccion]   [3 - Editar contacto]   [4 - Editar categoria manualmente -NO RECOMENDADO]\n[5 - Contratar/Descontratar Servicio]   [6 - ELIMINAR USUARIO]   [0 - Cancelar]")
                    if op >= 0 and op <= 6:
                        if op != 5 or op != 6 or op != 0:
                            menu_selector(editar_perfil_usuario,es_recursivo=True, db=user, key=op)
                            continuar = int_val("¿Desea continuar gestionando al usuario?\n 1 - Continuar    2 - Salir")
                            if continuar == 2:
                                break
                        else:
                            if op == 5:
                                funcionalidad_en_desarrollo()
                            else:
                                funcionalidad_en_desarrollo()
                    else:
                        input("Seleccione una opcion dada\n[Enter - Reintentar]")

            else:
                input("ID no encontrada\n(Enter para reintentar)")
        else:
            break
    msgs(3)

def editar_perfil_usuario(data_in_kwargs):
    '''
    Edita informacion del usuario seleccionado previamente
    ==> Recibe Diccionario
    '''
    unpacked_key = data_in_kwargs.get("key")
    unpacked_data = data_in_kwargs.get("db")
    if unpacked_key == 1:
        unpacked_key = "nombre"
    elif unpacked_key == 2:
        unpacked_key = "dirección"
    elif unpacked_key == 3:
        unpacked_key = "contacto"
    elif unpacked_key == 4:
        unpacked_key = "categoria"
    print(f">>>> Editando {unpacked_key} de usuario")
    nuevo_dato = None
    if unpacked_key != "contacto":
        nuevo_dato = str_val(f"Nuevo {unpacked_key} de usuario ('cancelar' para Cancelar)\n> ")
    else:
        while True:
            nuevo_dato = str_val(f"Nuevo {unpacked_key} de usuario ('cancelar' para Cancelar)\n> ")
            if validar_email_regexp(nuevo_dato) or nuevo_dato == "cancelar":
                break
            else:
                input("Ingrese un correo electronico valido\n[Enter - Reintentar]")
    if nuevo_dato.lower() == "cancelar":
        print("> Cancelando...")
    else:
        unpacked_data[unpacked_key] = nuevo_dato