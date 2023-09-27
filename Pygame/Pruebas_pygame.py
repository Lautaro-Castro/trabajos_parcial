import pygame
from pruebas_constantes import *
from pruebas_funciones_pygame import *

pygame.init()
pygame.mixer.init()
dic_datos_juego = {"puntaje": 0, "rta": "", "1er_intento": "", "2do_intento": "", "errores": 0, "nro_preg": 0, "rta_acertada": False}
dic_flags = {"ejecutar": True, "mostrar_preg": False, "mostrar_rtas": False, "juego_comenzado": False, "musica_on": True}
dic_sonidos = {"sonido_1er_errada": True, "sonido_preg_errada": True, "sonido_rta_correcta": True, "sonido_final": True}

pygame.mixer.music.play(-1)    

while dic_flags["ejecutar"]:
    
    pos_cursor = pygame.mouse.get_pos()
    pantalla.blit(image_fondo, (0,0))
    pantalla.blit(imagen_btn_reiniciar, btn_reiniciar)  
    if dic_flags["musica_on"]:
        pantalla.blit(image_musica_on, pos_btn_musica)
    else:
        pantalla.blit(image_musica_off, pos_btn_musica)
    btn_con_cursor = cursor_en_btn([btn_reiniciar], pos_cursor)
    pintar_btn_con_cursor(pantalla, [btn_reiniciar], imagen_cursor_en_btn_reiniciar, btn_con_cursor)
    pantalla.blit(et_btn_reiniciar, pos_et_reiniciar)  
    
    if dic_datos_juego["nro_preg"] < len(lista_preguntas):
        rtas_actuales = [lista_rtas_a[dic_datos_juego["nro_preg"]], lista_rtas_b[dic_datos_juego["nro_preg"]], lista_rtas_c[dic_datos_juego["nro_preg"]]]
        rta_correcta_actual = lista_rtas_correctas[dic_datos_juego["nro_preg"]]
        
        pantalla.blit(imagen_btn_pregunta, btn_pregunta)  
        btn_con_cursor = cursor_en_btn([btn_pregunta], pos_cursor)
        pintar_btn_con_cursor(pantalla, [btn_pregunta], imagen_cursor_en_btn, btn_con_cursor)
        pantalla.blit(et_boton_pregunta, pos_et_btn_pregunta)  
        etiqueta_score = fuente_score.render(f"Score: {dic_datos_juego['puntaje']}", True, AMARILLO_CLARO)
        pantalla.blit(etiqueta_score, pos_etiqueta_score)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            dic_flags["ejecutar"] = False
            
        if evento.type == pygame.MOUSEBUTTONDOWN:
            
            posicion_click = list(evento.pos)
            
            if btn_musica.collidepoint(posicion_click) and dic_flags["musica_on"]:
                pygame.mixer.music.set_volume(0)
                dic_flags["musica_on"] = False
            elif btn_musica.collidepoint(posicion_click):
                pygame.mixer.music.set_volume(0.1)
                dic_flags["musica_on"] = True
                
            if btn_pregunta.collidepoint(posicion_click):      
                
                if dic_datos_juego["nro_preg"] < len(lista_preguntas):
                    pygame.mixer.Sound.play(sonido_sig_preg) 
                    dic_datos_juego, dic_flags, dic_sonidos = reinicio_preg_nueva(dic_datos_juego, dic_flags, dic_sonidos)
                
                else:
                    dic_flags["mostrar_preg"] = False
                    
                    
            dic_datos_juego["rta"] = validar_click_en_rta(dic_flags["mostrar_rtas"], posicion_click, parametros_rtas, dic_datos_juego["rta"])
            
            if btn_reiniciar.collidepoint(posicion_click) and dic_flags["juego_comenzado"]:
                pygame.mixer.Sound.play(sonido_reinicio) 
                dic_datos_juego, dic_sonidos = reinciar_datos(dic_datos_juego, dic_sonidos) 
                
                
    
    if dic_flags["mostrar_preg"]:
        
        if dic_datos_juego["nro_preg"] < len(lista_preguntas):
            
            et_preg = fuente_pregunta.render(lista_preguntas[dic_datos_juego["nro_preg"]], True, MARRON)
            pos_et_preg = centrar_etiqueta(pantalla.get_rect().centerx, 300, et_preg)
            pos_fondo_preg = centrar_etiqueta(pantalla.get_rect().centerx, pantalla.get_rect().centery, imagen_fondo_preg)
            pantalla.blit(imagen_fondo_preg, pos_fondo_preg)
            pantalla.blit(et_preg, pos_et_preg)
            
            if dic_flags["mostrar_rtas"]:
                
                blitear_btns_rtas(pantalla, btns_rtas, imagen_btn_normal)
                btn_con_cursor = cursor_en_btn(btns_rtas, pos_cursor)
                pintar_btn_con_cursor(pantalla, btns_rtas, imagen_cursor_en_btn, btn_con_cursor)
                
                
                if dic_datos_juego["errores"] > 0:
                    if dic_sonidos["sonido_1er_errada"]:
                        pygame.mixer.Sound.play(sonido_1er_error)
                        dic_sonidos["sonido_1er_errada"] = False
                    pintar_rta_seleccionada(pantalla, btns_rtas, imagen_btn_rta_incorrecta, dic_datos_juego["1er_intento"], opciones_rtas)
                    
                    if dic_datos_juego["errores"]  > 1:
                        if dic_sonidos["sonido_preg_errada"]:
                            pygame.mixer.Sound.play(sonido_preg_errada)
                            dic_sonidos["sonido_preg_errada"] = False
                        pintar_rta_seleccionada(pantalla, btns_rtas, imagen_btn_rta_incorrecta, dic_datos_juego["2do_intento"], opciones_rtas)
                        
                        
                    if dic_datos_juego["1er_intento"] != "" and dic_datos_juego["2do_intento"] != "":
                        
                        pos_et_preg_errada = centrar_etiqueta(pantalla.get_rect().centerx, pantalla.get_rect().centery - 90, et_errores)
                        pos_et_pasar_sig_preg = centrar_etiqueta(pantalla.get_rect().centerx, pantalla.get_rect().centery - 70, et_errores_2)
                        blitear_varias_etiquetas(pantalla, [et_errores, et_errores_2], [pos_et_preg_errada, pos_et_pasar_sig_preg])
                        
                if  dic_datos_juego["rta_acertada"]:
                    if dic_sonidos["sonido_rta_correcta"]:
                        pygame.mixer.Sound.play(sonido_rta_correcta)
                        dic_sonidos["sonido_rta_correcta"] = False
                    pintar_rta_seleccionada(pantalla, btns_rtas, imagen_btn_rta_correcta, lista_rtas_correctas[dic_datos_juego["nro_preg"]], opciones_rtas)
                    

                    pos_et_preg_acertada = centrar_etiqueta(pantalla.get_rect().centerx, pantalla.get_rect().centery - 90, et_correcto)
                    pos_et_pasar_sig_preg = centrar_etiqueta(pantalla.get_rect().centerx, pantalla.get_rect().centery - 70, et_correcto_2)
                    blitear_varias_etiquetas(pantalla, [et_correcto, et_correcto_2], [pos_et_preg_acertada, pos_et_pasar_sig_preg])
                    
                etiquetas_rtas = renderizar_varias_etiquetas(fuente_rtas, rtas_actuales , True, MARRON)
                pos_rtas = centrar_etiquetas(etiquetas_rtas, btns_rtas)
                blitear_varias_etiquetas(pantalla, etiquetas_rtas, pos_rtas)
                
                dic_datos_juego = validar_rta(dic_datos_juego, rta_correcta_actual)
        
    if dic_datos_juego["nro_preg"] == len(lista_preguntas):
        if dic_sonidos["sonido_final"]:
            pygame.mixer.Sound.play(sonido_final)
            dic_sonidos["sonido_final"] = False
        et_game_over = fuente_game_over.render("GAME OVER", True, AMARILLO_CLARO)
        pos_game_over = centrar_etiqueta(pantalla.get_rect().centerx, pantalla.get_rect().centery, et_game_over)
        et_game_over_2 = fuente_game_over.render(f"SU PUNTAJE ES: {dic_datos_juego['puntaje']}/{len(lista_preguntas) *10}", True, AMARILLO_CLARO)
        pos_game_over_2 = centrar_etiqueta(pantalla.get_rect().centerx, pantalla.get_rect().centery + 50, et_game_over_2)
        blitear_varias_etiquetas(pantalla, [et_game_over, et_game_over_2], [pos_game_over, pos_game_over_2])   

    pygame.display.flip()
    
pygame.quit
