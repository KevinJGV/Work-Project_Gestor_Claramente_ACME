from funciones_main import *
from imports_gestion import *
from imports_reportes import *
from imports_ventas import *

ruta_actual = validar_ruta_main("> ")
json_path = validar_ruta_json("Ingrese la ruta relativa del archivo de datos a procesar\n> ")
data = opener(json_path)
menu_selector(gestiones,reportes,msg_op=2,db=data,script_path=ruta_actual)