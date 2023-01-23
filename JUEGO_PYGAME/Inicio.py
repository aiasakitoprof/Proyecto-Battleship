import pygame
from pygame.locals import *
import PySimpleGUI as sg
import random
pygame.init()
ANCHO = 1100
ALTO = 700
cell_size = ANCHO/30
font = pygame.font.SysFont(None, 20)
texto=pygame.font.SysFont(None, 30)
barcos={"acorazado": [5,(255,128,0)], "portaaviones":[4,(204,204,0)], "crucero": [3,(0,204,102)], "submarino": [2,(255,51,51)], "destructor":[2,(0,0,255)]}
barcos_colocados = {} # Guarda los barcos ya colocados.
coordenadas = []
disparos_realizados_ai=[]
coordenadas_ia=[]
disparos_realizados_user=[]
turno="usuario"

running=True


screen = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("Hundir la flota")



# Tablero 1
for i in range(0, 10):
    for j in range(0, 10):
        pygame.draw.circle(screen, (255,255,255), (int(i*cell_size)+100, int(j*cell_size)+100), 5)
        pygame.display.update()
        pygame.draw.rect(screen, (255,255,255), (0,0, ANCHO, ALTO), 2)

x = 74
y = 94

# Título del tablero 1
title = texto.render("Radar", True, (255, 255, 255))
screen.blit(title, (x+((cell_size*10)/2) - (title.get_width()/2), y-40-title.get_height()))
# Numeros del tablero 1 a la izquierda
for i in range(0, 10):
    text = font.render(str(i), True, (255, 255, 255))
    screen.blit(text, (x-font.size(str(i))[0], y + i*cell_size))

#  Numeros del tablero 1 en la parte superior
x = 85
for i in range(0, 10):
    text = font.render(str(i), True, (255, 255, 255))
    screen.blit(text, (x+i*cell_size+10, y-20-font.size(str(i))[1]))

x = 60
# Título del tablero 2
title = texto.render("Barcos", True, (255, 255, 255))
screen.blit(title, (x+((cell_size*10)/2) - (title.get_width()/2) + ANCHO/2, y-40-title.get_height()))

# Numeros a la izquierda del tablero 2
for i in range(0, 10):
    text = font.render(str(i), True, (255, 255, 255))
    screen.blit(text, (x+ANCHO/2+font.size(str(i))[0], y + i*cell_size))

# Numeros en la parte superior del tablero 2
x = 85
for i in range(0, 10):
    text = font.render(str(i), True, (255, 255, 255))
    screen.blit(text, (x+i*cell_size+10+ANCHO/2, y-20-font.size(str(i))[1]))

# Tablero 2
for i in range(0, 10):
    for j in range(0, 10):
        pygame.draw.circle(screen, (255,255,255), (int(i*cell_size)+100+ANCHO/2, int(j*cell_size)+100), 5)
        pygame.display.update()
        pygame.draw.rect(screen, (255,255,255), (0,0, ANCHO, ALTO), 2)




def dibujar_barco(orientation, row, col, size ,color):
    if orientation == "h":
        for i in range(size):
            pygame.draw.rect(screen, color, (int((col+i)*cell_size)+80+ANCHO/2, int(row*cell_size)+80, cell_size, cell_size))
            coordenadas.append((row, col+i))
    elif orientation == "v":
        for i in range(size):
            pygame.draw.rect(screen, color, (int(col*cell_size)+80+ANCHO/2, int((row+i)*cell_size)+80, cell_size, cell_size))
            coordenadas.append((row+i, col))
    pygame.display.update()




for navio in barcos.keys():
    barco_elegido=navio

    longitud = barcos[barco_elegido][0]
    color =  barcos[barco_elegido][1]

    # Funcionalidad del paquete PySimpleGUI que me permite mostrar una pantalla para introducir datos
    # del usuario
    layout = [[sg.Text("Seleccione orientacion (h/v): "), sg.InputText()],
            [sg.Text("Seleccione fila (0-9): "), sg.InputText()],
            [sg.Text("Seleccione columna (0-9): "), sg.InputText()],
            [sg.Button(f"Colocar {barco_elegido}")]]
    # Funcionalidad que me introduce las caracteristicas de la ventana para introducir datos
    # Donde se va a situar y que siempre va a estar por encima de la pantalla de pygame
    window = sg.Window(f"Colocar {barco_elegido}", layout,location=(ANCHO/3, ALTO - 180), keep_on_top=True)
    
    # Bucle que carga los datos del usuario y llama a la función de dibujar el barco con estos valores
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == f"Colocar {barco_elegido}":
            orientation = values[0]
            row = int(values[1])
            col = int(values[2])
            dibujar_barco(orientation, row, col, longitud, color) 
            window.close()
            break

print("Coordenadas_usuario", coordenadas)

# Colocamos los barcos del Ordenador de manera aleatoria
def colocar_barcos_ia():
    
        for barco_elegido, valor in barcos.items():
            barco_colocado=False
            while barco_colocado==False: # Si no está colocado.
                longitud = valor[0]
                posicion_ocupada = True
                while posicion_ocupada:
                    posicion_ocupada = False
                    orientacion = random.choice(['h', 'v'])
                    fila =random.randint(0,9)
                    columna = random.randint(0,9)
        
                    if orientacion == "h" and columna + longitud > 10: 
                        barco_colocado=False

                    elif orientacion == "v" and  fila + longitud > 10:
                        barco_colocado=False
                    else:
                        barco_colocado=True
                        if orientacion == 'h':

                            for i in range(longitud):
                                if (fila, columna + i) in coordenadas_ia:
                                    posicion_ocupada = True
                                break
                            if posicion_ocupada:
                                continue
                            for i in range(longitud):
                                coordenadas_ia.append((fila, columna + i))
                        else:
                            for i in range(longitud):
                                if (fila + i, columna) in coordenadas_ia:
                                    posicion_ocupada = True
                                    break
                            if posicion_ocupada:
                                continue
                            for i in range(longitud):
                                coordenadas_ia.append((fila + i, columna))

# Antes de dibujar el acierto del ordenador, se debe borrar el cuadrado del barco
def borrar_posicion(fila, columna):
    pygame.draw.rect(screen, (0,0,0), (int(columna*cell_size)+80+ANCHO/2, int(fila*cell_size)+80,cell_size,cell_size))
    pygame.display.update()

# Función que me permite dibujar una x verde cuando acierta
def dibujar_acierto(fila, columna):
    borrar_posicion(fila,columna)
    x1 = (columna * cell_size)+80+ANCHO/2 + (0.2 * cell_size)
    y1 = (fila * cell_size)+80 + (0.2 * cell_size)
    x2 = (columna * cell_size)+80+ANCHO/2 + (0.8 * cell_size)
    y2 = (fila * cell_size)+80 + (0.8 * cell_size)
    pygame.draw.line(screen, (0, 255, 0), (x1, y1), (x2, y2), 5)
    pygame.draw.line(screen, (0, 255, 0), (x1, y2), (x2, y1), 5)
    pygame.display.update()

# Función que me permite dibujar un circulo rojo cuando falla
def dibujar_fallo(fila, columna):
    pygame.draw.circle(screen, (255,0,0),  (int(columna*cell_size)+100+ANCHO/2, int(fila*cell_size)+100), 10)
    pygame.display.update()

# Función de disparo del ordenador
def disparo_ia():
    global turno
    continuar = True
    while continuar:
        fila = random.randint(0, 9)
        columna = random.randint(0, 9)
        disparo=(fila, columna)
        if disparo in disparos_realizados_ai:
            continue
        disparos_realizados_ai.append(disparo)
        if disparo in coordenadas:
            dibujar_acierto(fila, columna)
            coordenadas.remove(disparo)
        else:
            dibujar_fallo(fila, columna)
        continuar = False
        turno="usuario"



# Llamamos a la función que nos colocará los barcos del ordenador
colocar_barcos_ia()
print("Coordenadas Ordenador",coordenadas_ia)

# Antes de dibujar el acierto del usuario, se debe borrar el punto de agua
def borrar_posicion_ia(fila, columna):
    pygame.draw.circle(screen, (0,0,0),  (int(columna*cell_size)+100, int(fila*cell_size)+100), 10)
    pygame.display.update()

# Función que me permite dibujar una x verde cuando acierta
def dibujar_acierto_user(fila, columna):
    borrar_posicion_ia(fila, columna)
    x1 = (columna * cell_size)+80 + (0.2 * cell_size)
    y1 = (fila * cell_size)+80 + (0.2 * cell_size)
    x2 = (columna * cell_size)+80 + (0.8 * cell_size)
    y2 = (fila * cell_size)+80 + (0.8 * cell_size)
    pygame.draw.line(screen, (0, 255, 0), (x1, y1), (x2, y2), 5)
    pygame.draw.line(screen, (0, 255, 0), (x1, y2), (x2, y1), 5)
    pygame.display.update()


# Función que me permite dibujar un circulo rojo cuando falla
def dibujar_fallo_user(fila, columna):
    pygame.draw.circle(screen, (255,0,0),  (int(columna*cell_size)+100, int(fila*cell_size)+100), 10)
    pygame.display.update()

def disparo_user():
    global turno
    continuar = True
    lista = [  [sg.Text("Seleccione fila (0-9): "), sg.InputText()],
                [sg.Text("Seleccione columna (0-9): "), sg.InputText()],
                [sg.Button("Disparar")]]
    vista = sg.Window("Ataque", lista, location=(ANCHO/3, ALTO - 180), keep_on_top=True)

    while continuar:
        event, values = vista.read()
        if event in (sg.WIN_CLOSED, "Disparar"):
            fila = int(values[0])
            columna = int(values[1])
            disparo = (fila, columna)
            if disparo in disparos_realizados_user:
                sg.popup("Ese disparo ya ha sido realizado anteriormente. Por favor, seleccione otra posición.")
                continue
            else:
                disparos_realizados_user.append(disparo)
                if disparo in coordenadas_ia:
                    dibujar_acierto_user(fila, columna)
                    coordenadas_ia.remove(disparo)
                else:
                    dibujar_fallo_user(fila, columna)
                continuar = False
                vista.close()
                turno = "IA"



        


def turnos():
    global turno
    running = True
    while running:
        if turno == "usuario":
            disparo_user()
            if len(coordenadas_ia) == 0:
                running = False
                print("Has ganado")
                break
            else:
                turno = "IA"
        else:
            disparo_ia()
            if len(coordenadas) == 0:
                running = False
                print("El ordenador ha ganado")
                break
            else:
                turno = "usuario"


turnos()
# Bucle que permite seguir jugando
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Funcionalidad de pygame que permite actualizar la visualización del juego
    pygame.display.update()








