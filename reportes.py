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


def gestion_reporte(data_in_kwargs):
    '''
    Realiza CRUDs a reportes en el json con la idea logica de un software para proveedor de servicios de telecomunicaciones
    ==> Recibe Diccionario
    <== Devuelve Diccionario
    '''
    print(">>> Gestionar un reporte")
    estructura = "reportes"
    report_is_finded = funciones_main.encontrar_en_bdd(
        data_in_kwargs, estructura)
    if report_is_finded != 0:
        report_in_i = report_is_finded[2]
        pos = report_is_finded[1]
        funciones_main.logica_gestiones(
            estructura, report_is_finded, report_in_i, pos, data_in_kwargs)

def agregar_reporte(data_in_kwargs):
    pos_report = data_in_kwargs.get("pos_report")
    op_estructura = data_in_kwargs.get("op_estructura")
    data_in_kwargs = data_in_kwargs.get("data_in_kwargs")
    formateo = ["soporte", "reclamaciones", "sugerencias"]
    id_usuario = data_in_kwargs["db"]["reportes"][pos_report]["id_usuario"]
    print(">>>> Agregando reporte")
    motivo = funciones_main.alpnum_val(f"Indique motivo por el cual el usuario ID {id_usuario} gestiona en: {formateo[op_estructura-1].capitalize()}\n> ")
    if op_estructura == 1 or op_estructura == 2:
        while True:
            resultado = funciones_main.int_val("¿Consiguio dar solucion al usuario?\n[1 - Si]   [2 - No]\n> ")
            if resultado >= 1 and resultado <= 2:
                id = funciones_main.generar_id(data_in_kwargs["db"]["reportes"][pos_report][formateo[op_estructura-1]],"reportes", id=id_usuario)
                reporte = {
                    "id": id,
                    "descripcion": motivo
                }
                if resultado == 1:
                    data_in_kwargs["db"]["reportes"][pos_report][formateo[op_estructura-1]]["cerradas"].append(reporte)
                else:
                    data_in_kwargs["db"]["reportes"][pos_report][formateo[op_estructura-1]]["abiertas"].append(reporte)
                data_in_kwargs["db"]["reportes"][pos_report]["Cantidad Reportes"] += 1
                break
            else:
                input("Ingrese opcion valida\n[Enter - Reintentar]\n")
    else:
        id = funciones_main.generar_id(data_in_kwargs["db"]["reportes"][pos_report][formateo[op_estructura-1]],"reportes",complejidad="sugerencias", id=id_usuario)
        reporte = {
            "id": id,
            "descripcion": motivo
        }
        data_in_kwargs["db"]["reportes"][pos_report][formateo[op_estructura-1]].append(reporte)
        data_in_kwargs["db"]["reportes"][pos_report]["Cantidad Reportes"] += 1
    funciones_main.export_file(data_in_kwargs,"exported_db")

def cerrar_reporte(data_in_kwargs):
    pos_report = data_in_kwargs.get("pos_report")
    op_estructura = data_in_kwargs.get("op_estructura")
    data_in_kwargs = data_in_kwargs.get("data_in_kwargs")
    formateo = ["soporte", "reclamaciones"]
    print(">>>> Cerrar reporte")
    while True:
        reportes = data_in_kwargs["db"]["reportes"][pos_report]
        id_objetivo = funciones_main.alpnum_val(f"Ingrese el ID especifico de '{formateo[op_estructura-1].capitalize()}' a la que dara cierre (ACCION IRREVERSIBLE / 'cancelar' para cancelar)\n> ")
        hecho = False
        if id_objetivo != "cancelar":
            for reporte_key,reporte_valor in reportes.items():
                if reporte_key == formateo[op_estructura-1]:
                    if hecho:
                        break
                    for estado, reportes in reporte_valor.items():
                        for pos_lista_tipo_reporte, reporte in enumerate(reportes):
                            if reporte["id"] == id_objetivo and estado == "abiertas":
                                reporte_valor["cerradas"].append(reporte)
                                reportes.pop(pos_lista_tipo_reporte)
                                print(f"Reporte {id_objetivo} cerrado satsifactoriamente...")
                                hecho = True
            if not hecho:
                input("Reporte no existe\n[Enter - Continuar]\n")
            funciones_main.export_file(data_in_kwargs,"exported_db")
        else:
            print("> Cancelando...")
            break




