# Imports de funciones_main.py

from funciones_main import int_val
from funciones_main import str_val
from funciones_main import validar_email_regexp
from funciones_main import msgs
from funciones_main import validar_ruta_main
from funciones_main import validar_ruta_json
from funciones_main import opener
from funciones_main import menu_selector
from funciones_main import export_file
from funciones_main import encontrar_en_bdd

# Imports librerias

import json
import re
import datetime
import copy

# Formato docstring para copiar (esta linea no)
#     '''
#     ==> Recibe
#     <== Devuelve
#     '''


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
        elif config == "usuarios":
            print(">>> Visualizar todos los usuarios")
            users_data = data_copy.get("db").get("usuarios")
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
        elif config == "reportes":
            return
    else:
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
            return


def gestion_usuario(data_in_kwargs):
    '''
    Realiza CRUDs en el json con la idea logica de un software para proveedor de servicios de telecomunicaciones
    ==> Recibe Diccionario
    <== Devuelve Diccionario
    '''
    print(">>> Gestionar usuario")
    user_is_finded = encontrar_en_bdd(data_in_kwargs, "usuarios")
    user_in_i = user_is_finded[2]
    pos = user_is_finded[1]
    if user_is_finded != 0:
        if user_is_finded[0]:
            while True:
                mostrar_en_terminal(
                    user_in_i, es_paginado=False, config="usuarios")
                op = int_val("[1 - Editar Nombre]   [2 - Editar direccion]   [3 - Editar contacto]   [4 - Editar categoria manualmente -NO RECOMENDADO]\n[5 - Contratar/Descontratar Servicio]   [6 - ELIMINAR USUARIO]   [0 - Cancelar]\n> ")
                if op >= 0 and op <= 6:
                    if op == 1 or op == 2 or op == 3:
                        res = editar_perfil_usuario(op, data_in_kwargs, pos)
                        if res is not None:
                            data_in_kwargs = res
                            continuar = int_val(
                                "¿Desea continuar gestionando al usuario?\n1 - Continuar    2 - Salir\n> ")
                            if continuar == 2:
                                break
                    elif op == 4:
                        res = editar_categoria(data_in_kwargs, pos)
                        if res is not None:
                            data_in_kwargs = res
                            continuar = int_val(
                                "¿Desea continuar gestionando al usuario?\n1 - Continuar    2 - Salir\n> ")
                            if continuar == 2:
                                break
                    elif op == 5:
                        print("funcionalidad_en_desarrollo")
                    elif op == 6:
                        eliminar_usuario(data_in_kwargs, pos)
                        break
                    else:
                        break
                else:
                    input("Seleccione una opcion dada\n[Enter - Reintentar]\n")
        else:
            res = agregar_usuario(data_in_kwargs)
            if res is not None:
                data_in_kwargs = res
        return data_in_kwargs
    else:
        print("> Cancelando...")


def agregar_usuario(data_in_kwargs):
    '''
    Agrega un usuario a la bdd
    ==> Recibe Diccionario
    <== Devuelve Diccionario
    '''
    input("SE EJECUTA EL MODULO DE VENTAS, PENDIENTE\nAgregar usuario incompleto")
    print(">>>> Agregando usuario a base de datos")
    unpacked_data = data_in_kwargs.get("db").get("usuarios")
    servicios = ""
    if servicios is not None:
        user_to_fill = {}
        id = generar_id(unpacked_data)
        nombre = str_val("Nombre del usuario: ")
        direccion = str_val("Direccion de domicilio del usuario: ")
        contacto = validar_email_regexp(
            input("Correo electronico del usuario: "), es_validado=True)

        return data_in_kwargs


def generar_id(data):
    '''
    Funcion auxiliar de agregar_usuario
    ==> Recibe Diccionario
    <== Devuelve Diccionario
    '''
    ids = [user["id"] for user in data]
    id = 1
    while True:
        if id not in ids:
            return id
        else:
            id += 1


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
            nuevo_dato = str_val(
                f"Nuevo {op} de usuario ('cancelar' para Cancelar)\n> ")
            if nuevo_dato == "cancelar":
                print("> Cancelar")
                break
            try:
                int(nuevo_dato)
                input(
                    f"{op.title()} debe ser alfanumerico\n[Enter - Reintentar]\n")
            except:
                break
    else:
        while True:
            nuevo_dato = str_val(
                f"Nuevo {op} de usuario ('cancelar' para Cancelar)\n> ")
            if validar_email_regexp(nuevo_dato) or nuevo_dato == "cancelar":
                break
            else:
                input(
                    "Ingrese un correo electronico valido\n[Enter - Reintentar]\n")
    if nuevo_dato.lower() == "cancelar":
        print("Cancelando...")
    else:
        data_in_kwargs["db"]["usuarios"][pos_user][op] = nuevo_dato
        export_file(data_in_kwargs, "exported_db")
        return data_in_kwargs


def editar_categoria(data_in_kwargs, pos_user):
    '''
    Reasigna la categoria del usuario
    ==> Recibe Diccionario
    <== Devuelve Diccionario
    '''
    print(">>>> Modificando categoria de usuario\nATENCION: MODIFICAR SIN AUTORIZACION ESTE VALOR SIN AUTORIZACION ES SANCIONABLE, ASEGURESE DE TENER EL PERMISO DE SU COORDINADOR PARA ESTO.")
    yo = input("Continuar? (y/n) ")
    if yo == "y":
        while True:
            op = int_val(
                "[1 - Modificar a Cliente Nuevo]\n[2 - Modificar a Cliente Regular]\n[3 - Modificar a Cliente Leal]\n[0 - Cancelar]\n> ")
            if op >= 0 and op <= 3:
                if op != 0:
                    modificadores = ["cliente nuevo",
                                     "cliente regular", "cliente leal"]
                    data_in_kwargs["db"]["usuarios"][pos_user]["categoria"] = modificadores[op-1]
                    export_file(data_in_kwargs, "exported_db")
                    print(f"> Modificacion: {modificadores[op-1].title()}")
                    return data_in_kwargs
                else:
                    print("> Cancelando...")
                    break
            else:
                input(
                    "Seleccione opcion dentro del rango\n[Enter - Reintentar]")


def eliminar_usuario(data_in_kwargs, pos_user):
    '''
    Elimina al usuario
    ==> Recibe Diccionario
    <== Devuelve Diccionario
    '''
    data = data_in_kwargs["db"]["usuarios"][pos_user]
    if len(data["servicios"]) == 0:
        op = input(
            "///////////////////////////\nEsta accion es irreversible\n///////////////////////////\n['BORRAR' para confirmar]\n[Cualquier otro ingreso para abortar]\n> ")
        if op == "BORRAR":
            data_in_kwargs["db"]["usuarios"].pop(pos_user)
            input("Usuario eliminado satisfactoriamente\n Gestion añadida al registro de movimientos. PENDIENTE AÑADIR FUNCIONALIDAD")
            export_file(data_in_kwargs, "exported_db")
            return data_in_kwargs
        else:
            print("> Cancelando...")
    else:
        input(
            "Accion no permitida.\nEl usuario seleccionado no debe tener servicios contradados. Se requiere descontratar todos los servicios.\n[Enter - Cancelar]\n")
