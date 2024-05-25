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
    report_pos_finded = encontrar_en_bdd(data_in_kwargs, "reportes")
    report_in_i = report_pos_finded[2]
    pos = report_pos_finded[1]
    if report_pos_finded != 0:
        if report_pos_finded[0]:
            while True:
                mostrar_en_terminal(report_in_i, es_paginado=False, config="reportes")