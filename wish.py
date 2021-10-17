# Elaborador por: Camilo Sánchez Rodríguez, Gabriel Gomez Vega
# Fecha de creación: 12/10/2021, 11:16 AM
# Última edición: 16/10/2021, 11:03 PM
# Versión: 3.9.6

##############################################################
#####              Importación de Librerías              #####
##############################################################

import re
from archivo import *
from funciones import *

##############################################################
#####                 Variables Globales                 #####
##############################################################

paquetes = cargarBD()

##############################################################
#####              Definición de Funciones               #####
##############################################################

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

def ingresarPaquete():
    """
    Función:    Submenú de entradas requeridas para registrar datos
    Entradas:   paquetes (dict) - Diccionario de paquetes
    Salidas:    Retorna registro de datos
    """
    while True:
        print("\n" + " Registro de Datos ".center(50,"=") + "\n")
        numero = validarPaquete()
        if revisarPaquete(numero, paquetes):   # Restriccion: Paquete repetido
            imprimirError("No se puede repetir número de paquete")
            continue
        telefono, sucursal = validarTelefono(), insistirNombreSucursal()
        estado = opcionInsistirEstadoPaquete()
        dias = 10
        if estado != '1':   # Si estado es 2 o 3, cambia dias hábiles a 0
            dias = 0
        paquetes[numero] = [telefono, sucursal, dias, estado] # Crea paquete nuevo
        if not confirmarOpcion("", "¿Desea ingresar más paquetes?"):
            break   # Cierra submenu
    return paquetes

def actualizarPaquete():
    """
    Función:    Submenú de entradas requeridas para actualizar datos
    Entradas:   paquetes (dict) - Diccionario de paquetes
    Salidas:    Retorna registro de datos
    """
    while True:
        print("\n" + " Modificación de Datos ".center(50,"=") + "\n")
        numero = validarPaquete()
        if not revisarPaquete(numero, paquetes): # Restriccion: Paquete no registrado
            imprimirError("No se encuentra registrado el paquete")
            continue
        estado = opcionInsistirEstadoPaquete()
        if estado == paquetes[numero][-1]:     # Restricción: Estado ya registrado
            imprimirError("El paquete ya tiene ese estado registrado")
            continue
        if confirmarOpcion(" ADVERTENCIA ", "¿Seguro que desea realizar este cambio?"):
            dias = 0
            if estado == '1':   # Si estado es 1, cambia dias habiles a 5
                dias = 5
            paquetes[numero][-2] = dias    # Actualizan dias habiles y estado
            paquetes[numero][-1] = estado
        if not confirmarOpcion("", "¿Desea modificar más paquetes?"):
            break
    return paquetes

def eliminarPaquete():
    """
    Función:    Submenú de entradas requeridas para eliminar datos
    Entradas:   paquetes (dict) - Diccionario de paquetes
    Salidas:    Retorna registro de datos
    """
    while True:
        print("\n" + " Eliminación de Datos ".center(50,"=") + "\n")
        numero = validarPaquete()
        if not revisarPaquete(numero, paquetes):   # Restricción: Paquete no registrado
            imprimirError("No se encuentra registrado el paquete")
            continue
        if confirmarOpcion(" ADVERTENCIA ", "¿Seguro que desea eliminar este paquete?"):
            del paquetes[numero]
        if not validarMatriz():
            break
        if not confirmarOpcion("", "¿Desea eliminar más paquetes?"):
            break
    return paquetes

def cantidadPaquetes(ppaquetes):
    """
    Funcionamiento: Imprime la cantidad de paquetes que hay en el diccionario
    Entradas:
    -ppaquetes(int): es el número de paquetes
    Salidas: Na
    """
    print(f"\nEl total de paquetes registrados es: {ppaquetes}")
    return ""

def imprimirBasePaquetes(pbasePaquete):
    """
    Funcionamiento: Imprime todos los paquetes que estén almacenados en la base
    Entradas:
    -pbasePaquete(dict): es el diccionario con todos los paquetes
    Salidas: Na
    """
    lineas = "-"*140 #Esto es para no hacer la multiplicación varias veces
    print("\n" + lineas + "\n" + agregarEspacios("Número de paquete", 35) + agregarEspacios("Número de teléfono", 35) + agregarEspacios("Sucursal", 30) + agregarEspacios("Días hábiles", 25) + agregarEspacios("Estado", 15) + "\n" + lineas)
    for llave in sacarLlavesDicc(pbasePaquete):
        print(agregarEspacios(str(llave), 35) + agregarEspacios(str(pbasePaquete[llave][0]), 35) + agregarEspacios(pbasePaquete[llave][1], 30) + agregarEspacios(str(pbasePaquete[llave][2]), 25) + agregarEspacios(str(pbasePaquete[llave][-1]), 15) + "\n" + lineas)
    return ""

def menuReportes(plargoDiccionario, pbaseDiccionario):
    """
    Funcionamiento: Es el menú de reportes
    Entradas:
        -plargoDiccionario(int): Es la cantidad de elementos que tiene el diccionario
        -pabseDiccionario(dict): Es el diccionario que tiene los paquetes
    Salidas: N/A
    """
    while True:
        lista = ("\n1. Total de paquetes registrados.",
                 "2. Imprimir todos los paquetes.", "3. Salir")
        print("\n" + " Menú de Reportes ".center(50, "="))
        for elemento in lista:
            print(elemento)
        opcion = input("\nIngrese una opción: ")
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

def validarMatriz():
    """
    Funcionamiento: Valida la entrada al menu de reportes o de eliminacion de datos
    Entradas: N/A
    Salidas: Retorna True si hay paquetes en matriz, False si no
    """
    if len(paquetes) > 0:
        return True
    imprimirError("No hay paquetes registrados")
    return False

##############################################################
#####                Programa Principal                  #####
##############################################################

opciones = ("\n1. Insertar Paquete", "2. Actualizar Paquete",
            "3. Eliminar Paquete", "4. Reportes", "0. Salir")

while True:
    print(" Menú Principal ".center(50, "="))
    for string in opciones: # Imprime cada opcion
        print(string)
    guardarBD(paquetes)     # Guarda cambios de paquetes en archivo
    opcion = input("\nIngrese una opción: ")
    if opcion == "1":           # Inserta paquetes en diccionario
        ingresarPaquete()
    elif opcion == "2":         # Modifica paquetes
        actualizarPaquete()
    elif opcion == "3":
        if validarMatriz():     # Permite eliminar paquetes si los hay
            eliminarPaquete()
    elif opcion == "4":
        if validarMatriz():     # Muestra reportes sólo si hay paquetes
            menuReportes(len(paquetes), paquetes)
    elif opcion == "0":
        print("\nGracias por usar el sistema.")
        break
    else:                   # Restricción: Opción Inválida
        imprimirError("Opción Inválida")