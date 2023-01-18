import random
class Barcos_ia:

    def __init__(self, radar):
        self.radar = radar
        self.barcos = {"acorazado": 5, "portaaviones": 4, "crucero": 3, "submarino": 2, "destructor": 2}

    def colocar_barcos(self):
        for barco_elegido, longitud in self.barcos.items():
            posicion_ocupada = True
            while posicion_ocupada:
                posicion_ocupada = False
                orientacion = random.choice(['h', 'v'])
                if orientacion == 'h':
                    fila = random.randint(0, self.radar.height - 1)
                    columna = random.randint(0, self.radar.width - longitud)
                    for i in range(longitud):
                        if (fila, columna + i) in self.radar.barcos_ia:
                            posicion_ocupada = True
                            break
                    if posicion_ocupada:
                        continue
                    for i in range(longitud):
                        self.radar.barcos_ia.append((fila, columna + i))
                else:
                    fila = random.randint(0, self.radar.height - longitud)
                    columna = random.randint(0, self.radar.width - 1)
                    for i in range(longitud):
                        if (fila + i, columna) in self.radar.barcos_ia:
                            posicion_ocupada = True
                            break
                    if posicion_ocupada:
                        continue
                    for i in range(longitud):
                        self.radar.barcos_ia.append((fila + i, columna))