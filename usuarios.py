import funciones_main
import reportes
import ventas

# Formato docstring para copiar (esta linea no)
#     '''
#     ==> Recibe
#     <== Devuelve
#     '''


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
        id = funciones_main.generar_id(unpacked_data,"usuarios")
        nombre = funciones_main.alpnum_val("Nombre del usuario: ")
        direccion = funciones_main.alpnum_val(
            "Direccion de domicilio del usuario: ")
        contacto = funciones_main.validar_email_regexp(
            input("Correo electronico del usuario: "), es_validado=True)

        return data_in_kwargs


def editar_perfil_usuario(data_in_kwargs):
    '''
    Edita informacion del usuario seleccionado previamente
    ==> Recibe Diccionario
    '''
    op = data_in_kwargs.get("op")
    pos_user = data_in_kwargs.get("pos_user")
    data_in_kwargs = data_in_kwargs.get("data_in_kwargs")
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
            nuevo_dato = funciones_main.alpnum_val(
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
            nuevo_dato = funciones_main.alpnum_val(
                f"Nuevo {op} de usuario ('cancelar' para Cancelar)\n> ")
            if funciones_main.validar_email_regexp(nuevo_dato) or nuevo_dato == "cancelar":
                break
            else:
                input(
                    "Ingrese un correo electronico valido\n[Enter - Reintentar]\n")
    if nuevo_dato.lower() == "cancelar":
        print("Cancelando...")
    else:
        data_in_kwargs["db"]["usuarios"][pos_user][op] = nuevo_dato
        funciones_main.export_file(data_in_kwargs, "exported_db")
        return data_in_kwargs


def editar_categoria(data_in_kwargs):
    '''
    Reasigna la categoria del usuario
    ==> Recibe Diccionario
    <== Devuelve Diccionario
    '''
    pos_user = data_in_kwargs.get("pos_user")
    data_in_kwargs = data_in_kwargs.get("data_in_kwargs")
    print(">>>> Modificando categoria de usuario\nATENCION: MODIFICAR SIN AUTORIZACION ESTE VALOR SIN AUTORIZACION ES SANCIONABLE, ASEGURESE DE TENER EL PERMISO DE SU COORDINADOR PARA ESTO.")
    yo = input("Continuar? (y/n) ")
    if yo == "y":
        while True:
            op = funciones_main.int_val(
                "[1 - Modificar a Cliente Nuevo]\n[2 - Modificar a Cliente Regular]\n[3 - Modificar a Cliente Leal]\n[0 - Cancelar]\n> ")
            if op >= 0 and op <= 3:
                if op != 0:
                    modificadores = ["cliente nuevo",
                                     "cliente regular", "cliente leal"]
                    data_in_kwargs["db"]["usuarios"][pos_user]["categoria"] = modificadores[op-1]
                    funciones_main.export_file(data_in_kwargs, "exported_db")
                    print(f"> Modificacion: {modificadores[op-1].title()}")
                    return data_in_kwargs
                else:
                    print("> Cancelando...")
                    break
            else:
                input(
                    "Seleccione opcion dentro del rango\n[Enter - Reintentar]")


def eliminar_usuario(data_in_kwargs):
    '''
    Elimina al usuario
    ==> Recibe Diccionario
    <== Devuelve Diccionario
    '''
    pos_user = data_in_kwargs.get("pos_user")
    data_in_kwargs = data_in_kwargs.get("data_in_kwargs")
    data = data_in_kwargs["db"]["usuarios"][pos_user]
    if len(data["servicios"]) == 0:
        op = input(
            "///////////////////////////\nEsta accion es irreversible\n///////////////////////////\n['BORRAR' para confirmar]\n[Cualquier otro ingreso para abortar]\n> ")
        if op == "BORRAR":
            data_in_kwargs["db"]["usuarios"].pop(pos_user)
            input("Usuario eliminado satisfactoriamente\n Gestion añadida al registro de movimientos. PENDIENTE AÑADIR FUNCIONALIDAD")
            funciones_main.export_file(data_in_kwargs, "exported_db")
            return data_in_kwargs
        else:
            print("> Cancelando...")
    else:
        input(
            "Accion no permitida.\nEl usuario seleccionado no debe tener servicios contradados. Se requiere descontratar todos los servicios.\n[Enter - Cancelar]\n")
