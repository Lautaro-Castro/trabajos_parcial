from os import system

def menu_stark_2(opciones: list):
    
    """
    Imprime el menú en pantalla y solicita el ingreso de una opción del mismo.
    
    Args:
        opciones(list): Lista que contenga las opciones que se pueden ingresar.
    
    Returns:
        Un string que representa la opción ingresada. 
    """
    validacion = False
    
    while not(validacion):
        print("-"*30 + "\n|DESAFIO STARK 02 EL PROGRAMA|\n" + "-"*30 +"\nA) Recorrer la lista imprimiendo por consola el nombre de cada héroe de género NB.\nB) Recorrer la lista y determinar cuál es el héroe más alto de género F.\nC) Recorrer la lista y determinar cuál es el héroe más alto de género M.\nD) Recorrer la lista y determinar cuál es el héroe más débil de género M.\nE) Recorrer la lista y determinar cuál es el héroe más débil de género NB.\nF) Recorrer la lista y determinar la fuerza promedio de los héroes de género NB.\nG) Determinar cuántos héroes tienen cada tipo de color de ojos.\nH) Determinar cuántos héroes tienen cada tipo de color de pelo.\nI) Listar todos los héroes agrupados por color de ojos.\nJ) Listar todos los superhéroes agrupados por tipo de inteligencia.\nK) Finalizar programa.")
        opcion = input("\nIngrese su opcion: ").strip().lower()
        
        validacion = validar_opcion_ingresada(opcion, opciones)
        
    return opcion

def ejecutar_opcion_a(lista: list):
    
    """
    Busca los héroes de género NB e imprime en pantalla sus nombres.
    
    Args:
        lista(list): Lista que contenga todos los héroes.
    """
    print("-"*20 +"\n|HEROES DE GENERO NB|\n" + "-"*20)
    
    lista_por_genero = obtener_heroes_por_genero(lista, "NB")
    for elemento in lista_por_genero:
        print("-"*50 + f"\nNombre: {elemento['nombre']}\n" + "-"*50)   
    input("\nPresione ENTER para continuar")
    system("cls")

def ejecutar_opcion_b(lista: list):
    """
    Busca al héroe femenino más alto y lo imprime en pantalla.
    
    Args:
        lista(list): Lista que contenga todos los héroes.
    """
    mayor_altura = 0.0
    nombre_mayor_altura = ""
    bandera_altura = True
    lista_f = obtener_heroes_por_genero(lista, "F")
    
    for elemento in lista_f:
        if bandera_altura:
            mayor_altura = float(elemento["altura"])
            nombre_mayor_altura = elemento["nombre"]
            bandera_altura = False
        elif mayor_altura < float(elemento["altura"]):
            mayor_altura = float(elemento["altura"])
            nombre_mayor_altura = elemento["nombre"]
        
    print(f"\n{nombre_mayor_altura} mide {mayor_altura} y es la héroe femenina con mayor altura")
    input("\nPresione ENTER para continuar")
    system("cls")

def ejecutar_opcion_c(lista: list):
    
    """
    Busca al héroe masculino más alto y lo imprime en pantalla.
    
    Args:
        lista(list): Lista que contenga todos los héroes.
    """
    mayor_altura = 0.0
    nombre_mayor_altura = ""
    bandera_altura = True
    lista_m = obtener_heroes_por_genero(lista, "M")
    
    for elemento in lista_m:
            if bandera_altura:
                mayor_altura = float(elemento["altura"])
                nombre_mayor_altura = elemento["nombre"]
                bandera_altura = False
            elif mayor_altura < float(elemento["altura"]):
                mayor_altura = float(elemento["altura"])
                nombre_mayor_altura = elemento["nombre"]
        
    print(f"\n{nombre_mayor_altura} mide {mayor_altura} y es el héroe masculino con mayor altura")
    input("\nPresione ENTER para continuar")
    system("cls")

def ejecutar_opcion_d(lista: list):
    
    """
    Busca al héroe masculino més débil y lo imprime en pantalla.
    
    Args:
        lista(list): Lista que contenga todos los héroes.
    """
    menor_fuerza = 0
    nombre_menor_fuerza = ""
    bandera_fuerza = True
    lista_m = obtener_heroes_por_genero(lista, "M")
    
    for elemento in lista_m:
            if bandera_fuerza:
                menor_fuerza = int(elemento["fuerza"])
                nombre_menor_fuerza = elemento["nombre"]
                bandera_fuerza = False
            elif menor_fuerza > int(elemento["fuerza"]):
                menor_fuerza = int(elemento["fuerza"])
                nombre_menor_fuerza = elemento["nombre"]
        
    print(f"\n{nombre_menor_fuerza} es el superheroe masculino mas debil con una fuerza de: {menor_fuerza}")
    input("\nPresione ENTER para continuar")
    system("cls")

def ejecutar_opcion_e(lista: list):
    
    """
    Busca el héroe NB más débil y lo imprime en pantalla.
    
    Args:
        lista(list): Lista que contenga todos los héroes.
    """
    menor_fuerza = 0
    nombre_menor_fuerza = ""
    bandera_fuerza = True
    lista_NB = obtener_heroes_por_genero(lista, "NB")
    
    for elemento in lista_NB:
        if elemento["genero"] == "NB":
            if bandera_fuerza:
                menor_fuerza = int(elemento["genero"])
                nombre_menor_fuerza = elemento["nombre"]
                bandera_fuerza = False
            elif menor_fuerza > int(elemento["fuerza"]):
                menor_fuerza = int(elemento["fuerza"])
                nombre_menor_fuerza = elemento["nombre"]
        
    print(f"\n{nombre_menor_fuerza} es el superheroe no binario mas debil con una fuerza de: {menor_fuerza}")
    input("\nPresione ENTER para continuar")
    system("cls")

def ejecutar_opcion_f(lista: list):
    
    """
    Imprime por pantalla la fuerza promedio de los héroes de género NB.
    
    Args:
        lista(list): Lista que contenga todos los héroes.
    """
    total_fuerzas = 0.0
    contador = 0
    lista_nb = obtener_heroes_por_genero(lista, "NB")
    
    for elemento in lista_nb:
            total_fuerzas += int()
            contador += 1
           
    print(f"\nLa fuerza promedio de los superheroes no binarios es: {total_fuerzas/contador}")
    input("\nPresione ENTER para continuar")
    system("cls")

def ejecutar_opcion_g(lista: list):
    
    """
    Imprime en pantalla cuántos héroes tienen cada tipo de color de ojos.
    
    Args:
        lista(list): Lista que contenga todos los héroes.
    """
    
    cantidad_colores_ojos = {}  
    for elemento in lista:
        color_ojos = elemento["color_ojos"].title()

        if color_ojos in cantidad_colores_ojos:
            cantidad_colores_ojos[color_ojos] += 1
        else:
            cantidad_colores_ojos[color_ojos] = 1
            
    print("-"*38 + "\n|Cantidad de héroes por color de ojos|\n" + "-"*38)
    imprimir_dato_en_dic(cantidad_colores_ojos)
    input("\nPresione ENTER para continuar")
    system("cls")

def ejecutar_opcion_h(lista: list):
    
    """
    Imprime en pantalla cuántos héroes tienen cada tipo de color de pelo.
    
    Args:
        lista(list): Lista que contenga todos los héroes.
    """
    cantidad_colores_pelo = {}  
    for elemento in lista:
        color_pelo = elemento["color_pelo"].title()

        if color_pelo in cantidad_colores_pelo:
            cantidad_colores_pelo[color_pelo] += 1
        else:
            cantidad_colores_pelo[color_pelo] = 1
    
    print("-"*38 + "\n|Cantidad de héroes por color de pelo|\n" + "-"*38)
    imprimir_dato_en_dic(cantidad_colores_pelo)
    input("\nPresione ENTER para continuar")
    system("cls")

def ejecutar_opcion_i(lista: list):
    
    """
    Imprime a los héroes agrupados por color de ojos.
    
    Args:
        lsita(list): Lista que contenga todos los héroes.
    """
    
    grupo_colores_ojos = {}
    for elemento in lista:
        
        color_ojos = elemento["color_ojos"].title()
        nombre = elemento["nombre"]
        
        if color_ojos in grupo_colores_ojos:
            grupo_colores_ojos[color_ojos].append(nombre)
        else:
            grupo_colores_ojos[color_ojos] = [nombre]
            
    print("-"*36 + "\n|Héroes agrupados por color de ojos|\n" + "-"*36)
    imprimir_lista_en_dic(grupo_colores_ojos)
    input("\nPresione ENTER para continuar")
    system("cls")

def ejecutar_opcion_j(lista: list):
    
    """
    Imprime a los héroes agrupados por tipo de inteligencia.
    
    Args: 
        lista(list): Lista que contenga todos los héroes
    """
    
    grupo_tipo_inteligencia = {}
    for elemento in lista:
        
        tipo_inteligencia = elemento["inteligencia"].title()
        nombre = elemento["nombre"]
        
        if tipo_inteligencia in grupo_tipo_inteligencia:
            grupo_tipo_inteligencia[tipo_inteligencia].append(nombre)
        else:
            grupo_tipo_inteligencia[tipo_inteligencia] = [nombre]
            
    print("-"*43 + "\n|Héroes agrupados por tipo de inteligencia|\n" + "-"*43)
    imprimir_lista_en_dic(grupo_tipo_inteligencia)
    input("\nPresione ENTER para continuar")
    system("cls")

def validar_opcion_ingresada(opcion: str, opciones: list):
    
    """
    Valida que la opción ingresada este dentro de la opciones permitidas.
    
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
    
def obtener_heroes_por_genero(lista: list, genero: str):

    """
    Busca en la lista todos los héroes de un género en específico.
    
    Args:
        lista(list): Lista que contenga todos los héroes a comparar.
        genero(str): Clave del género a buscar.
        
    Returns:
        Lista que contiene los heroes filtrados por genero.
    """
    lista_por_genero = []
    
    if len(lista) > 0:
        for elemento in lista:
            if elemento["genero"].lower() == genero.lower():
                lista_por_genero.append(elemento)    
 
    return(lista_por_genero)
    
def imprimir_dato_en_dic(dic: dict):
    """
    Recorre un diccionario imprimiendo en pantalla cada clave con su valor.

    Args:
        dic(dict): Diccionario que se desea imprimir en pantalla.
    """
    for clave, valor in dic.items():
        if clave != "":
            print(f"{clave}: {valor}")
        else:
            print(f"None: {valor}")
            
def imprimir_lista_en_dic(dic: dict):
    """
    Recorre un diccionario imprimiendo en pantalla la lista de cada clave.

    Args:
        dic(dict): Diccionario que se desea imprimir en pantalla.
    """
    for clave, valor in dic.items():
        if clave != "":
            print("-"*(len(clave)+2) + "\n|" + clave.title() + "|\n"+ "-"*(len(clave)+2))
        else:
            print("-"*6 + "\n|None|\n" + "-"*6)
        for elemento in valor:
            print(elemento.title())
        print("")
        