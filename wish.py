# Elaborador por: Camilo Sánchez Rodríguez, Gabriel Gomez Vega
# Fecha de creación: 12/10/2021, 11:16 AM
# Última edición: XX/10/2021, XX:XX XX
# Versión: 3.9.6
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
    return opcion[1]