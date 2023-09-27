from funciones_stark_2 import *
from data_stark import *

run = True

opciones = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]

while run:
    
    opcion = menu_stark_2(opciones)
    opcion.lower()
    
    match opcion:
        
        case "a":
            ejecutar_opcion_a(lista_personajes)
            
        case "b":
            ejecutar_opcion_b(lista_personajes)
            
        case "c":
            ejecutar_opcion_c(lista_personajes)
        
        case "d":
            ejecutar_opcion_d(lista_personajes)
            
        case "e":
            ejecutar_opcion_e(lista_personajes)
            
        case "f":
            ejecutar_opcion_f(lista_personajes)
            
        case "g":
            ejecutar_opcion_g(lista_personajes)
            
        case "h":
            ejecutar_opcion_h(lista_personajes)
        
        case "i":
            ejecutar_opcion_i(lista_personajes)
            
        case "j":
            ejecutar_opcion_j(lista_personajes)
            
        case "k":
            print("Gracias por utilizar el programa")
            run = False