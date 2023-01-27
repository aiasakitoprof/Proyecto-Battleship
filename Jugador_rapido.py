import random
from Jugador import Tablero
from colorama import Fore, Style

class Barcos_rapidos: # Creamos la clase barcos ia
    
    def __init__(self, tablero): # Definicion del objeto barcos ia
        self.tablero = tablero
        self.barcos = {"acorazado": 5, "portaaviones": 4, "crucero": 3, "submarino": 3, "destructor": 2} # Diccionario con barcos y sus longitudes
    
    def colocar_barcos_rapidos(self): # Definimos la funcion de la colocacion de barcos la cual se hara aleatoriamente
        for barco_elegido, longitud in self.barcos.items(): # Recorremos los barcos en el diccionario "self.barcos"
            posicion_ocupada = True # Posicion ocupada la inicializamos en true
            while posicion_ocupada:     #Utilizamos este ciclo para asegurarnos que la posicion elegida no esta ocupada
                posicion_ocupada = False
                orientacion = random.choice(['h', 'v']) #Elegimos orientacion aleatoria
                if orientacion == 'h': # Si la orientacion elegida es horizontal
                    fila = random.randint(0, self.tablero.height - 1)   # Elegimos posicion aleatoria
                    columna = random.randint(0, self.tablero.width - longitud)
                    for i in range(longitud):   #Verificamos si la posicion esta ocupada
                        if self.tablero.tablero[fila][columna + i] != "·":
                            posicion_ocupada = True
                            break
                    if posicion_ocupada:
                        continue
                    for i in range(longitud):
                        self.tablero.tablero[fila][columna + i] = Fore.YELLOW + barco_elegido[0].upper() + Style.RESET_ALL  # Colocamos el barco en el tablero
                else:   # Si la orientacion elegida es vertical
                    fila = random.randint(0, self.tablero.height - longitud)    # Elegimos poscion aleatoria en el tablero
                    columna = random.randint(0, self.tablero.width - 1) 
                    for i in range(longitud): # Verificamos si la posicion esta ocuapda
                        if self.tablero.tablero[fila + i][columna] != "·":  # Si esta ocupada se estalablece posion_ocupada 'True'
                            posicion_ocupada = True 
                            break   # Se saldria del bucle for y se estableceria una nueva posicion
                    if posicion_ocupada:    # De lo contrario seguiriamos el bucle para colocar el barco
                        continue
                    for i in range(longitud):
                        self.tablero.tablero[fila + i][columna] = Fore.YELLOW + barco_elegido[0].upper() + Style.RESET_ALL # Colocamos el barco en el tablero