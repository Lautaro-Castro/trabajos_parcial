from os import system

def menu_stark_1(opciones: list):
    """
    Imprime el menú en pantalla y solicita el ingreso de una opción del mismo.
    
    Args:
        opciones(list): Lista que contenga las opciones que se pueden ingresar.
    
    Returns:
        Un string que representa la opción ingresada. 
    """
    validacion = False
    
    while not(validacion):
        print("-"*30 + "\n|DESAFIO STARK 01 EL PROGRAMA|\n" + "-"*30 +"\nA) Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe.\nB) Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO).\nC) Recorrer la lista y mostrar nombre e identidad del héroe más bajo (MÍNIMO).\nD) Recorrer la lista y determinar el peso promedio de los héroes masculinos (PROMEDIO).\nE) Recorrer la lista y mostrar nombre y peso de los héroes (cualquier género) los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino.\nF) Finalizar programa.")

        opcion = input("\nIngrese su opcion: ")
        opcion = opcion.lower().strip()
        
        validacion = validar_opcion_ingresada(opcion, opciones)
    return opcion

def ejecutar_opcion_a(lista: list):
    
    """
    Imrprime en pantalla los datos de todos los heroes.
    
    Args:
        lista(list): Lista que contenga todos los héroes a imprimir.
    
    """
    
    for elemento in lista:
        print("-"*40)
        for s_elemento in elemento:
            print(f"{s_elemento.title()}: {elemento.get(s_elemento)}")
        print("-"*40)
    input("Presione ENTER para continuar.")
    system("cls")

def ejecutar_opcion_b(lista: list):
    
    """
    Busca el héroe de mayor fuerza e imprime por pantalla su identidad y peso.
    
    Args:
        lista(list): Lista que contenga todos los héroes de donde sacar el más fuerte.
    """
    mayor_fuerza = 0
    bandera_fuerza = True
    
    for elemento in lista:
        if bandera_fuerza:
            mayor_fuerza = int(elemento['fuerza'])
            bandera_fuerza = False
        elif mayor_fuerza < int(elemento['fuerza']):
            mayor_fuerza = int(elemento['fuerza'])
    
    print("Superheroe/s más fuerte/s:")
    for elemento in lista:
        if mayor_fuerza == int(elemento['fuerza']):
            print("-"*30 + f"\nIdentidad: {elemento['identidad']}\nPeso: {'peso'}\n" + "-"*30)
    input("Presione ENTER para continuar.")
    system("cls")

def ejecutar_opcion_c(lista: list):
    
    """
    Busca el héroe de menor altura e imprime su nombre e identidad.
    
    Args:
        lista(list): Lista que contenga todos los héroes de donde sacar el más bajo.
    """
    
    menor_altura = 0
    bandera_altura = True
    
    for elemento in lista:
        if bandera_altura:
            menor_altura = float(elemento['altura'])
            bandera_altura = False
        elif menor_altura < float(elemento['altura']):
            menor_altura = float(elemento['altura'])
    
    print("Superheroe/s de menor altura:")
    for elemento in lista:
        if menor_altura == float(elemento['altura']):
            print("-"*30 + f"\nNombre: {elemento['nombre']}\nIdentidad: {elemento['identidad']}\n" + "-"*30)
            
    input("Presione ENTER para continuar.")
    system("cls")

def ejecutar_opcion_d(lista: list):
    
    """
    Determina el peso promedio de los héroes masculinos y lo imprime en pantalla.
    
    Args:
        lista(list): Lista que contenga todos los héroes de donde sacar el promedio.
    """
    total_pesos = 0.0
    contador = 0
    
    for elemento in lista:
        if elemento['genero'].lower() == "m":
            total_pesos += float(elemento['peso'])
            contador += 1
                    
    print(f"El peso promedio de los superheroes masculinos es: {total_pesos/contador}")
    input("Presione ENTER para continuar.")
    system("cls")

def ejecutar_opcion_e(lista: list):
    
    """
    Imprime por pantalla nombre y peso de los héroes cuya fuerza supere el promedio de la fuerza femenina.
    
    Args:
        lista(list): Lista que contenga todos los héroes a comparar.
    """
    total_fuerzas = 0
    promedio_fuerzas = 0
    contador = 0
    
    for elemento in lista:
        if elemento['genero'].lower() == "f":
            total_fuerzas += int(elemento['fuerza'])
            contador += 1
    
    promedio_fuerzas = total_fuerzas / contador
    
    
    print(f"\nSuperheroes con fuerza superior al promedio femenino ({promedio_fuerzas}):")
    
    for elemento in lista:
        if float(elemento['fuerza']) > promedio_fuerzas:
            print("-"*30 + f"\nNombre: {elemento['nombre']}\nPeso: {elemento['peso']}\n" + "-"*30)
            
    input("Presione ENTER para continuar.")
    system("cls")
  
def validar_opcion_ingresada(opcion: str, opciones: list):
    
    """
    Valida que la opcion ingresada este dentro de la opciones permitidas.
    
    Args:
        opcion(str): Representa la opcion ingresada.
        opciones(list): Lista que contenga las opciones posibles.

    Returns:
        Retorna True si la opcion esta dentro de la opciones permitidas, False si no.
    """
    for elemento in opciones:
        if opcion == elemento:
            return True
        
    input("¡ERROR! La opcion ingresada no es válida. Presione ENTER para continuar")
    system("cls")
    return False
