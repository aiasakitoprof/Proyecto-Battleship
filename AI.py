import random

class Radar:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.radar = [["·" for i in range(width)] for i in range(height)]  # Matriz del radar.
        self.coordenadas_barcos_ia = []  # Lista para los barcos de la ia.

class Barcos_ia:
    def __init__(self, radar):
        self.radar = radar
        self.barcos = {"acorazado": 5, "portaaviones": 4, "crucero": 3, "submarino": 2, "destructor": 2}  # Posibles barcos.

    def colocar_barcos_ia(self):
        for barco_elegido, longitud in self.barcos.items():  # Seleccionamos barco y longitud.
            posicion_ocupada = True  # Bool de control.
            while posicion_ocupada:
                posicion_ocupada = False
                orientacion = random.choice(['h', 'v'])  # Seleccion aleatoria de orientación.
                if orientacion == 'h':  # Horizontal.
                    fila = random.randint(0, self.radar.height - 1)  # Coordenadas de posición aleatorias.
                    columna = random.randint(0, self.radar.width - longitud)
                    for i in range(longitud):  # Rango = longitud del barco.
                        if (fila, columna + i) in self.radar.coordenadas_barcos_ia:  # Si durante el bucle se sale del tablero rompemos el bucle.
                            posicion_ocupada = True
                            break
                    if posicion_ocupada:  # En caso positivo reiniciamos.
                        continue
                    for i in range(longitud):
                        self.radar.coordenadas_barcos_ia.append((fila, columna + i))  # En caso de poderse colocar guardamos las coordenadas en la lista.
                else:  # Vertical
                    fila = random.randint(0, self.radar.height - longitud)
                    columna = random.randint(0, self.radar.width - 1)  # Coordenadas de posición aleatorias.
                    for i in range(longitud):  # Rango = longitud del barco.
                        if (fila + i, columna) in self.radar.coordenadas_barcos_ia:  # Si durante el bucle se sale del tablero rompemos el bucle.
                            posicion_ocupada = True
                            break
                    if posicion_ocupada:  # En caso positivo reiniciamos.
                        continue
                    for i in range(longitud):
                        self.radar.coordenadas_barcos_ia.append((fila + i, columna))   # En caso de poderse colocar guardamos las coordenadas en la lista.