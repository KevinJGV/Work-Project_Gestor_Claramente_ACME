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
    res = menu_selector(mostrar_usuario_s, gestion_usuario, db=unpacked_data)
    msgs(2)
    return res

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
            print(f"\t< {start} / {end} >\n[0 - Pagina anterior]    [1 - Pagina siguiente]\n[2 - Volver]")
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
            print(f"-> {servicio['servicio']}")

def gestion_usuario(data_in_kwargs):
    print(">>> Gestionar usuario")
    data_in_kwargs = data_in_kwargs.get("db")
    unpacked_data = data_in_kwargs.get("usuarios")
    while True:
        user_id = int_val("Ingresa ID existente para gestionar usuario o uno no registrado para crear perfil de usuario (0 - Cancelar)\n> ")
        if user_id != 0:
            for pos, user_in_i in enumerate(unpacked_data):
                if user_in_i["id"] == user_id:
                    print("Usuario encontrado... Procesando...")
                    while True:
                        mostrar_usuario_s(user_in_i, es_paginado=False)
                        op = int_val("[1 - Editar Nombre]   [2 - Editar direccion]   [3 - Editar contacto]   [4 - Editar categoria manualmente -NO RECOMENDADO]\n[5 - Contratar/Descontratar Servicio]   [6 - ELIMINAR USUARIO]   [0 - Cancelar]\n> ")
                        if op >= 0 and op <= 6:
                            if op == 1 or op == 2 or op == 3:
                                res = editar_perfil_usuario(op, data_in_kwargs, pos)
                                if res is not None:
                                    data_in_kwargs = res
                                    continuar = int_val("¿Desea continuar gestionando al usuario?\n 1 - Continuar    2 - Salir")
                                    if continuar == 2:
                                        break
                            elif op == 4:
                                print("funcionalidad_en_desarrollo")
                            elif op == 5:
                                print("funcionalidad_en_desarrollo")
                            elif op == 6:
                                res = eliminar_usuario(data_in_kwargs,user_id)
                                if res is not None:
                                    data_in_kwargs = res
                                break
                            else:
                                break
                        else:
                            input("Seleccione una opcion dada\n[Enter - Reintentar]")
                    break
            input("ID no encontrada\n(Enter para reintentar)")
        else:
            break
    msgs(3)

def editar_perfil_usuario(op, data_in_kwargs, pos_user):
    '''
    Edita informacion del usuario seleccionado previamente
    ==> Recibe Diccionario
    '''
    if op == 1:
        op = "nombre"
    elif op == 2:
        op = "dirección"
    elif op == 3:
        op = "contacto"
    print(f">>>> Editando {op} de usuario")
    nuevo_dato = None
    if op != "contacto":
        while True:
            nuevo_dato = str_val(f"Nuevo {op} de usuario ('cancelar' para Cancelar)\n> ")
            if nuevo_dato == "cancelar":
                print("> Cancelar")
                break
            try:
                int(nuevo_dato)
                input(f"{op.title()} debe ser alfanumerico\n[Enter - Reintentar]")
            except:
                break                
    else:
        while True:
            nuevo_dato = str_val(f"Nuevo {op} de usuario ('cancelar' para Cancelar)\n> ")
            if validar_email_regexp(nuevo_dato) or nuevo_dato == "cancelar":
                break
            else:
                input("Ingrese un correo electronico valido\n[Enter - Reintentar]")
    if nuevo_dato.lower() == "cancelar":
        print("Cancelando...")
    else:
        data_in_kwargs["db"]["usuarios"][pos_user][op] = nuevo_dato
        export_file(data_in_kwargs, "exported_db")
        return data_in_kwargs

def eliminar_usuario(data_in_kwargs,pos_user):
    data = data_in_kwargs["db"]["usuarios"][pos_user]
    if len(data["servicios"]) == 0:
        print("Esta accion es irreversible\n- 'BORRAR' para conituar\n- Cualquier otro ingreso para abortar")
        op = str(input("> "))
        if op == "BORRAR":
            data_in_kwargs["db"]["usuarios"][pos_user].pop()
            input("Usuario eliminado satisfactoriamente\n Gestion añadida al registro de movimientos. PENDIENTE AÑADIR FUNCIONALIDAD")
            export_file(data_in_kwargs, "exported_db")
            return data_in_kwargs
    else:
        input("Accion no permitida.\nEl usuario seleccionado no debe tener servicios contradados. Se requiere descontratar todos los servicios. [Enter - Cancelar]")