# Elaborador por: Camilo Sánchez Rodríguez, Gabriel Gomez Vega
# Fecha de creación: 12/10/2021, 11:16 AM
# Última edición: XX/10/2021, XX:XX XX
# Versión: 3.9.6


# Template documentación funciones
"""
    Función:
    Entradas:
    Salidas:
    """

##############################################################
#####              Importación de Librerías              #####
##############################################################

import re

##############################################################
#####              Definición de Funciones               #####
##############################################################

def imprimirError(ptexto):
    """
    Función:    Muestra error a usuario antes de continuar el programa
    Entradas:   ptexto (str) - Mensaje de error
    Salidas:    Imprime título y mensaje de error
    """
    print("", "_"*50, "|" + "Error".center(48, ' ') + "|", "-"*50, sep="\n")
    print("\n" + ptexto.center(50, " ") + "\n")
    input("Continuar <ENTER>".center(50, " "))
    print("_"*50 + "\n")

def validarPaquete():
    """
    Función:    Valida entrada de número de paquete
    Entradas:   entrada (int) - Número entero
    Salidas:    Retorna entrada si es válida. De lo contrario, imprime error
    """
    while True:
        try:
            entrada = int(input("Número de paquete: "))
            if entrada > 0:
                return entrada
            imprimirError("Valor ingresado debe ser mayor a 0") # Restricción de Valor
        except ValueError:
            imprimirError("Debe ingresar un número entero") # Restricción de Tipo

def revisarPaquete(pnum, pdict):
    """
    Función:    Indica si número de paquete existe en diccionario
    Entradas:
        pnum (int) - Número de paquete
        pdict (dict) - Diccionario de paquetes
    Salidas:    Retorna True si está, False si no está
    """
    return pnum in pdict

def validarTelefono():
    """
    Función:    Valida entrada de número telefónico
    Entradas:   entrada (str) - Número de teléfono
    Salidas:    Retorna entrada si es válida. De lo contrario, imprime error
    """
    while True:
        entrada = input("Número de teléfono: ")
        if re.match("^\d{8}$", entrada):
            return entrada
        imprimirError("Formato inválido, ingrese 8 dígitos") # Restricción de Valor

##############################################################
#####                Programa Principal                  #####
##############################################################

paquetes = {0:[], 1:[], 2:[], 3:[]} # Diccionario de prueba, reemplazar por dict vació al final

