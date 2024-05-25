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
from funciones_main import mostrar_en_terminal

# Imports de gestion.py

from gestion import gestion_usuario
from gestion import agregar_usuario
from gestion import generar_id
from gestion import editar_perfil_usuario
from gestion import editar_categoria
from gestion import eliminar_usuario

# Imports de ventas.py

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


def generar_reporte(data_in_kwargs):
    '''
    Realiza CRUDs a reportes en el json con la idea logica de un software para proveedor de servicios de telecomunicaciones
    ==> Recibe Diccionario
    <== Devuelve Diccionario
    '''
    print(">>> Gestionar un reporte")
    report_pos_finded = encontrar_en_bdd(data_in_kwargs, "reportes")
    report_in_i = report_pos_finded[2]
    pos = report_pos_finded[1]
    if report_pos_finded != 0:
        if report_pos_finded[0]:
            while True:
                mostrar_en_terminal(report_in_i, es_paginado=False, config="reportes")