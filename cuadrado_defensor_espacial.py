#Librerias que vamos a utilizar
#Gestión de multiples aspectos de juegos basicos y avanzados
import pygame
#Manejo de eventos aleatorios
import random
#Manejo de evento en la consola de comandos
import sys

# Inicializar PyGame
pygame.init()

# Configuración de la ventana
ANCHO = 800 #Determinar el ancho de la ventana
ALTO = 600 #Determinar el alto de la ventana
VENTANA = pygame.display.set_mode((ANCHO, ALTO)) #Creación de la ventana con estas dimensiones
#Titulo del juego que se mostrara en la ventana del jugador
pygame.display.set_caption("Defensor Espacial Cuadratico")

# Colores
NEGRO = (0, 0, 0) #Fondo 
BLANCO = (255, 255, 255) #Disparos
ROJO = (255, 0, 0) #Enemigos
AZUL = (0, 0, 255) #Jugador

# Fuentes de los textos utilizados en el juego
fuente = pygame.font.SysFont("Arial", 36)

# Jugador
jugador_img = pygame.Surface((50, 30))
jugador_img.fill(AZUL) #Colorear el jugador
jugador_x = ANCHO // 2 #Coordena del eje X
jugador_y = ALTO - 50 #Coordena del eje Y
velocidad_jugador = 7  #Velocidad de movimiento del jugador en dos dimensiones

# Balas
balas = [] #Cartucho de balas
velocidad_bala = -7 #Velocidad de movimiento del disparo

# Enemigos
enemigos = [] #Lista que guarda las posiciones de los enemigos
velocidad_enemigos = 2 #Velocidad de movimiento de los enemigos
for i in range(5): #Se crean 5 enemigos
    #Generar enemigos con tamaños y coordenadas aleatorias, para despues agregarlos a la lista de enemigos
    enemigos.append(pygame.Rect(random.randint(0, ANCHO-40), random.randint(-100, -40), 40, 40))

# Estado del juego
menu_activo = True #Permite alternar entre el menu y el juego
juego_activo = False #Permite activar o desactivar el juego
instrucciones_activas = False #Permite alternar entre las instrucciones y el juego
puntaje = 0 #Puntaje del jugador

# -------- FUNCIONES PERSONALIZADAS --------
def mostrar_texto(texto, x, y, color=BLANCO):
    etiqueta = fuente.render(texto, True, color) #Renderizar el texto con la fuente y el color
    VENTANA.blit(etiqueta, (x, y)) #Ubicar en el texto en la posición solicitada

def mostrar_menu():
    VENTANA.fill(NEGRO)
    mostrar_texto("SPACE DEFENDER", 250, 150)
    mostrar_texto("1. Jugar", 300, 250)
    mostrar_texto("2. Instrucciones", 300, 300)
    mostrar_texto("3. Salir", 300, 350)
    pygame.display.update() #Actualizar la ventana despues de una interacción del jugador

def mostrar_instrucciones():
    VENTANA.fill(NEGRO)
    mostrar_texto("Instrucciones:", 280, 100)
    mostrar_texto("Mueve la nave con ← →", 200, 200)
    mostrar_texto("Dispara con ESPACIO", 200, 250)
    mostrar_texto("Pulsa ESC para volver al menú", 200, 350)
    pygame.display.update()

def mover_jugador(keys, x):
    if keys[pygame.K_LEFT] and x > 0: #Si el jugador presiona la tecla izquierda y el valor de x es mayor a 0, puede mover el cuadrado
        x -= velocidad_jugador #Actualización del valor de x, despues de moverse a la izqueirda
    if keys[pygame.K_RIGHT] and x < ANCHO - 50: #Si el jugador presiona la tecla derecha y el valor de x es menor al ancho - 50, puede mover el cuadrado
        x += velocidad_jugador #Actualización del valor de x, despues de moverse a la derecha
    return x #Devuelve el valor de x

def disparar(keys, lista_balas, x, y):
    if keys[pygame.K_SPACE]:# Si el jugador presiona la tecla espacio, puede disparar
        if len(lista_balas) < 5:  # límite de balas en pantalla
            lista_balas.append(pygame.Rect(x+20, y, 10, 20)) #Recargar el cartucho de disparso, indepiendente de la posición del jugador

def mover_balas(lista_balas):
    for bala in lista_balas[:]: #Recorre una lista de elementos copiada de la original
        bala.y += velocidad_bala  #Actualización de la velocidad del disparo
        if bala.y < 0:
            lista_balas.remove(bala) #Eliminar el disparo si sale del eje Y
            
def generar_enemigos(lista_enemigos):
    for enemigo in lista_enemigos: #Recorre la lista de enemigos
        enemigo.y += velocidad_enemigos #Actualización del valor de la velocidad del enemigo
        if enemigo.y > ALTO: #Si sale del eje Y, generar un nuevo enemigo
            enemigo.x = random.randint(0, ANCHO-40)
            enemigo.y = random.randint(-100, -40)

def colisiones(lista_balas, lista_enemigos):
    global puntaje
    for bala in lista_balas[:]:
        for enemigo in lista_enemigos[:]:
            if bala.colliderect(enemigo):
                lista_balas.remove(bala) #Desaparecer el disparo
                lista_enemigos.remove(enemigo) #Desaparecer el enemigo
                lista_enemigos.append(pygame.Rect(random.randint(0, ANCHO-40), random.randint(-100, -40), 40, 40)) #Generar un nuevo enemigo
                puntaje += 10 #Actualizar el puntaje
                break #Salir del bucle, de manera que no se repiten las colisiones

def dibujar_juego(x, y, lista_balas, lista_enemigos):
    VENTANA.fill(NEGRO)
    VENTANA.blit(jugador_img, (x, y))

    for bala in lista_balas:
        pygame.draw.rect(VENTANA, BLANCO, bala) #Dibujar los disparos

    for enemigo in lista_enemigos:
        pygame.draw.rect(VENTANA, ROJO, enemigo) #Dibujar los enemigos

    mostrar_texto(f"Puntaje: {puntaje}", 10, 10) #Mostrar el puntaje
    
    pygame.display.update()

