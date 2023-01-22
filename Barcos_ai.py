import random
class Barcos_ia: # Creamos la clase Barcos_ia

    def __init__(self, radar):  # Definicion del obljeto barcos_ia
        self.radar = radar  # se asigna un objeto de la clase radar
        self.barcos = {"acorazado": 5, "portaaviones": 4, "crucero": 3, "submarino": 2, "destructor": 2} # Diccionario con barcos y sus longitudes

    def colocar_barcos(self): # Definimos la funcion de la colocacion de barcos la cual se hara aleatoriamente
        for barco_elegido, longitud in self.barcos.items(): # Recorremos los barcos en el diccionario "self.barcos"
            posicion_ocupada = True # Posicion ocupada la inicializamos en true
            while posicion_ocupada:  #Utilizamos este ciclo para asegurarnos que la posicion elegida no esta ocupada
                posicion_ocupada = False
                orientacion = random.choice(['h', 'v']) #Elegimos orientacion aleatoria
                if orientacion == 'h':  # Si la orientacion elegida es horizontal
                    fila = random.randint(0, self.radar.height - 1) # Elegimos posicion aleatoria
                    columna = random.randint(0, self.radar.width - longitud)
                    for i in range(longitud):   # Verificamos si la posicion esta ocupada
                        if (fila, columna + i) in self.radar.barcos_ia: # Si la posicion elegida esta ocupada
                            posicion_ocupada = True # Se establece posicion en True
                            break
                    if posicion_ocupada: # Sino esta ocupada se coloca el barco en el radar
                        continue
                    for i in range(longitud):
                        self.radar.barcos_ia.append((fila, columna + i))
                else:
                    fila = random.randint(0, self.radar.height - longitud)  #Se elige una posicion aleatoria en el radar
                    columna = random.randint(0, self.radar.width - 1)
                    for i in range(longitud):
                        if (fila + i, columna) in self.radar.barcos_ia:
                            posicion_ocupada = True
                            break
                    if posicion_ocupada:
                        continue
                    for i in range(longitud):
                        self.radar.barcos_ia.append((fila + i, columna)) # Si no esta ocupada se coloca el barco en el radar


                       