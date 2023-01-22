import random
# He creado las siguientes listas para facilitar la información del usuario
# y decidir quien ha ganado la partida
acorazado_ia=[]
portaaviones_ia=[]
crucero_ia=[]
submarino_ia=[]
destructor_ia=[]
todos_barcos_ia={}

class Radar:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.radar = [["·" for i in range(width)] for i in range(height)]
        self.coordenadas_barcos_ia = []
        # En la siguiente lista guardo las coordenadas del barco en formato string
        self.coordenadas_barcos_computer=[]

    def view_radar(self):
        print("  ", end="")
        for i in range(self.width):
            print(i, end=" ")
        print()
        for i, row in enumerate(self.radar):
            print(i, end=" ")
            print(" ".join(row))

class Barcos_ia:
    def __init__(self, radar):
        self.radar = radar
        self.barcos = {"acorazado": 5, "portaaviones": 4, "crucero": 3, "submarino": 2, "destructor": 2}

    def colocar_barcos_ia(self):
        for barco_elegido, longitud in self.barcos.items():
            posicion_ocupada = True
            while posicion_ocupada:
                posicion_ocupada = False
                orientacion = random.choice(['h', 'v'])
                if orientacion == 'h':
                    fila = random.randint(0, self.radar.height - 1)
                    columna = random.randint(0, self.radar.width - longitud)
                    for i in range(longitud):
                        if (fila, columna + i) in self.radar.coordenadas_barcos_ia:
                            posicion_ocupada = True
                            break
                    if posicion_ocupada:
                        continue
                    for i in range(longitud):
                        self.radar.coordenadas_barcos_ia.append((fila, columna + i))
                        # Proceso para guardar las coordenadas del ordenador
                        self.radar.coordenadas_barcos_computer.append(str(fila)+str(columna+i))
                        coordenadas=str(fila)+str(columna+i)
                        if barco_elegido=="acorazado":
                            acorazado_ia.append(coordenadas)
                        if barco_elegido=="portaaviones":
                            portaaviones_ia.append(coordenadas)
                        if barco_elegido=="crucero":
                            crucero_ia.append(coordenadas)
                        if barco_elegido=="submarino":
                            submarino_ia.append(coordenadas)
                        if barco_elegido=="destructor":
                            destructor_ia.append(coordenadas)
                else:
                    fila = random.randint(0, self.radar.height - longitud)
                    columna = random.randint(0, self.radar.width - 1)
                    for i in range(longitud):
                        if (fila + i, columna) in self.radar.coordenadas_barcos_ia:
                            posicion_ocupada = True
                            break
                    if posicion_ocupada:
                        continue
                    for i in range(longitud):
                        self.radar.coordenadas_barcos_ia.append((fila + i, columna))
                        #Proceso para guardar las coordenadas del ordenador
                        self.radar.coordenadas_barcos_computer.append(str(fila+i)+str(columna))
                        coordenadas=str(fila+i)+str(columna)
                        if barco_elegido=="acorazado":
                            acorazado_ia.append(coordenadas)
                        if barco_elegido=="portaaviones":
                            portaaviones_ia.append(coordenadas)
                        if barco_elegido=="crucero":
                            crucero_ia.append(coordenadas)
                        if barco_elegido=="submarino":
                            submarino_ia.append(coordenadas)
                        if barco_elegido=="destructor":
                            destructor_ia.append(coordenadas)
                    # Finalmente guardamos los barcos con sus coordenadas en un diccionario
                    todos_barcos_ia["acorazado"]=acorazado_ia
                    todos_barcos_ia["portaaviones"]=portaaviones_ia
                    todos_barcos_ia["crucero"]=crucero_ia
                    todos_barcos_ia["submarino"]=submarino_ia
                    todos_barcos_ia["destructor"]=destructor_ia