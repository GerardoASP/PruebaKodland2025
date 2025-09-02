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