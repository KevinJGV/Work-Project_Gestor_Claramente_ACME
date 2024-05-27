import funciones_main
import usuarios
from datetime import datetime

# Formato docstring para copiar (esta linea no)
#     '''
#     ==> Recibe
#     <== Devuelve
#     '''

def contratacion_descontratacion(data_in_kwargs):
    print(">>>> Contratacion / Descontratacion de Servicio")
    data_in_kwargs = data_in_kwargs.get("data_in_kwargs")
    data_is_finded = funciones_main.encontrar_en_bdd(
            data_in_kwargs, "usuarios", alt="venta")
    if data_is_finded != 0:
        if data_is_finded[0] is not False:
            while True:
                datos_relevantes = data_is_finded[1:]
                funciones_main.mostrar_en_terminal(data_is_finded[2],es_paginado=False,config="usuarios")
                res = funciones_main.menu_selector(contratacion,descontratacion,msg_op=11, contenido_terminal= True,data_in_kwargs=data_in_kwargs, datos_relevantes=datos_relevantes)
                if res == 0:
                    break
        else:
            usuarios.agregar_usuario(data_in_kwargs,data_is_finded[1])


def contratacion(data_in_kwargs, proviene_agregar_usuario=False):
    print(">>>>> Contratacion de Servicio")
    if proviene_agregar_usuario is False:
        datos_relevantes = data_in_kwargs.get("datos_relevantes")
        data_in_kwargs = data_in_kwargs.get("data_in_kwargs")
        referencia_servicios = data_in_kwargs["db"]["ventas"]["servicios"]
        referencia_historial = data_in_kwargs["db"]["ventas"]["historial"]
        descuento = 0
        if len(datos_relevantes[1]["servicios"]) <= 3:
            if datos_relevantes[1]["categoria"] == "cliente nuevo":
                descuento = 0.5
            elif datos_relevantes[1]["categoria"] == "cliente regular":
                descuento = 0.3
            else:
                descuento = 0.15
        while True:
            funciones_main.mostrar_en_terminal(referencia_servicios,es_paginado=False, config=["contratar",descuento])
            print(f"PROMOTOR: Este usuario es {datos_relevantes[1]["categoria"]} y tiene menos de 3 servicios, obtendra un descuento del {round(descuento*100)}% en este maximo de servicios. !Informaselo!\n")
            op = funciones_main.int_val("> ",op_msg="input")
            if op == 0:
                break
            elif len(referencia_servicios) >= op and op >= 1:
                op -= 1
                fecha = datetime.now().date()
                fecha = datetime.strftime(fecha, "%d-%m-%Y")
                tarifa = str(round((int(referencia_servicios[op]["tarifa"])*descuento-int(referencia_servicios[op]["tarifa"]))*(-1)))
                servicio = {
                        "servicio": referencia_servicios[op]["servicio"],
                        "fecha": fecha,
                        "tarifa": tarifa
                    }
                datos_relevantes[1]["servicios"].append(servicio)
                historial = {
                    "fecha": fecha,
                    "venta": referencia_servicios[op]["servicio"]
                }
                referencia_historial.append(historial)
                input("Contratacion exitosa...\n[Enter - Continuar]")
                funciones_main.export_file(data_in_kwargs,"exported_db")
            else:
                print("ERROR, PENDIENTE DE REPORTE")
    else:
        referencia_servicios = data_in_kwargs["db"]["ventas"]["servicios"]
        referencia_historial = data_in_kwargs["db"]["ventas"]["historial"]
        descuento = 0.6
        funciones_main.mostrar_en_terminal(referencia_servicios,es_paginado=False, config=["contratar",descuento])
        print(f"PROMOTOR: Este usuario esta subscribiendose a Claro, obtendra un descuento del {round(descuento*100)}% en su primera contratacion. !Informaselo!\n")
        op = funciones_main.int_val("APARTIR DE AQUI LA CONTRATACION SE HARA EFECTIVA\nSelecciona una opcion para continuar (0 - Cancelar contratacion)\n> ",)
        if op == 0:
            return 0
        elif len(referencia_servicios) >= op and op >= 1:
            op -= 1
            fecha = proviene_agregar_usuario["antiguedad"]
            tarifa = str(round((int(referencia_servicios[op]["tarifa"])*descuento-int(referencia_servicios[op]["tarifa"]))*(-1)))
            servicio = {
                    "servicio": referencia_servicios[op]["servicio"],
                    "fecha": fecha,
                    "tarifa": tarifa
                }
            proviene_agregar_usuario["servicios"].append(servicio)
            historial = {
                "fecha": fecha,
                "venta": referencia_servicios[op]["servicio"]
            }
            referencia_historial.append(historial)


def descontratacion(data_in_kwargs):
    datos_relevantes = data_in_kwargs.get("datos_relevantes")
    data_in_kwargs = data_in_kwargs.get("data_in_kwargs")
    referencia_servicios = datos_relevantes[1]["servicios"]
    if len(referencia_servicios) != 0:
        print(">>>>> Descontratacion de Servicio")
        while True:
            funciones_main.mostrar_en_terminal(referencia_servicios,es_paginado=False, config="descontratar")
            op = funciones_main.int_val("> ",op_msg="input")
            if op == 0:
                break
            elif len(referencia_servicios) >= op and op >= 1:
                op -= 1
                confirmar = input("'BORRAR' para confirmar accion\n> ")
                if confirmar == "BORRAR":
                    referencia_servicios.pop(op)
                    print("Descontratacion efectuada...")
                    funciones_main.export_file(data_in_kwargs,"exported_db")
                    break
                else:
                    print("> Abortando...")
    else:
        print("Usuario sin servicios, modulo inaccesible")


def historial_ventas(data_in_kwargs):
    print(">>>> Visualizar historial de ventas")
    referencia_historial = data_in_kwargs.get("data_in_kwargs").get("db").get("ventas").get("historial")
    funciones_main.mostrar_en_terminal(referencia_historial,requiere_mostrar_config=False,config="historial")