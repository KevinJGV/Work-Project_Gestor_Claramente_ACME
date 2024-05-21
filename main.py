from funciones_main import *
from imports_gestion import *
from imports_gestion import *
from imports_gestion import *

ruta_actual = validar_ruta_main("> ")
json_path = validar_ruta_json("Ingrese la ruta relativa del archivo de datos a procesar\n> ")
data = opener(json_path)
msgs(2)
menu_selector(gestiones,db=data,script_path=ruta_actual)