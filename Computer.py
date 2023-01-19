from Tablero_computer import *
import random
total_coordenadas=[]
class BarcosComputer:
    #Esta clase me permite colocar los navios en posiciones random
    def __init__(self, board): # Llamada al objeto tablero.

        self.board = board # Importa el tablero
        self.barcos = {"1": 4,  "2": 3, "3": 2,} # Diccionario con los barcos y sus longitudes.

    def colocar_barcos(self):

        coordenadas=[]
        
        global total_coordenadas

        barcosRandom = ["1","2","3"]
        while len(self.board.barcos_colocados) < len(self.barcos): # Premisa, si no están todos los barcos colocados seguimos ejecutando.
            #Elegimos un barco del array, cada número pertenece a un navio diferente
            barco_elegido =random.choice(barcosRandom) # Selector de barcos.
            longitud = self.barcos[barco_elegido] # Extraemos su longitud

            if barco_elegido in self.board.barcos_colocados: # Comprobamos que no esté ya colocado.
                #print(f"El barco {barco_elegido} ya esta colocado.") # <== Si lo está.
                continue
            barco_colocado = False
            #Guardamos los datos en el diccionario de cada navio
            if barco_elegido == "1":
                acorazado["id"]="1"
                acorazado["L"]=longitud
            elif barco_elegido == "2":
                crucero["id"]="2"
                crucero["L"]=longitud
            elif barco_elegido=="3":
                submarino["id"]="3"
                submarino["L"]=longitud

            while barco_colocado==False: # Si no está colocado.
                orientacion=["v","h"]
                #El ordenador elige una orientación al azar
                orientacionRandom = random.choice(orientacion)
                #print("orientacion",orientacionRandom) # Atributos del barco.
                #El ordenador elige una fila random entre 0 y 9
                fila =random.randint(0,9)
                #print("fila",fila)
                #El ordenador elige una columna random entre 0 y 9
                columna = random.randint(0,9)
                #print("columna",columna)
                # Antes de pasar a poner los barcos en el tablero comprobamos que se puedan colocar en la posición especificada.
                if orientacionRandom == "h" and columna + longitud > 10: # Si queremos poner el barco en horizontal.
                    #print(f"Barco {barco_elegido} fuera del tablero, en fila.{columna+longitud}")
                    barco_colocado=False

                elif orientacionRandom == "v" and  fila + longitud > 10:                              # Realizamos la misma operación si queremos que el barco esté en vertical.
                    #print(f"Barco {barco_elegido} fuera del tablero, en columna. {fila+longitud}")
                    barco_colocado=False
                else:
                    barco_colocado=True
                # Guardamos la orientación de cada navio en su diccionario correspondiente
                if barco_elegido == "1":
                    acorazado["orienta"]=orientacionRandom
                elif barco_elegido == "2":
                    crucero["orienta"]=orientacionRandom
                elif barco_elegido=="3":
                    submarino["orienta"]=orientacionRandom
                # Procedemos a colocar los barcos.
                posicion_ocupada = False
                bucle_activo = True

            while bucle_activo:

                    if orientacionRandom == "h": # Si la orientación es horizontal.

                        for i in range(longitud): # Rango = longitud del barco.
                            #print("longitud",longitud)
                            #print("barco",barco_elegido,"columna",columna+i)
                            #print("posicion fila",fila, "posicion columna",columna,"i",i,"columna + i",columna+i)
                            if self.board.board[fila][columna + i] != ".": # Si la posición de inicio del barco es diferente al agua.
                                #print("Posición ocupada.")
                                posicion_ocupada = True
                                bucle_activo=False
                                coordenadas=[]

                    elif orientacionRandom == "v":  # Si la orientación es vertical.

                        for i in range(longitud): # Rango = longitud del barco.
                            #print(longitud)
                            #print("barco",barco_elegido,"fila",fila+i)
                            # print(self.board.board[fila + i][columna])
                            #print("posicion fila",fila, "i",i,"fila+i",fila+i,"columna",columna)
                            if self.board.board[fila + i][columna] != ".":  # Si la posición de inicio del barco es diferente al agua.
                                #print("Posición ocupada.")

                                posicion_ocupada = True
                                bucle_activo = False
                                coordenadas=[]
                    if not posicion_ocupada: # Si la posición no está ocupada.
                        if orientacionRandom == "h": # Orientación horizontal.
                            for i in range(longitud): # Rango = longitud del barco.
                                #print("columna",columna,"i",i)
                                self.board.board[fila][columna + i] = barco_elegido[0] # Sustituimos el agua de las coordenadas por el barco.
                                # Guardamos las coordenadas de cada navio en su diccionario
                                # correspondiente, es necesario tener un array de coordenadas
                                # para introducirlas posteriormente en el diccionario
                                coordenadas.append(str(fila)+str(columna+i))
                                total_coordenadas.append(str(fila)+str(columna+i))
                                if barco_elegido == "1":
                                    acorazado["coordenadas"]=coordenadas
                                elif barco_elegido == "2":
                                    crucero["coordenadas"]=coordenadas
                                elif barco_elegido == "3":
                                    submarino["coordenadas"]=coordenadas
                            barco_colocado = True
                            coordenadas=[]

                            self.board.barco_colocado(barco_elegido) # Guardamos el barco para que no se pueda colocar de nuevo.

                        elif orientacionRandom == "v": # Orientación Vertical.
                            for i in range(longitud): # Rango = longitud del barco.
                                #print("fila",fila,"i",i)
                                self.board.board[fila+i][columna] = barco_elegido[0] # Sustituimos el agua de las coordenadas por el barco.
                                # Guardamos las coordenadas de cada navio en su diccionario
                                # correspondiente, es necesario tener un array de coordenadas
                                # para introducirlas posteriormente en el diccionario
                                coordenadas.append(str(fila+i)+str(columna))
                                total_coordenadas.append(str(fila+i)+str(columna))
                                if barco_elegido == "1":
                                    acorazado["coordenadas"]=coordenadas
                                elif barco_elegido == "2":
                                    crucero["coordenadas"]=coordenadas
                                elif barco_elegido == "3":
                                    submarino["coordenadas"]=coordenadas
                            barco_colocado = True
                            coordenadas=[]

                            self.board.barco_colocado(barco_elegido) # Guardamos el barco para que no se pueda colocar de nuevo.

            # Mostramos las coordenadas del ordenador para detectar errores, no mostrar en el juego definitivo
            #print("Computer",total_coordenadas)