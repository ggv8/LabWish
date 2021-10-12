# Elaborador por: Camilo Sánchez Rodríguez, Gabriel Gomez Vega
# Fecha de creación: 12/10/2021, 11:16 AM
# Última edición: XX/10/2021, XX:XX XX
# Versión: 3.9.6

##############################################################
#####              Importación de Librerías              #####
##############################################################
from wish import *
##############################################################
#####              Definición de Funciones               #####
##############################################################
def cantidadPaquetes(ppaquetes):
    """
    Funcionamiento: Imprime la cantidad de paquetes que hay en el diccionario
    Entradas:
    -ppaquetes(int): es el número de paquetes
    Salidas: Na
    """
    return f"El total de paquetes registrados es: {ppaquetes}"
    
def agregarEspacios(string, tamano):
    """
    Funcionamiento: Sirve para que el string ingresado tenga un tamaño específico con espacios en blanco
    Entradas:
    string(str): Es el texto a modificar tamaño
    tamano(int): Es la cantidad de caracteres de espacio vacío a agregar
    Salidas: Es el string modificado
    """
    return (string + (' ' * tamano))[:tamano]

def sacarLlavesDicc(pdiccionario):
    """
    Funcionamiento: Agrega en una lista las llaves del diccionario y las ordena
    Entradas:
    -pdiccionario(dict): Es el diccionario a sacar las llaves
    Salidas: 
    """
    listaLlaves = []
    for llave in pdiccionario.keys():
        listaLlaves.append(llave)
    listaLlaves.sort()
    return listaLlaves

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

############################################################
# Te lo voy a dejar aquí por si querés hacer alguna prueba #
############################################################

diccionario = {244: ["12345678", "Cartago", "10", "2"], 5:["88888888", "San José", "3", "1"], -2:["22222222", "limón", "1", "1"]}

print(f"\nEste es el diccionario de prueba: {diccionario}\n")

print(imprimirBasePaquetes(diccionario))