import pygame
from pygame.locals import *
import PySimpleGUI as sg
import random
import os
import sys
pygame.init()
#Medidas de la pantalla de juego
ANCHO = 1100
ALTO = 700

#Medida de una celda del tablero
cell_size = ANCHO/30
font = pygame.font.SysFont(None, 20)
texto=pygame.font.SysFont(None, 30)
tiradasPosibles= [(fila,columna) for fila in range(10) for columna in range(10)]
# En el diccionario de barcos tenemos el tipo de barco, su longitud y color por defecto
barcos={"acorazado": [5,(255,128,0)], "portaaviones":[4,(204,204,0)], "crucero": [3,(0,204,102)], "submarino": [2,(255,51,51)], "destructor":[2,(0,0,255)]}
# Diccionario creado para disponer de los indices para que cuando se colocan los barcos del usuario, no se vuelva a repetir el barco a colocar
barcos_indice={"1":["acorazado",5,(255,128,0)], "2":["portaaviones",4,(204,204,0)], "3":["crucero",3,(0,204,102)], "4":["submarino",2,(255,51,51)], "5":["destructor",2,(0,0,255)]}
# Con la siguiente lista verifico cual es el barco que se ha hundido
todos_barcos={}
# Lista para guardar las coordenadas de los barcos del usuario
coordenadas = []
# La misma lista pero en formato string, necesito esta lista para validar que no
# se vuelven a escoger las mismas coordenadas
coordenadas_str=[]
# Lista para guardar los disparos del ordenador, necesaria para la logica de tiro
disparos_realizados_ai=[]
# Coordenadas de los barcos del ordenador, necesaria para validar quien ha ganado
coordenadas_ia=[]
# Lista de disparos realizados por el usuario, necesaria para no volver a repetir la tirada
disparos_realizados_user=[]
# Lista que guarda los aciertos del ordenador, necesaria para la logica de tiro
aciertos_computer=[]
# Se guardan los barcos hundidos por el ordenador en una lista (actualmente esta lista no se emplea)
# Se podría emplear para cambiar el modo de indicar quien gana
barcos_hundidos=[]
# Listas para guardar las coordenadas de cada tipo de barco, estos se guardan en un diccionario
# en un diccionario
acorazado=[]
portaaviones=[]
crucero=[]
submarino=[]
destructor=[]
# Inicializamos el modo de tiro del ordenador a "buscar" (tirada random), en caso de que se haga 
# un acierto se cambiará el modo a "hundir"
modo="buscar"
# La opción de disparar se inicia con el turno del usuario
turno="usuario"
# Variable necesaria para validar cuantos tiros han sido aciertos, en caso de que haya más de uno
# Se priorizará el modo "hundir"
contadorTiros=0
# Variable necesaria para que no se pueda volver a colocar un barco que ya ha sido colocado
barco_actual_ia=1
barco_actual = 1
button=0
# Variable que indica que el modo de juego está activo
running=True
# Función que permite encontrar la ruta relativa del archivo
def resolver_ruta(ruta_relativa):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath('.'), ruta_relativa)
imagen=pygame.image.load(resolver_ruta("JUEGO_PYGAME/game_over.png"))
#Variable que inicia la ventana con las medidas definidas
screen = pygame.display.set_mode((ANCHO,ALTO))
#Título del juego que se muestra en la parte superior de la pantalla
pygame.display.set_caption("Hundir la flota")



# Actualizar la pantalla
pygame.display.update()

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


# Función que permite colocar los barcos del usuario
def colocar_barco(barcos, screen, cell_size, ANCHO, ALTO, coordenadas, coordenadas_str, barco_actual):
    # Bucle que recorre el diccionario de barcos y  recoge los valores necesarios
    for navio, valor in barcos_indice.items():
        indice=navio
        barco=valor[0]
        longitud =valor[1]
        color =  valor[2]
        # Validamos que el indice del barco sea igual que el barco que se debe colocar en cada momento,
        # en caso de que un barco sea colocado, la variable "barco_actual" se incrementa y no permite repetir barcos
        if indice == str(barco_actual):
        # Funcionalidad del paquete PySimpleGUI que me permite mostrar una pantalla para introducir datos
            layout = [[sg.Text("Seleccione orientacion (h/v) del barco actual "+str(barco_actual)), sg.InputText()],
                    [sg.Text("Seleccione fila (0-9)"), sg.InputText()],
                    [sg.Text("Seleccione columna (0-9): "), sg.InputText()],
                    [sg.Button(f"Colocar {barco}")]]
            
            # Funcionalidad que me introduce las caracteristicas de la ventana para introducir datos
            window = sg.Window(f"Colocar {barco} de longitud {longitud}", layout, location=(ANCHO/3, ALTO - 180), keep_on_top=True)
            # Se captura el evento y los valores introducidos antes de cerrar la ventana
            event, values = window.read()
            window.close()
            if event != f"Colocar {barco}":
                continue
            
            orientation = values[0]
            try:
                row = int(values[1])
                col = int(values[2])
                # CONTROL DE ERRORES
                # Validación de que los numeros introducidos por el usuario no se salen del rango
                if row<0 or row>9 or col<0 or col>9:
                    sg.popup("Números invalidos, debe introducir un rango entre 0 y 9", keep_on_top=True)
                    return colocar_barco(barcos, screen, cell_size, ANCHO, ALTO, coordenadas, coordenadas_str, barco_actual)
            # En caso de que introduzca letras en lugar de números
            except ValueError:
                sg.popup("Números invalidos, debe introducir un rango entre 0 y 9, ha introducido letras", keep_on_top=True)
                return colocar_barco(barcos, screen, cell_size, ANCHO, ALTO, coordenadas, coordenadas_str, barco_actual)
            # En caso de que introduzca otra letra
            if orientation not in ["v","h"]:
                sg.popup("Debe introducir una orientacion válida, v-vertical, h-horizontal.", keep_on_top=True)
                return colocar_barco(barcos, screen, cell_size, ANCHO, ALTO, coordenadas, coordenadas_str, barco_actual)

            if orientation == "h" and col + longitud >=11:
                sg.popup("El barco se sale del tablero.", keep_on_top=True)
                # El barco sale del tablero en fila
                return colocar_barco(barcos, screen, cell_size, ANCHO, ALTO, coordenadas, coordenadas_str, barco_actual)

            elif orientation == "v" and  row + longitud >=11:
                sg.popup("El barco se sale del tablero.", keep_on_top=True)
                # El barco sale del tablero en columna
                return colocar_barco(barcos, screen, cell_size, ANCHO, ALTO, coordenadas, coordenadas_str, barco_actual)
                    
            # Si la orientación es horizontal
            if orientation == "h":
                for i in range(longitud):
                    if (row, col+i) in coordenadas:
                        sg.popup("Este lugar esta ocupado, por favor selecciona otro.", keep_on_top=True)
                        # En caso de que la coordenada esté ocupada volvemos a inicializar la función
                        return colocar_barco(barcos, screen, cell_size, ANCHO, ALTO, coordenadas, coordenadas_str, barco_actual)
                    # Guardamos las coordenadas en las listas correspondientes
                    coordenadas.append((row, col+i))
                    coordenadas_str.append(str(row)+str(col+i))
                    #coordenadas_barcos.append(str(fila)+str(columna+i)
                    if barco=="acorazado":
                        acorazado.append(coordenadas_str)
                    if barco=="portaaviones":
                        portaaviones.append(coordenadas_str)
                    if barco=="crucero":
                        crucero.append(coordenadas_str)
                    if barco=="submarino":
                        submarino.append(coordenadas_str)
                    if barco=="destructor":
                        destructor.append(coordenadas_str)
                    # pinta los cuadrados de cada barco con el color y las medidas correspondientes
                    pygame.draw.rect(screen, color, (int((col+i)*cell_size)+80+ANCHO/2, int(row*cell_size)+80, cell_size, cell_size))
            elif orientation == "v":
                for i in range(longitud):
                    if (row+i, col) in coordenadas:
                        sg.popup("Este lugar esta ocupado, por favor selecciona otro.", keep_on_top=True)
                        return colocar_barco(barcos, screen, cell_size, ANCHO, ALTO, coordenadas, coordenadas_str, barco_actual)
                    coordenadas.append((row+i, col))
                    coordenadas_str.append(str(row+i)+str(col))
                    if barco=="acorazado":
                        acorazado.append(coordenadas_str)
                    if barco=="portaaviones":
                        portaaviones.append(coordenadas_str)
                    if barco=="crucero":
                        crucero.append(coordenadas_str)
                    if barco=="submarino":
                        submarino.append(coordenadas_str)
                    if barco=="destructor":
                        destructor.append(coordenadas_str)
                    pygame.draw.rect(screen, color, (int(col*cell_size)+80+ANCHO/2, int((row+i)*cell_size)+80, cell_size, cell_size))
            # Guardamos los barcos y sus coordenadas en un diccionario
            todos_barcos["acorazado"]=acorazado
            todos_barcos["portaaviones"]=portaaviones
            todos_barcos["crucero"]=crucero
            todos_barcos["submarino"]=submarino
            todos_barcos["destructor"]=destructor
            barco_actual+=1
            pygame.display.update()

def colocar_barcos_ia(barco_actual_ia):
    for navio, valor in barcos_indice.items():
        indice=navio
        barco=valor[0]
        longitud =valor[1]
        posicion_ocupada=True
        if indice == str(barco_actual_ia):
            while posicion_ocupada:
                orientacion = random.choice(['h', 'v'])
                fila =random.randint(0,9)
                columna = random.randint(0,9)
                # El valor de la suma no puede ser 11 o mayor a 11, ej. si longitud = 5
                # columna=5, la suma es 10, valido
                if orientacion == "h" and columna + longitud >=11:
                    # El barco sale del tablero en fila
                    continue
                # El valor de la suma no puede ser 11 o mayor a 11, ej. si longitud = 5
                # fila=5, la suma es 10, valido
                elif orientacion == "v" and  fila + longitud >=11:
                    # El barco sale del tablero en columna
                    continue
                    
                else:
                    # si la posición no está ocupada continua colocando el barco actual
                    posicion_ocupada=False
                    # Si la orientación es horizontal
                    if orientacion == 'h':
                        # Bucle que recorre el largo del barco y va colocandolo segun su orientación
                        for i in range(longitud):
                            # Si la fila y la columna+1 coinciden en algun momento del bucle con las coordenadas
                            # ya introducidas, vuelve a inicar el bucle
                            if (fila, columna + i) in coordenadas_ia:
                                posicion_ocupada = True
                                break
                        if posicion_ocupada:
                            continue
                        # En caso de que la posición no esté ocupada, guardamos las coordenadas del barco en la lista
                        for i in range(longitud):
                            coordenadas_ia.append((fila, columna + i))
                    elif orientacion == 'v':
                        for i in range(longitud):
                            if (fila + i, columna) in coordenadas_ia:
                                posicion_ocupada = True
                                break
                        if posicion_ocupada:
                            continue
                        for i in range(longitud):
                            coordenadas_ia.append((fila + i, columna))
                    # Incrementamos el valor del indice del barco para no volverlo a colocar
                    barco_actual_ia+=1
        
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

def posicion_azar():
        #En el modo "buscar" de la tirada del ordenador se realizan las siguientes
        # tiradas random
        fila = random.randint(0,9)
        columna = random.randint(0,9)
        return (fila,columna)

def buscar_alrededor():
        # Estrategias empleadas para favorecer que el ordenador sea más intuitivo
        # seleccionamos la fila y la columna de la ultima tirada acertada por el ordenador
        fila=int(aciertos_computer[-1][0])
        columna=int(aciertos_computer[-1][1])
        # Inicializamos la variable eleccion, que será el tiro que se ha elegido para disparar, según la lógica de la función
        eleccion=(fila,columna)
        # Dirección de la tirada consecutiva (0 = ninguna, 1 = horizontal, 2 = vertical
        direccion_tirada = 0
        # En caso de que "elección" no esté dentro de los disparos realizados por la ia
        while eleccion not in disparos_realizados_ai:
            # Si el tamaño de los aciertos es mayor a 1
            if len(aciertos_computer) > 1:
                # Comprueba si hay una fila o columna de tiradas acertadas consecutivas
                if aciertos_computer[-1][0] == aciertos_computer[-2][0]:
                    direccion_tirada = 1
                    #fila = int(self.aciertos_computer[-1][0])
                    # Verificamos que el número de columna no se salga del tablero
                    if columna+1 >9:
                        columna=columna-1
                    elif columna-1 <0:
                        columna=columna+1
                    else:
                        columna = random.choice([columna-1,columna+1])
                    eleccion=(fila,columna)
                # Comprobación de si hay dos aciertos en la misma columna
                elif aciertos_computer[-1][1] == aciertos_computer[-2][1]:
                    direccion_tirada = 2
                    columna = int(aciertos_computer[-1][1])
                    if fila+1 >9:
                        fila=fila-1
                    elif fila-1 <0:
                        fila=fila+1
                    else:
                        fila = random.choice([fila-1,fila+1])
                    eleccion=(fila,columna)
            else:
                # En caso de que no haya un número de aciertos mayor a 1, no sabremos
                # la dirección
                direccion_tirada = 0
                # En caso de que el tiro elegido esté dentro de los disparos ya realizados
                # la dirección será desconocida
            if eleccion in disparos_realizados_ai:
                direccion_tirada = 0
        # Si la dirección es desconocida seguimos la siguiente estrategia
        if direccion_tirada==0:
            # Creamos una lista de aproximaciones
            aproximaciones=[(fila-1,columna), (fila+1,columna), (fila,columna-1), (fila,columna+1)]
            # Creamos una lista de aproximaciones válidas, que serán las que no se salgan del tablero
            valid_aproximaciones = [aprox for aprox in aproximaciones if aprox[0] >= 0 and aprox[0] <= 9 and aprox[1] >= 0 and aprox[1] <= 9]
            # Mezclamos las aproximaciones para realizar una tirada al azar entre las aproximaciones validadas
            random.shuffle(valid_aproximaciones)
            for aprox in valid_aproximaciones:
                # Validamos que la aproximación no esté en los disparos ya realizados por el ordendor
                if aprox not in disparos_realizados_ai:
                    eleccion=aprox
                    break
                else:
                    # En caso contrario se eligira una tirada de las posiciones
                    # restantes
                    random.shuffle(tiradasPosibles)
                    for posibles in tiradasPosibles:
                        eleccion=posibles
                        break               
                    
        return eleccion


def disparo_ia(todos_barcos,coordenadas,tiradasPosibles):
        global modo
        global contadorTiros
        global turno
        # Inicializamos las variables del ambito del la función
        # Disparo que se realizará en el tablero
        disparo = 0
        # Fila donde se realizará el tiro
        fila=0
        # Columna donde se realizará el tiro
        columna=0
        # Booleano para indicar cuando inicia y acaba el disparo
        continuar=True

        while continuar:
            # print("modo activo", modo)
            # print("Contador Tiros", contadorTiros)
            if modo=="buscar":
                # En este modo hace una tirada al azar
                fila, columna = posicion_azar()
                #tiros = str(fila) + str(columna)
                disparo = (fila, columna)

                if disparo in disparos_realizados_ai:
                    continue
                # si los tiros no estan en el array de disparos, se guardaran
                # en sus listas correspondientes
                #self.disparos_computer.append(tiros)
                disparos_realizados_ai.append(disparo)
                # Si el tiro coincide con las coordenadas de los barcos, será
                # un acierto y se borrará de la lista de coordenadas
                if disparo in coordenadas:
                    aciertos_computer.append(disparo)
                    coordenadas.remove(disparo)
                    #Eliminamos los el tiro realizado de las tiradas posibles para 
                    # Validar en otra función que tiradas disponemos
                    tiradasPosibles.remove(disparo)
                    dibujar_acierto(fila, columna)
                    contadorTiros+=1
                    modo = "hundir"
                # if disparo in coordenadas_user:
                #     coordenadas_user.remove(disparo)
                    #disparar=False
                    # En el siguiente bucle comparamos los tiros con los valores
                    # del diccionario
                    for key, value in todos_barcos.items():
                            for element in value:
                                if element == disparo:
                                    # en caso de que haya un acierto se eliminará
                                    # del diccionario
                                    todos_barcos[key].remove(disparo)
                                # si el tamaño de la lista que corresponde al barco
                                # está vacia, el ordenador habrá undido un barco
                                if len(todos_barcos[key]) == 0:
                                    print(key, "undido")
                                    barcos_hundidos.append(key)
                                    modo = "buscar"
                else:
                    # En caso de fallo, mostramos el simbolo correspondiente en
                    # el tablero y lo añadimos a la lista de fallos
                    #self.fallos_computer.append(tiros)
                    print(disparo)
                    dibujar_fallo(fila, columna)
                    tiradasPosibles.remove(disparo)
                    print("Agua")
                    if contadorTiros>0:
                        modo = "hundir"
                    else:
                        modo = "buscar"
                
                    #disparar=False
            # En este modo intentamos hundir el barco
            elif modo == "hundir":
                # llamamos a la función buscar_alrededor que tiene la lógica de tiro
                fila,columna = buscar_alrededor()
                #tiros = str(fila) + str(columna)
                disparo = (fila, columna)
                # Si el tiro está en la lista volverá a tirar
                if disparo in disparos_realizados_ai:
                    continue
                # Se guardan los datos de disparo en las listas correspondientes
                #self.disparos_computer.append(tiros)
                disparos_realizados_ai.append(disparo)
                # Si el tiro ha sido un acierto se mostrará el simbolo correspondiente.
                # Se guarda en la lista de aciertos y se borra de las coordenadas del barco
                if disparo in coordenadas:
                    # Si el disparo coincide con una coordenada del barco del usuario
                    # sustituimos, marcamos la casilla con X
                    dibujar_acierto(fila, columna)
                    # Guardamos el acierto en la lista y borramos el acierto de la lista
                    # de coordenadas del usuario
                    aciertos_computer.append(disparo)
                    coordenadas.remove(disparo)
                    # Eliminamos el tiro de la lista de tiradas posibles
                    tiradasPosibles.remove(disparo)
                    contadorTiros+=1
                    modo="hundir"
                    #disparar=False
                    # Verificamos si el tiro ha hundido un barco
                    for key, value in todos_barcos.items():
                        for element in value:
                            if element == disparo:
                                todos_barcos[key].remove(disparo)
                            if len(todos_barcos[key]) == 0:
                                print(key, "undido")
                                # En caso de que se haya undido un barco lo guardamos
                                # en la lista de barcos hundidos
                                barcos_hundidos.append(key)
                                modo = "buscar"
                else:
                    # Si hay un disparo fallido lo marcamos con O
                    dibujar_fallo(fila, columna)
                    print("Agua")
                    # Eliminamos la tirada de las tiradas posibles
                    tiradasPosibles.remove(disparo)
                    if contadorTiros>0:
                        modo = "hundir"
                    else:
                        modo = "buscar"
                    #disparar=False
            
            # if contadorTiros==4:
            #     contadorTiros=0
            # Variable que cierra el bucle
            continuar = False
            turno="usuario"


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

# Función que permite realizar el disparo al usuario según las coordenadas introducidas
def disparo_user():
    global turno
    disparo=0
    fila=0
    columna=0
    continuar = True
    lista = [  [sg.Text("Seleccione fila (0-9): "), sg.InputText()],
                [sg.Text("Seleccione columna (0-9): "), sg.InputText()],
                [sg.Button("Disparar")]]
    vista = sg.Window("Ataque", lista, location=(ANCHO/3, ALTO - 180), keep_on_top=True, background_color='#ff0000')

    while continuar:
        # Validación para poder cerrar el juego y que no nos pida jugadas, en caso contrario realizaba todo el bucle
        if len(coordenadas)==0:
            break
        event, values = vista.read()
        if event in (sg.WIN_CLOSED, "Disparar"):
            if values[0] is not None and values[1] is not None:
                if values[0].isdigit() and values[1].isdigit():
                    fila = int(values[0])
                    columna = int(values[1])
                    disparo = (fila, columna)
                else:
                    sg.popup("Por favor, introduzca solo números enteros")
                    continue
        else:
            continue
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

# Calculamos el ancho de la pantalla para hallar el punto medio para pintar la imagen de game over
x = (ANCHO - imagen.get_width()) / 2
# Calculamos el alto de la pantalla para hallar el punto medio para pintar la imagen de game over
# y le sumamos 200 pixels
y = ((ALTO - imagen.get_height()) / 2)+200

def turnos():
    global turno
    running = True
    while running:
        if turno == "usuario":
            disparo_user()
            if len(coordenadas_ia) == 0:
                running = False
                print("Has ganado")
                sg.popup("Has ganado al ordenador, enhorabuena",  keep_on_top=True)
                # Cargamos la imagen de game over5 en el centro de la pantalla de pygame, pero en la posición inferior
                screen.blit(imagen, (x,y))
                break
            else:
                turno = "IA"
        else:
            disparo_ia(todos_barcos, coordenadas, tiradasPosibles)
            if len(coordenadas) == 0:
                running = False
                print("El ordenador ha ganado")
                sg.popup("El ordenador te ha ganado, puedes cerrar la ventana",  keep_on_top=True)
                # Cargamos la imagen de game over5 en el centro de la pantalla de pygame, pero en la posición inferior
                screen.blit(imagen, (x,y))
                break
            else:
                turno = "usuario"


colocar_barco(barcos, screen, cell_size, ANCHO, ALTO, coordenadas, coordenadas_str, barco_actual)

# Llamamos a la función que nos colocará los barcos del ordenador
colocar_barcos_ia(barco_actual_ia)
print("Coordenadas Ordenador",coordenadas_ia)
print(tiradasPosibles)
print("Coordenadas_usuario", coordenadas)
turnos()



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Funcionalidad de pygame que permite actualizar la visualización del juego
    pygame.display.update()
# Sale del juego
pygame.quit()

