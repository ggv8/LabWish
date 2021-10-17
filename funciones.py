# Elaborador por: Camilo Sánchez Rodríguez, Gabriel Gomez Vega
# Fecha de creación: 12/10/2021, 11:16 AM
# Última edición: 16/10/2021, 11:03 PM
# Versión: 3.9.6

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

def confirmarOpcion(ptitulo, pmensaje):
    """
    Función:    Pide confirmación antes de realizar una tarea
    Entradas:   ptitulo, pmensaje (str) - Título y contenido de opcion
    Salidas:    Retorna True (Aceptar), False (Cancelar)
    """
    while True:
        print("\n" + f"{ptitulo}".center(50,"=") + "\n")
        print(pmensaje.center(50," "))
        entrada = input("\n" + "<A> Aceptar  <C> Cancelar".center(49," "))
        if entrada == "A":
            return True
        elif entrada == "C":
            return False
        imprimirError("Confirme o cancele con A o C") # Restricción: Entrada != B o C
