import funciones_main
import usuarios
import reportes


# Formato docstring para copiar (esta linea no)
#     '''
#     ==> Recibe
#     <== Devuelve
#     '''


def navegador(data, ruta_script, cofiguracion):
    if cofiguracion == "principal":
        while True:
            op = funciones_main.int_val("> ", op_menu=2)
            if op >= 0 and op <= 3:
                if op == 0:
                    print("> Cerrando programa...")
                    break
                elif op == 1:
                    navegador(data, ruta_script, "usuarios")
                elif op == 2:
                    navegador(data, ruta_script, "reportes")
                elif op == 3:
                    navegador(data, ruta_script, "ventas")
            else:
                input(
                    "Opción no identificada\nIntente nuevamente\n(Enter para continuar)\n")
    elif cofiguracion == "usuarios":
        funciones_main.menu_selector(funciones_main.mostrar_en_terminal, usuarios.gestion_usuario,
                                     msg_op=3, db=data, mostrar_cofig=cofiguracion, script_path=ruta_script)
    elif cofiguracion == "reportes":
        funciones_main.menu_selector(funciones_main.mostrar_en_terminal, reportes.gestion_reporte,
                                     msg_op=4, db=data, mostrar_cofig=cofiguracion, script_path=ruta_script)
    elif cofiguracion == "ventas":
        return


ruta_actual = funciones_main.validar_ruta_main("> ")
json_path = funciones_main.validar_ruta_json(
    "Ingrese la ruta relativa del archivo de datos a procesar\n> ")
data = funciones_main.opener(json_path)
usuarios.actualizar_categoria_automatico(data, ruta_actual, "principal")
