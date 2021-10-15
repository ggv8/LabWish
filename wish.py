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
from funciones import *
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
    return ""

def validarNombreSucursal(pnombre):
    """
    Funcionamiento: Determina si el valor ingresado coincide con el formato de nombre de sucursal, no permite números
    Entradas:
    pnombre(str): Es el nombre a verificar si cumple con el formato
    Salidas: Una tupla (True, pnombre) o un str indicando error
    """
    if re.match("^[a-zA-ZáéíóúÁÉÍÓÚ '-]{6,}$", pnombre):
        return (True, pnombre)
    print("El nombre de la sucursal no debe tener signos de puntuación o números, y debe tener más de 5 caracteres; por ejemplo: \"CCR Cartago Centro\".")
    return " "

def pedirNombreSucursal():
    """
    Funcionamiento: Pide la entrada de la funcion validarNombreSucursal
    Entradas: Na
    Salidas: retorna la función validarNombreSucursal
    """
    vnombre = input("Ingrese el nombre de la sucursal: ")
    return validarNombreSucursal(vnombre)

def insistirNombreSucursal():
    """
    Funcionamiento: De manera repetitiva, pide un formato de nombre de sucursal hasta que esté correcto
    Entradas: Na
    Salidas:
    opcion[1](str): Equivale al nombre del con el formato correcto
    """
    opcion = " "
    while opcion[0] != True:
        opcion = pedirNombreSucursal()
    return opcion[1]

def validarEstadoPaquete(pnum):
    """
    Funcionamiento: Valida que el estado del paquete tenga un formato correcto
    Entradas:
    -pnum(str): es el numero que indica el estado
    Salidas: Una tupla; (True, pnum), o un str vacío
    """
    if re.match("^[1-3]$",pnum):
        return (True, pnum)
    print("Por favor ingrese un número entre (1) y (3)")
    return " "

def pedirEstadoPaquete():
    """
    Funcionamiento: Toma la entrada para la funcion validarEstadoPaquete
    Entrada:
    -pnum(str): Na
    Salidas: Retorna la funcion validarEstadoPaquete
    """
    vestado = input("Ingrese el estado del paquete: ")
    return validarEstadoPaquete(vestado)

def opcionInsistirEstadoPaquete():
    """
    Funcionamienot: Insiste al usuario hasta que ingrese un formato de estado correcto
    Entradas: na
    Salidas: 
    -opcion[1](str): Es el estado del paquete
    """
    opcion = " "
    while opcion[0] != True:
        opcion = pedirEstadoPaquete()
    return int(opcion[1])

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
##########################################################################################################
def cantidadPaquetes(ppaquetes):
    """
    Funcionamiento: Imprime la cantidad de paquetes que hay en el diccionario
    Entradas:
    -ppaquetes(int): es el número de paquetes
    Salidas: Na
    """
    return f"El total de paquetes registrados es: {ppaquetes}"

def imprimirBasePaquetes(pbasePaquete):
    """
    Funcionamiento: Imprime todos los paquetes que estén almacenados en la base
    Entradas:
    -pbasePaquete(dict): es el diccionario con todos los paquetes
    Salidas: Na
    """
    lineas = "-"*140 #Esto es para no hacer la multiplicación varias veces
    print(lineas+ "\n" + agregarEspacios("Número de paquete", 35) + agregarEspacios("Número de teléfono", 35) + agregarEspacios("Sucursal", 30) + agregarEspacios("Días hábiles", 25) + agregarEspacios("Estado", 15) + "\n" + lineas)
    for llave in sacarLlavesDicc(pbasePaquete):
        print(agregarEspacios(str(llave), 35) + agregarEspacios(str(pbasePaquete[llave][0]), 35) + agregarEspacios(pbasePaquete[llave][1], 30) + agregarEspacios(str(pbasePaquete[llave][2]), 25) + agregarEspacios(str(pbasePaquete[llave][-1]), 15) + "\n" + lineas)
    return ""

def menuReportes(plargoDiccionario, pbaseDiccionario):
    while True:
        """
        Funcionamiento: Es el menú de reportes
        Entradas:
        -plargoDiccionario(int): Es la cantidad de elementos que tiene el diccionario
        -pabseDiccionario(dict): Es el diccionario que tiene los paquetes
        Salidas: Na
        """
        print("\nMenú de reportes"
        "\n1. Total de paquetes registrados."
        "\n2. Imprimir todos los paquetes."
        "\n3. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            cantidadPaquetes(plargoDiccionario)
        elif opcion == "2":
            imprimirBasePaquetes(pbaseDiccionario)
        elif opcion == "3":
            break
        else:
            imprimirError("Se debe ingresar un número del (1) al (3).")
    print("Regresando al menú principal...")
    return ""

def validarMenuReportes(pbaseDiccionario):
    """
    Funcionamiento: Valida la entrada al menu de reportes
    Entradas: 
    -pbaseDiccionario(dict): Es el diccionario a evaluar
    Salidas: Retorna la funcion menuReportes
    """
    largoDiccionario = len(pbaseDiccionario)
    if largoDiccionario > 0:
        return menuReportes(largoDiccionario, pbaseDiccionario)
    imprimirError("Todavía no se ha insertado ningún paquete")
    return ""
##############################################################
#####                Programa Principal                  #####
##############################################################

paquetes = {0:[], 1:[], 2:[], 3:[]} # Diccionario de prueba, reemplazar por dict vació al final

diccionario = {244: ["12345678", "Cartago", "10", "2"], 5:["88888888", "San José", "3", "1"], -2:["22222222", "limón", "1", "1"]}
print(validarMenuReportes(diccionario))