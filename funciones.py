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

def ingresarPaquete(pregistro):
    """
    Función:    Submenú de entradas requeridas para registrar datos
    Entradas:   pregistro (dict) - Diccionario de paquetes
    Salidas:    Retorna registro de datos
    """
    while True:
        print("\n" + " Registro de Datos ".center(50,"=") + "\n")
        numero = validarPaquete()
        if revisarPaquete(numero, pregistro):   # Restriccion: Paquete repetido
            imprimirError("No se puede repetir número de paquete")
            continue
        telefono, sucursal = validarTelefono(), insistirNombreSucursal()
        estado, dias = opcionInsistirEstadoPaquete(), 10
        if estado != '1':   # Si estado es 2 o 3, cambia dias hábiles a 0
            dias = 0
        pregistro[numero] = [telefono, sucursal, dias, estado] # Crea paquete nuevo
        if not confirmarOpcion("", "¿Desea ingresar más paquetes?"):
            break   # Cierra submenu
    return pregistro

def actualizarPaquete(pregistro):
    """
    Función:    Submenú de entradas requeridas para actualizar datos
    Entradas:   pregistro (dict) - Diccionario de paquetes
    Salidas:    Retorna registro de datos
    """
    while True:
        print("\n" + " Modificación de Datos ".center(50,"=") + "\n")
        numero = validarPaquete()
        if not revisarPaquete(numero, pregistro): # Restriccion: Paquete no registrado
            imprimirError("No se encuentra registrado el paquete")
            continue
        estado = opcionInsistirEstadoPaquete()
        if estado == pregistro[numero][-1]:     # Restricción: Estado ya registrado
            imprimirError("El paquete ya tiene ese estado registrado")
            continue
        if confirmarOpcion(" ADVERTENCIA ", "¿Seguro que desea realizar este cambio?"):
            dias = 0
            if estado == '1':   # Si estado es 1, cambia dias habiles a 5
                dias = 5
            pregistro[numero][-2] = dias    # Actualizan dias habiles y estado
            pregistro[numero][-1] = estado
        if not confirmarOpcion("", "¿Desea modificar más paquetes?"):
            break
    return pregistro

def eliminarPaquete(pregistro):
    """
    Función:    Submenú de entradas requeridas para eliminar datos
    Entradas:   pregistro (dict) - Diccionario de paquetes
    Salidas:    Retorna registro de datos
    """
    while True:
        print("\n" + " Eliminación de Datos ".center(50,"=") + "\n")
        numero = validarPaquete()
        if not revisarPaquete(numero, pregistro):   # Restricción: Paquete no registrado
            imprimirError("No se encuentra registrado el paquete")
            continue
        if confirmarOpcion(" ADVERTENCIA ", "¿Seguro que desea eliminar este paquete?"):
            del pregistro[numero]
        if not confirmarOpcion("", "¿Desea eliminar más paquetes?"):
            break
    return pregistro


print(ingresarPaquete(x))
print(actualizarPaquete(x))
print(eliminarPaquete(x))