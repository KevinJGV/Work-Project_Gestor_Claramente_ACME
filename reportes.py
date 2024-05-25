import funciones_main
import usuarios
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


def generar_reporte(data_in_kwargs):
    '''
    Realiza CRUDs a reportes en el json con la idea logica de un software para proveedor de servicios de telecomunicaciones
    ==> Recibe Diccionario
    <== Devuelve Diccionario
    '''
    print(">>> Gestionar un reporte")
    report_is_finded = funciones_main.encontrar_en_bdd(
        data_in_kwargs, "reportes")
    report_in_i = report_is_finded[2]
    pos = report_is_finded[1]
    funciones_main.logica_gestiones(
        "usuarios", report_is_finded, report_in_i, pos, data_in_kwargs)
