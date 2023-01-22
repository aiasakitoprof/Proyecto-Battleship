# import random
# class Tablero:

#     def __init__(self, width=10, height=10): # Definición del objeto tablero.
#         self.height = height
#         self.width = width
#         self.tablero = [["·" for i in range(width)] for i in range(height)] # Bucle para crear el tablero.
#         self.barcos_colocados = {} # Guarda los barcos ya colocados.
#         self.coordenadas_barcos_ia = []
    
#     def view_tablero(self): # Printeo de tablero.
        
#         print("  ", end="") # Hueco separador de coordenadas.
        
#         for i in range(len(self.tablero[0])): # Coordenadas de columnas (Encima del tablero).
#             print(i, end=" ")
#         print()
        
#         for i, row in enumerate(self.tablero): # Coordenadas de filas (A la derecha del tablero).
#             print(i, end=" ")
#             print(" ".join(row))
    
#     def barco_colocado(self, barco):
#         self.barcos_colocados[barco] = True

# class Barcos_ia:
#     def __init__(self, tablero):
#         self.tablero = tablero
#         self.barcos = {"acorazado": 5, "portaaviones": 4, "crucero": 3, "submarino": 2, "destructor": 2}

#     def colocar_barcos_ia(self):
#         for barco_elegido, longitud in self.barcos.items():
#             posicion_ocupada = True
#             while posicion_ocupada:
#                 posicion_ocupada = False
#                 orientacion = random.choice(['h', 'v'])
#                 if orientacion == 'h':
#                     fila = random.randint(0, self.tablero.height - 1)
#                     columna = random.randint(0, self.tablero.width - longitud)
#                     for i in range(longitud):
#                         if (fila, columna + i) in self.tablero.coordenadas_barcos_ia:
#                             posicion_ocupada = True
#                             break
#                     if posicion_ocupada:
#                         continue
#                     for i in range(longitud):
#                         self.tablero.coordenadas_barcos_ia.append((fila, columna + i))
#                 else:
#                     fila = random.randint(0, self.tablero.height - longitud)
#                     columna = random.randint(0, self.tablero.width - 1)
#                     for i in range(longitud):
#                         if (fila + i, columna) in self.tablero.coordenadas_barcos_ia:
#                             posicion_ocupada = True
#                             break
#                     if posicion_ocupada:
#                         continue
#                     for i in range(longitud):
#                         self.tablero.coordenadas_barcos_ia.append((fila + i, columna))

# tablero = Tablero()
# barcos_ia = Barcos_ia(tablero)
# barcos_ia.colocar_barcos_ia()
# print(tablero.coordenadas_barcos_ia)

import random
class Tablero: # Creamos la clase tablero
    def __init__(self, width=10, height=10): # Definición del objeto tablero.
        self.height = height # En el se define el ancho y alto del tablero definidos en 10.
        self.width = width
        self.tablero = [["·" for i in range(width)] for i in range(height)] # Bucle para crear el tablero.

    def view_tablero(self): # Printeo de tablero.
        
        print("  ", end="") # Hueco separador de coordenadas.
        
        for i in range(len(self.tablero[0])): # Coordenadas de columnas (Encima del tablero).
            print(i, end=" ")
        print()
        
        for i, row in enumerate(self.tablero): # Coordenadas de filas (A la derecha del tablero).
            print(i, end=" ")
            print(" ".join(row))
class Barcos_ia: # Creamos la clase barcos ia
    def __init__(self, tablero): # Definicion del objeto barcos ia
        self.tablero = tablero
        self.barcos = {"acorazado": 5, "portaaviones": 4, "crucero": 3, "submarino": 2, "destructor": 2} # Diccionario con barcos y sus longitudes
    def colocar_barcos_ia(self): # Definimos la funcion de la colocacion de barcos la cual se hara aleatoriamente
        for barco_elegido, longitud in self.barcos.items(): # Recorremos los barcos en el diccionario "self.barcos"
            posicion_ocupada = True # Posicion ocupada la inicializamos en true
            while posicion_ocupada:     #Utilizamos este ciclo para asegurarnos que la posicion elegida no esta ocupada
                posicion_ocupada = False
                orientacion = random.choice(['h', 'v'])
                if orientacion == 'h':
                    fila = random.randint(0, self.tablero.height - 1)
                    columna = random.randint(0, self.tablero.width - longitud)
                    for i in range(longitud):
                        if self.tablero.tablero[fila][columna + i] != "·":
                            posicion_ocupada = True
                            break
                    if posicion_ocupada:
                        continue
                    for i in range(longitud):
                        self.tablero.tablero[fila][columna + i] = barco_elegido[0].upper()
                else:
                    fila = random.randint(0, self.tablero.height - longitud)
                    columna = random.randint(0, self.tablero.width - 1)
                    for i in range(longitud):
                        if self.tablero.tablero[fila + i][columna] != "·":
                            posicion_ocupada = True
                            break
                    if posicion_ocupada:
                        continue
                    for i in range(longitud):
                        self.tablero.tablero[fila + i][columna] = barco_elegido[0].upper()
tablero = Tablero()
barcos_ia = Barcos_ia(tablero)
barcos_ia.colocar_barcos_ia()
tablero.view_tablero()