from funciones_stark import *
from data_stark import *

opciones = ["a", "b", "c", "d", "e", "f"]
run = True

while run:
    
    opcion = menu_stark_1(opciones).lower().strip()
    
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
            print("Gracias por utilizar el programa")
            run = False
        