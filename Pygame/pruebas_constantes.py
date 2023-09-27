import pygame
from datos import lista
from funciones_pygame import *

pygame.init()
pygame.mixer.init()

#VENTANA
ancho_ventana = 800
alto_ventana = 600

image_fondo = pygame.image.load("fondo.jpg")
pygame.mixer.music.load("musica_fondo.wav")
pygame.mixer.music.set_volume(0.1)

sonido_rta_correcta = pygame.mixer.Sound("rta_correcta.wav")
pygame.mixer.Sound.set_volume(sonido_rta_correcta, 0.2)

sonido_preg_errada = pygame.mixer.Sound("preg_errada.wav")
pygame.mixer.Sound.set_volume(sonido_preg_errada, 0.2)

sonido_sig_preg = pygame.mixer.Sound("sig_preg.wav")
pygame.mixer.Sound.set_volume(sonido_sig_preg, 0.2)

sonido_1er_error = pygame.mixer.Sound("1er_error.wav")
pygame.mixer.Sound.set_volume(sonido_1er_error, 0.2)

sonido_final = pygame.mixer.Sound("final.mp3")
pygame.mixer.Sound.set_volume(sonido_final, 0.2)

sonido_reinicio = pygame.mixer.Sound("reinicio.mp3")
pygame.mixer.Sound.set_volume(sonido_reinicio, 0.2)



#BOTONES
pos_btn_pregunta = (300, 30)
tam_btn_pregunta = (200, 60)
pos_et_btn_pregunta = (335, 43)
imagen_btn_pregunta = pygame.image.load("boton_pregunta.png")

pos_btn_reiniciar = (10, 10)
tam_btn_reiniciar = (100, 30)
pos_et_reiniciar = (26, 16)
imagen_btn_reiniciar = pygame.image.load("boton_reiniciar.png")
imagen_cursor_en_btn_reiniciar = pygame.image.load("cursor_en_boton_reiniciar.png")

pos_btn_musica = (15, 45)
tam_btn_musica = (50,50)

pos_etiqueta_score = (620, 20)

pos_boton_rta_a = (75, 400)
tam_boton_rta_a = (200, 60)

pos_boton_rta_b = (300, 400)
tam_boton_rta_b = (200, 60)

pos_boton_rta_c = (525, 400)
tam_boton_rta_c = (200, 60)


pos_rta_a = (80, 400)
pos_rta_b = (305, 400)
pos_rta_c = (530, 400)

imagen_btn_normal = pygame.image.load("boton_normal.png")
imagen_cursor_en_btn = pygame.image.load("cursor_en_boton.png")
imagen_btn_rta_correcta = pygame.image.load("boton_rta_correcta.png")
imagen_btn_rta_incorrecta = pygame.image.load("boton_rta_incorrecta.png")
image_musica_on = pygame.image.load("music_on.png")
image_musica_off = pygame.image.load("music_off.png")

imagen_fondo_preg = pygame.image.load("fondo_preg.png")

opciones_rtas = ["a", "b", "c"]

#COLORES
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 102, 153)
CELESTE = (173, 216, 230)
COLOR_BTN_PREGUNTA = (200, 200, 200)
ROJO = (250, 181, 173)
VERDE = (173, 250, 173)
GRIS_OSCURO = (47, 47, 47)
GRIS_CLARO = (200, 200, 200)
MARRON = (100, 57, 41)
AMARILLO_CLARO = (255, 255, 153)
NARANJA = (255, 102, 0)
LIRIO = (255, 0, 255)
ROSA = (255, 0, 200)
CIAN = (0, 176, 246)

#DEFINIR FUENTES
fuente_boton_pregunta = pygame.font.SysFont("Times New Roman", 30, True)
fuente_score = pygame.font.SysFont("Times New Roman", 30, True)
fuente_reinicar = pygame.font.SysFont("Times New Roman", 16, True)
fuente_pregunta = pygame.font.SysFont("Times New Roman", 25, True)
fuente_rtas = pygame.font.SysFont("Times New Roman", 21, True)
fuente_game_over = pygame.font.SysFont("Times New Roman", 50, True)

#BOTONES
btn_pregunta = pygame.Rect(pos_btn_pregunta, tam_btn_pregunta)
btn_reiniciar = pygame.Rect(pos_btn_reiniciar, tam_btn_reiniciar) 
btn_rta_a = pygame.Rect(pos_boton_rta_a, tam_boton_rta_a) 
btn_rta_b = pygame.Rect(pos_boton_rta_b, tam_boton_rta_b)
btn_rta_c = pygame.Rect(pos_boton_rta_c, tam_boton_rta_c)
btns_rtas = [btn_rta_a, btn_rta_b, btn_rta_c]
btn_musica = pygame.Rect(pos_btn_musica, tam_btn_musica)

#LISTADO DE ELEMENTOS
lista_preguntas = listar_datos(lista, "pregunta")
lista_rtas_a = listar_datos(lista, "a")
lista_rtas_b = listar_datos(lista, "b")
lista_rtas_c = listar_datos(lista, "c")
lista_rtas_correctas = listar_datos(lista, "correcta")

#ETIQUETAS
et_boton_pregunta = fuente_boton_pregunta.render("Pregunta", True, BLANCO)
et_btn_reiniciar = fuente_reinicar.render("Reiniciar", True, AMARILLO_CLARO)
et_errores = fuente_rtas.render("Maximo de errores alcanzado.", True, ROJO)
et_errores_2 = fuente_rtas.render("Presione en 'Pregunta' para pasar a la siguiente.", True, ROJO)
et_correcto = fuente_rtas.render("¡Respuesta correcta! Suma 10 ptos.", True, VERDE)
et_correcto_2 = fuente_rtas.render("Presione en 'Pregunta' para pasar a la siguiente.", True, VERDE)

#DEFINIR PANTALLA
pantalla = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Juego")

#PARAMETROS REPUESTAS
parametros_rtas = [{"rta": "a", "pos": btn_rta_a },{"rta": "b", "pos": btn_rta_b },{"rta": "c", "pos": btn_rta_c}]


