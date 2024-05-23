from funciones_main import *
from imports_gestion import *

# Formato docstring para copiar (esta linea no)
#     '''
#     ==> Recibe
#     <== Devuelve
#     '''

def reportes(data_in_kwargs):
    '''
    Funcion para dar como argumento de longitud variable a funcion Menu_selector()
    ==> Recibe Diccionario
    <== Devuelve Diccionario
    '''
    encontrar_en_bdd()
    res = menu_selector(mostrar_usuario_s, gestion_usuario,msg_op=3, db=data_in_kwargs)
    return res