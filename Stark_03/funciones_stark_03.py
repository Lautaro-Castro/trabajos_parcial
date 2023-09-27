from os import system


def stark_normalizar_datos(lista: list):

    """
    Castea los valores del diccionario a int o float, según corresponda su tipo.
    
    Args:
        lista(list): Lista que contenga el diccionario a normalizar.
        
    Returns:
        cambio_de_dato(bool): Toma el valor True si algún dato fue casteado, o False si ninguno se casteo.
    """
    
    cambio_de_dato = False  
    
    if len(lista) > 0:
        for e_lista in lista:
            
            if type(e_lista["altura"]) != float or type(e_lista["peso"]) != float or type(e_lista["fuerza"]) != int:
                e_lista["altura"] = float(e_lista["altura"])
                e_lista["peso"] = float(e_lista["peso"])
                e_lista["fuerza"] = int(e_lista["fuerza"])
                cambio_de_dato = True
    
    return(cambio_de_dato)

def obtener_dato(diccionario: dict, clave: str):
    
    """
    Busca en un diccionario el valor de una clave.
    
    Args: 
        clave(str): Clave a buscar el valor.
        
    Returns:
        Retorna el valor de la clave si fue encontrada, si no retorna False.
    """
    
    if len(diccionario) > 0 and clave in diccionario:
        return(diccionario[clave])
    else:
        return(False)
      
def obtener_nombre(diccionario: dict):
    
    """
    Busca en un diccionario el valor de la clave "nombre".
    
    Args: 
        diccionario(dic): Diccionario en el cuál se buscara el valor de "nombre".
        
    Returns:
        Retorna el valor de la clave si fue encontrada, si no retorna False.
    """
    
    if obtener_dato(diccionario, "nombre"):
        return(f"Nombre: {obtener_dato(diccionario, 'nombre')}")
    else:
        return(False)
      
def obtener_nombre_y_dato(diccionario: dict, clave: str):
    """
    Busca en un diccionario el valor de una clave específica.
    
    Args: 
        diccionario(dic): Diccionario en el cuál se buscara el valor de la clave.
        clave(str): Clave a la cuál buscarle el valor.
        
    Returns:
        Retorna el valor de la clave si fue encontrada, si no retorna False.
    """
    nombre = obtener_nombre(diccionario)
    dato = obtener_dato(diccionario, clave)
    
    if nombre and dato:
        return(f"{nombre} | {clave.title()}: {dato}")
    else:
        return(False)
     
def validar_int_float(dato):
    """
    Valida que un dato sea de tipo int o float.
    
    Args: 
        dato: Dato a validar el tipo.
        
    Returns:
        Retorna True si el dato es de tipo int o float, si no retorna False.
    """
    
    if type(dato) != int and type(dato) != float:
        return(False)
    else:
        return(True)
     
def obtener_maximo(lista: list, clave: str):
    """
    Obtiene el valor máximo en una lista de diccionarios.
    
    Args: 
        lista(list): Lista que contenga los diccionarios de donde extraer el valor máximo.
        clave(str): Clave del dato a buscar el valor máximo.
        
    Returns:
        Retorna el valor máximo de la clave si fue encontrado, si no retorna False
    """
    maximo = 0
    bandera_maximo = True
    
    if len(lista) == 0:
        return(False)
    else:
        for e_lista in lista:
            dato = e_lista[clave.lower()]
            if not validar_int_float(dato):
                return(False)
            elif bandera_maximo:
                maximo = dato
                bandera_maximo = False
            elif dato > maximo:
                maximo = dato
    
    return(maximo)
                                         
def obtener_minimo(lista: list, clave: str):
    """
    Obtiene el valor mínimo en una lista de diccionarios.
    
    Args: 
        lista(list): Lista que contenga los diccionarios de donde extraer el valor mínimo.
        clave(str): Clave del dato a buscar el valor mínimo.
        
    Returns:
        Retorna el valor mínimo de la clave si fue encontrado, si no retorna False
    """
    minimo = 0
    bandera_minimo = True
    
    if len(lista) == 0:
        return(False)
    else:
        for e_lista in lista:
            dato = e_lista[clave.lower()]
            if not validar_int_float(dato):
                return(False)
            elif bandera_minimo:
                minimo = dato
                bandera_minimo = False
            elif dato < minimo:
                minimo = dato
    
    return(minimo)

def obtener_dato_cantidad(lista: list, valor, clave: str):
    """
    Busca la cantidad de veces que un dato se repite en una lista de diccionarios.
    
    Args: 
        lista(list): Lista que contenga los diccionarios donde verificar el dato repetido.
        valor: Dato a buscar cuantas veces se repite.
        clave(str): Clave donde validar que se repita el dato.
        
    Returns:
        Retorna una lista con los diccionarios que contienen el dato.
    """
    lista_local = []
    for e_lista in lista:
        if e_lista[clave] == valor:
            lista_local.append(e_lista)
    return(lista_local)

def stark_imprimir_heroes(lista: list):
    """
    Imprime los datos guardados en una lista.
    
    Args: 
        lista(list): Lista con los datos a imprimir.

    Returns:
        Retorna False si la lista está vacía.
    """

    if len(lista) > 0:
        for e_lista in lista:
            if type(e_lista) == dict:
                print("-------------------------")
                lista_claves = list(e_lista.keys())    
                lista_valores = list(e_lista.values())

                for e_lista_2 in range(len(lista_claves)):
                    print(f"{lista_claves[e_lista_2].title()}: {lista_valores[e_lista_2]}")
                
                print("-------------------------")
            else:
                print("-------------------------")
                print(e_lista)
                print("-------------------------")

    else:
        return(False)

def sumar_dato_heroe(lista: list, clave: str):
    """
    Suma un dato(int/float) de una lista de diccionarios.
    
    Args: 
        lista(list): Lista con los datos a sumar.
        clave(str): Clave del dato a sumar.

    Returns:
        Retorna el valor de la suma.
    """
    suma = 0
    if len(lista) > 0:
        for e_lista in lista:
            if type(e_lista) == dict and len(e_lista) > 0:
                if validar_int_float(e_lista[clave]):
                    suma += e_lista[clave]
    

    return(suma)

def dividir(dividendo, divisor):
    """
    Realiza una división.
    
    Args: 
        dividendo: Número a dividir.
        divisor: Número que divide.

    Returns:
        Retorna el resultado de la división. Si la división no se puede hacer retorna False.
    """
    if  not validar_int_float(dividendo): 
        return(False)
    elif not validar_int_float(divisor):
        return(False)
    elif divisor == 0: 
         return(False)
    else:
        return(dividendo / divisor)

def calcular_promedio(lista: list, dato: str):
    """
    Calcula el promedio de un dato de una lista de diccionarios.
    
    Args: 
        lista(list): Lista con el dato a promediar.

    Returns:
        Retorna False si el promedio no se puede calcular.
    """
    suma = sumar_dato_heroe(lista, dato)
    
    return(dividir(suma, len(lista)))
    
def mostrar_promedio_dato(lista: list, clave: str):
    
    """
    Imprime el promedio de un dato de una lista de diccionarios.
    
    Args: 
        lista(list): Lista con el dato a promediar.

    Returns:
        Retorna False si el promedio no se puede imprimir
    """
    
    if len(lista) > 0:
        for e_lista in lista:
            if  validar_int_float(e_lista[clave]):
                promedio = calcular_promedio(lista, clave)
            else:
                return(False)
        print(f"El promedio es: {promedio}")
    else:
        return(False)
    
def imprimir_menu():
    """
    Imprime por pantalla el menú de opciones.
    """
    print("1)Normalizar datos.\n2)Recorrer la lista imprimiendo por consola el nombre de cada superhéroe degénero NB.\n3)Recorrer la lista y determinar cuál es el superhéroe más alto de género F\n4)Recorrer la lista y determinar cuál es el superhéroe más alto de género M\n5)Recorrer la lista y determinar cuál es el superhéroe más débil de género M\n6)Recorrer la lista y determinar cuál es el superhéroe más débil de género NB\n7)Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB\n8)Determinar cuántos superhéroes tienen cada tipo de color de ojos.\n9)Determinar cuántos superhéroes tienen cada tipo de color de pelo.\n10)Listar todos los superhéroes agrupados por color de ojos.\n11)Listar todos los superhéroes agrupados por tipo de inteligencia.\n12)Finalizar el programa")

def validar_entero(numero: str):
    """
    Valida que un str recibido sea un número entero.
    
    Args: 
        numero(str): String a validar que sea un entero.

    Returns:
        Retorna True si el string es un entero o False si no lo es.
    """
    
    if numero.strip().isdigit():
        return(True)
    else:
        return(False)

def stark_menu_principal():
    """
    Imprime por pantalla el menú de opciones, solicita el ingreso de una opción y verifica que esta sea válida.

    Returns:
        Si la opción es válida la retorna casteada a int, si no retorna False.
    """
    imprimir_menu()
    opcion = input("\nIngrese una opción: ")
    if validar_entero(opcion):
        return(int(opcion))
    else:
        return(False)

def stark_marvel_app(lista: list):
    """
    Ejecuta el programa principal.
    
    Args:
        lista(list): Lista que contenga los diccionarios con los que funcionará el programa. 
    """
    
    run = True
    bandera_normalizar = False
    while run: 
        match stark_menu_principal():
            
            case 1:
                if stark_normalizar_datos(lista):
                    input("Datos normalizados correctamente. Presione ENTER para continuar")
                    bandera_normalizar = True
                    system("cls")
                else:
                    input("Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente")
                    system("cls")
            case 2:
                if bandera_normalizar:
                    for e_lista in lista:
                        if obtener_nombre_y_dato(e_lista, "genero") and "NB" in obtener_nombre_y_dato(e_lista, "genero").upper():
                            print(obtener_nombre_y_dato(e_lista, "genero"))
                    input("Presione ENTER para continuar")        
                    system("cls")    
                else:
                     input("Por favor normalizar los datos primero. Presione ENTER para continuar")
                     system("cls")
            case 3:
                if bandera_normalizar:
                    lista_f = obtener_dato_cantidad(lista, "F", "genero")     
                    mas_alta = obtener_maximo(lista_f, "altura")
                    lista_mas_altas = obtener_dato_cantidad(lista_f, mas_alta, "altura")
                    stark_imprimir_heroes(lista_mas_altas)
                    input("Presione ENTER para continuar")  
                    system("cls")
                else:
                     input("Por favor normalizar los datos primero. Presione ENTER para continuar")
                     system("cls")
            case 4:
                if bandera_normalizar:
                    lista_m = obtener_dato_cantidad(lista, "M", "genero")     
                    mas_alto = obtener_maximo(lista_m, "altura")
                    lista_mas_altos = obtener_dato_cantidad(lista_m, mas_alto, "altura")
                    stark_imprimir_heroes(lista_mas_altos)
                    input("Presione ENTER para continuar")  
                    system("cls")
                else:
                     input("Por favor normalizar los datos primero. Presione ENTER para continuar")
                     system("cls")
            case 5:
                if bandera_normalizar:
                    lista_m = obtener_dato_cantidad(lista, "M", "genero")     
                    mas_debil = obtener_minimo(lista_m, "fuerza")
                    lista_mas_debiles = obtener_dato_cantidad(lista_m, mas_debil, "fuerza")
                    stark_imprimir_heroes(lista_mas_debiles)
                    input("Presione ENTER para continuar")  
                    system("cls")
                else:
                     input("Por favor normalizar los datos primero. Presione ENTER para continuar")
                     system("cls")
            case 6:
                if bandera_normalizar:
                    if bandera_normalizar:
                        lista_nb = obtener_dato_cantidad(lista, "NB", "genero")     
                        mas_debil = obtener_minimo(lista_nb, "fuerza")
                        lista_mas_debiles = obtener_dato_cantidad(lista_nb, mas_debil, "fuerza")
                        stark_imprimir_heroes(lista_mas_debiles)
                        input("Presione ENTER para continuar")
                        system("cls")  
                else:
                     input("Por favor normalizar los datos primero. Presione ENTER para continuar")
                     system("cls")
            case 7:
                
                if bandera_normalizar:
                        lista_nb = obtener_dato_cantidad(lista, "NB", "genero")     
                        mostrar_promedio_dato(lista_nb, "fuerza")
                        input("Presione ENTER para continuar")
                        system("cls")
                else:
                     input("Por favor normalizar los datos primero. Presione ENTER para continuar")
                     system("cls")
            case 8:
                if bandera_normalizar:
                    lista_color_ojos = lista_tipo_dato(lista, "color_ojos")
                    cantidad_color_ojos = []
                    for e_lista in lista_color_ojos:
                            cantidad_color_ojos.append(obtener_dato_cantidad(lista, e_lista, "color_ojos"))
                           
                    for e_lista in cantidad_color_ojos:
                        
                        color = e_lista[0].get("color_ojos")
                        print(f"{color}: {len(e_lista)}")
                    input("Presione ENTER para continuar")        
                    system("cls") 
                                 
                else:
                     input("Por favor normalizar los datos primero. Presione ENTER para continuar")
                     system("cls")
            case 9:
                if bandera_normalizar:
                    lista_color_pelo = lista_tipo_dato(lista, "color_pelo")
                    cantidad_color_pelo = []
                    for e_lista in lista_color_pelo:
                            cantidad_color_pelo.append(obtener_dato_cantidad(lista, e_lista, "color_pelo"))
                           
                    for e_lista in cantidad_color_pelo:
                        
                        color = e_lista[0].get("color_pelo")
                        print(f"{color}: {len(e_lista)}")
                    input("Presione ENTER para continuar")        
                    system("cls") 
                                 
                else:
                     input("Por favor normalizar los datos primero. Presione ENTER para continuar")
                     system("cls")
            case 10:
                if bandera_normalizar:
                    lista_color_ojos = lista_tipo_dato(lista, "color_ojos")   
                    cantidad_color_ojos = []
                    for e_lista in lista_color_ojos:
                        cantidad_color_ojos.append(obtener_dato_cantidad(lista, e_lista, "color_ojos"))
                           
                    for e_lista in cantidad_color_ojos:
                        print(f"\t{e_lista[0]['color_ojos']}")
                        stark_imprimir_heroes(e_lista)
                    input("Presione ENTER para continuar")        
                    system("cls") 
                                 
                else:
                     input("Por favor normalizar los datos primero. Presione ENTER para continuar")
                     system("cls")
            case 11:
                if bandera_normalizar:
                    lista_tipo_inteligencia = lista_tipo_dato(lista, "inteligencia")
                    cantidad_tipo_inteligencia = []
                    for e_lista in lista_tipo_inteligencia:
                            cantidad_tipo_inteligencia.append(obtener_dato_cantidad(lista, e_lista, "inteligencia"))
                           
                    for e_lista in cantidad_tipo_inteligencia:
                        print(f"\t{e_lista[0]['inteligencia']}")
                        stark_imprimir_heroes(e_lista)
                    input("Presione ENTER para continuar")        
                    system("cls") 
                                 
                else:
                     input("Por favor normalizar los datos primero. Presione ENTER para continuar")
                     system("cls")
            case 12:
                print("Gracias por usar el programa")
                run = False
            case default:
                input("¡ERROR! La opcion ingresada no es correcta. Presione ENTER para continuar")
                system("cls")

def lista_tipo_dato(lista: list, clave: str):
    """
    Crea una lista con los dsitintos valores que camparten misma clave.
    
    Args:
        lista(list): Lista de diccionarios de los cuáles obtener los distintos valores de una misma clave.
        clave(str): Clave de la cuál obtener los valores.
    
    Return:
        lista_tipo_dato(list): Lista con los distintos valores encontrados.
        False: Si la lista está vacía retorna False.
    """
    
    lista_tipo_dato = []
    if len(lista) > 0:
        for e_lista in lista:
            if e_lista[clave] not in lista_tipo_dato:
                lista_tipo_dato.append(e_lista[clave])
        return(lista_tipo_dato)
    else:
        return(False)
    

    
    
