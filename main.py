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

# Imports de gestion.py

from gestion import mostrar_en_terminal
from gestion import gestion_usuario
from gestion import agregar_usuario
from gestion import generar_id
from gestion import editar_perfil_usuario
from gestion import editar_categoria
from gestion import eliminar_usuario

# Imports de reportes.py

# Imports de ventas.py

# Imports librerias

import json
import re
import datetime
import copy


def navegador(data, ruta_script, cofiguracion):
    if cofiguracion == "principal":
        while True:
            op = int_val("> ", op_menu=2)
            if op >= 0 and op <= 3:
                if op == 0:
                    print("> Cerrando programa...")
                    break
                elif op == 1:
                    navegador(data, ruta_script, "gestiones")
                elif op == 2:
                    navegador(data, ruta_script, "reportes")
                elif op == 3:
                    navegador(data, ruta_script, "ventas")
            else:
                input("Opción no identificada\nIntente nuevamente\n(Enter para continuar)\n")
    elif cofiguracion == "gestiones":
        menu_selector(mostrar_en_terminal, gestion_usuario,
                            msg_op=3, db=data, mostrar_cofig="usuarios", script_path=ruta_script)
    elif cofiguracion == "reportes":
        return
    elif cofiguracion == "ventas":
        return


ruta_actual = validar_ruta_main("> ")
json_path = validar_ruta_json(
    "Ingrese la ruta relativa del archivo de datos a procesar\n> ")
data = opener(json_path)
navegador(data, ruta_actual, "principal")
