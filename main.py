import funciones_main
import usuarios
import reportes
import ventas

# Formato docstring para copiar (esta linea no)
#     '''
#     ==> Recibe
#     <== Devuelve
#     '''

ruta_actual = funciones_main.validar_ruta_main("> ")
json_path = funciones_main.validar_ruta_json(
    "Ingrese la ruta relativa del archivo de datos a procesar\n> ", ruta_actual)
data = funciones_main.opener(json_path)
usuarios.actualizar_categoria_automatico(data,json_path)
funciones_main.menu_selector(funciones_main.gestor, una_opcion=True,msg_op=2, limitador=3,envia_op=True, db=data, script_path=ruta_actual)
