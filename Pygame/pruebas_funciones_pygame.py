import pygame


def listar_datos(lista: list, clave: str):
    """ 
    Enlista los valores obtenidos de una lista de diccionarios.
    
    Args: 
        lista(list): Lista de diccionarios con los valores a enlistar.
        clave(str): Clave de los valores a enlista.
        
    Returns:
        lista_local(list): Lista con los valores enlistados.
        False: Retorna False si la lista está vacía.
    
    """
    if len(lista) > 0:
        
        lista_local = []
        
        for e_lista in lista:
            lista_local.append(e_lista[clave])
        
        return(lista_local) 
    else:
        return(False)
 
def blitear_rects_mismo_fondo(pantalla, fondo, rectangulos: list):
    """
    Dibuja rectangulos del mismo color. 
    
    Args:
        pantalla: Superficie donde dibujar los botones.
        color: Color de los botones.
        rectangulos(list): Lista que contenga los rectangulos ya declarados.
    """
    for indice in range(len(rectangulos)):
        pantalla.blit(fondo, rectangulos[indice])
        
def blitear_varias_etiquetas(superficie, etiquetas, pos_etiquetas):
    """ 
    Añade varios textos a la pantalla.
    
    Args: 
        superficie: Superficie donde añadir los textos.
        etiquetas: Textos ya renderizados.
        pos_etiquetas: Posiciones de los textos
    """
    for indice in range(len(etiquetas)):
        superficie.blit(etiquetas[indice], pos_etiquetas[indice])
    
def validar_click_en_rta(mostrar_rtas: bool, posicion_click: list, rtas: dict, rta: str):
    """ 
    Valida que se haya click en algún botón de las respuestas.
    
    Args: 
        mostrar_rtas(bool): Booleano que indica si las respuestas se están mostrando.
        posicion_click(list): Lista que indica las coordenadas donde se hizo click. 
        rtas(dict): Diccionario que contiene las posibles respuestas y sus posiciones.
        rta(str): String donde guardar la respuesta seleccionada.
        
    Returns:
        rta(stra): String de la respuesta seleccionada.
    
    """
    for elemento in rtas:
        if mostrar_rtas and elemento["pos"].collidepoint(posicion_click):
            rta = elemento["rta"]
    return rta 
    
def renderizar_varias_etiquetas(fuente, textos: list, bold: bool, color):
    """ 
    Renderiza varios textos.
    
    Args: 
        fuente: Fuente ya seteada a usar en los textos.
        textos(list): Lista de strings de los textos a renderizar.
        bold(bool): Texto en negrita.
        color: Color del texto.
        
    Returns:
        etiquetas(list): Lista con los textos renderizados.
    
    """
    etiquetas = []
    
    for i in range(len(textos)):
        etiquetas.append(fuente.render(textos[i], bold, color))
    return(etiquetas) 

def validar_rta(datos: dict, rta_correcta: str):
    """ 
    Valida si la respuesta es correcta o no y actualiza los valores según corresponda.
    
    Args: 
        datos(dict): Diccionario con los datos a actualizar.
        rta_correcta(str): String con la respuesta correcta.
        
    Returns:
        datos(dict): Diccionario con los valores actualzados.
    
    """
    if datos["errores"] < 2 and datos["rta"] == rta_correcta and not(datos["rta_acertada"]):
        datos["puntaje"] += 10
        datos["rta"] = ""
        datos["rta_acertada"] = True
    elif datos["errores"] < 1 and datos["rta"] != datos["1er_intento"] and not(datos["rta_acertada"]):
        datos["errores"] += 1
        datos["1er_intento"] = datos["rta"]
    elif datos["errores"] < 2 and datos["rta"] != datos["1er_intento"] and not(datos["rta_acertada"]):
        datos["errores"] += 1
        datos["2do_intento"] = datos["rta"]
    
    return(datos)

def reinciar_datos(datos_juego: dict, datos_sonidos: dict):
    """ 
    Reinicia los valores del juego.
    
    Args: 
        datos_juego(dict): Diccionario con los valores a reiniciar.
        datos_sonidos:
        
    Returns:
        datos(dict): Diccionario con los valores reiniciados.
    
    """
    datos_juego["nro_preg"] = 0
    datos_juego["puntaje"] = 0
    datos_juego["errores"] = 0
    datos_juego["rta"] = ""
    datos_juego["1er_intento"] = ""
    datos_juego["2do_intento"] = ""
    datos_juego["rta_acertada"] = False 
    datos_juego["mostrar_preg"] = True 
    datos_sonidos["sonido_1er_errada"] = True
    datos_sonidos["sonido_preg_errada"] = True
    datos_sonidos["sonido_rta_correcta"] = True
    datos_sonidos["sonido_final"] = True

    
    return (datos_juego, datos_sonidos)

def centrar_etiquetas(etiquetas: list, rectangulos: list):
    """ 
    Calcula la posición centrada de varias etiquetas.
    
    Args: 
        etiquetas(list): Lista con los etiquetas a centrar.
        rectangulos(list): Lista con los rectangulos donde centrar.
        
    Returns:
        pos_rtas(list): Lista con las posiciones centradas de las etiquetas.
    
    """
    pos_rtas = []
    
    for indice in range(len(etiquetas)):
        pos_rtas.append(centrar_etiqueta(rectangulos[indice].centerx, rectangulos[indice].centery,etiquetas[indice]))
    
    return(pos_rtas)

def centrar_etiqueta(centerx, centery, etiqueta):
    """ 
    Centra una etiqueta.
    
    Args: 
        centerx: Valor de la coordenada x del centro.
        centry: Valor de la coordenada y del centro.
        
    Returns:
        pos_et: Coordenadas del texto centradas.
    
    """
    pos_et = etiqueta.get_rect()
    pos_et.centerx = centerx
    pos_et.centery = centery
    
    return(pos_et)

def pintar_rta_seleccionada(pantalla, btns: list, fondo, eleccion, opciones):
    """
    Pinta el boton clickeado del color recibido por parametro.

    Args:
        pantalla: Superficie donde dibujar el rectangulo. 
        btns: Lista de los botones.
        color: Color a pintar.
        eleccion: Boton clickeado.
    """
    for indice in range(len(opciones)):
        if eleccion == opciones[indice]:
            pantalla.blit(fondo, btns[indice])
          
def reinicio_preg_nueva(datos: dict, flags: dict, datos_sonidos: dict):
    """ 
    Reinicia los valores correspondientes al cambiar de pregunta.
    
    Args: 
        datos(dict): Diccionario con los valores a reiniciar.
        flags(dict): Diccionario con los flags a reiniciar.
    Returns:
        datos(dict): Diccionario con los valores reiniciados.
        flags(dict): Diccionario con los valores reiniciados.
    """
    if flags["juego_comenzado"]:
        datos["nro_preg"] += 1
        flags["mostrar_preg"] = True 
    else:
        flags["mostrar_preg"] = True
        flags["mostrar_rtas"] = True
        flags["juego_comenzado"] = True 
        
        
    datos["errores"] = 0
    datos["rta"] = ""
    datos["1er_intento"] = ""
    datos["2do_intento"] = ""
    datos["rta_acertada"] = False 
    
    datos_sonidos["sonido_1er_errada"] = True
    datos_sonidos["sonido_preg_errada"] = True
    datos_sonidos["sonido_rta_correcta"] = True
    datos_sonidos["sonido_final"] = True
    
    return (datos, flags, datos_sonidos)

def blitear_btns_rtas(pantalla, btns: list, fondo):
    """ 
    Añade en pantalla los botones de respuestas.
    
    Args: 
        pantalla: Superficie donde añadir los botones.
        btns(list): Lista con la cantidad de botones a añadir.
        fondo: Fondo de los botones.
    """
    for btn in btns:
        pantalla.blit(fondo, btn)

def cursor_en_btn(btns:list, pos_cursor):
    for btn in btns:
        if btn.collidepoint(pos_cursor):
            return btn
        
def pintar_btn_con_cursor(pantalla, btns:list, fondo, btn_con_cursor):
    for btn in btns:
        if btn == btn_con_cursor:
            pantalla.blit(fondo, btn)