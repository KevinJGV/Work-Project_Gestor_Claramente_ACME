from gestion import *
from reportes import *
from ventas import *


ruta_actual = validar_ruta_main("> ")
json_path = validar_ruta_json()
data = opener(json_path)
funcionejemplo = ""

menu_selector(funcionejemplo,db=data)