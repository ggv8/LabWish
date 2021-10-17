# Elaborador por: Camilo Sánchez Rodríguez, Gabriel Gomez Vega
# Fecha de creación: 12/10/2021, 11:16 AM
# Última edición: XX/10/2021, XX:XX XX
# Versión: 3.9.6

##############################################################
#####              Importación de Librerías              #####
##############################################################

import pickle

##############################################################
#####              Definición de Funciones               #####
##############################################################

def cargarBD():
    """
    Función:    Verifica si existe Base de Datos previa
    Entradas:   N/A
    Salidas:    Retorna contenidos de BD. De lo contrario, retorna {}
    """
    try:
        file = open('wishBD', 'rb')
        contenido = pickle.load(file)
        file.close()
        return contenido
    except (EOFError, FileNotFoundError): # None indica BD no existente o vacía
        return {}

def guardarBD(pcontenido):
    """
    Función:    Guarda contenido en archivo binario
    Entradas:   N/A
    Salidas:    N/A
    """
    file = open('wishBD', 'wb')
    pickle.dump(pcontenido, file)
    file.close()
    return ""