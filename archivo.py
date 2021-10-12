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

def buscarBD():
    """
    Función:    Verifica si existe Base de Datos previa
    Entradas:   N/A
    Salidas:    Retorna contenidos BD. Si no, pide datos para crear BD
    """
    try:
        print("\n" + "Cargando base de datos...".center(50, " "))
        file = open('PaquetesBD', 'rb')
        contenido = pickle.load(file)
        file.close()
        return contenido
    except EOFError:            # Restricción: Base de Datos nula
        print("\n" + "Error: Base de datos se encuentra vacía".center(50, " "))
    except FileNotFoundError:   # Restricción: BD no encontrada o no existe
        print("\n" + "No existe base de datos. Generando base de datos nueva...".center(50, " "))
    return {}   # En caso de error, genera Base de Datos nueva

def guardarBD(pregistro):
    """
    Función:    Guarda cambios realizados en archivo
    Entradas:   pregistro (list) - Lista de datos tras cambios
    Salidas:    Imprime mensaje confirmando que se han guardado cambios
    """
    file = open('PaquetesBD', 'wb')
    pickle.dump(pregistro, file)
    file.close()
    print("\n" + "Base de datos actualizada.".center(50, " ") + "\n")
    input("Continuar <ENTER>".center(50," "))
    return