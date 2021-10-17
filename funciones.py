# Elaborador por: Camilo Sánchez Rodríguez, Gabriel Gomez Vega
# Fecha de creación: 12/10/2021, 11:16 AM
# Última edición: XX/10/2021, XX:XX XX
# Versión: 3.9.6

##############################################################
#####              Importación de Librerías              #####
##############################################################

##############################################################
#####              Definición de Funciones               #####
##############################################################
    
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

############################################################
# Te lo voy a dejar aquí por si querés hacer alguna prueba #
############################################################

diccionario = {244: ["12345678", "Cartago", "10", "2"], 5:["88888888", "San José", "3", "1"], -2:["22222222", "limón", "1", "1"]}

print(f"\nEste es el diccionario de prueba: {diccionario}\n")
