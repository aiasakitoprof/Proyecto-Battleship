coordenadas_barcos=[]
acorazado=[]
portaaviones=[]
crucero=[]
submarino=[]
destructor=[]
todos_barcos={}

def clear_terminal():
    import os
    import platform
    if platform.system() == "Windows":
        clear = lambda: os.system('cls')
        clear()
    elif platform.system() == "Linux":
        clear = lambda: os.system('clear')
        clear()
    elif platform.system() == "Darwin":
        clear = lambda: os.system('clear')
        clear()

class Tablero:

    def __init__(self, width=10, height=10): # Definición del objeto tablero.
        
        self.tablero = [["·" for i in range(width)] for i in range(height)] # Bucle para crear el tablero.
        self.barcos_colocados = {} # Guarda los barcos ya colocados.
    
    def view_tablero(self): # Printeo de tablero.
        
        print("  ", end="") # Hueco separador de coordenadas.
        
        for i in range(len(self.tablero[0])): # Coordenadas de columnas (Encima del tablero).
            print(i, end=" ")
        print()
        
        for i, row in enumerate(self.tablero): # Coordenadas de filas (A la derecha del tablero).
            print(i, end=" ")
            print(" ".join(row))
    
    def barco_colocado(self, barco):
        self.barcos_colocados[barco] = True

class Barcos:

    def __init__(self, tablero): # Llamada del objeto tablero.
        
        self.tablero = tablero # Importa el tablero
        self.desc_barcos={"acorazado": 5, "portaaviones":4, "crucero": 3, "submarino": 2, "destructor":2,}
        self.barcos = {"1": 5, "2":4, "3": 3, "4": 2, "5":2,} # Diccionario con los barcos y sus longitudes.


    def colocar_barcos(self):
        
        while len(self.tablero.barcos_colocados) < len(self.barcos): # Premisa, si no están todos los barcos colocados seguimos ejecutando.
            clear_terminal()
            self.tablero.view_tablero()
            siSeleccion=False
            #Bucle para asegurarnos de que el usuario elige el barco de la lista
            while siSeleccion==False:
                barco_elegido = input("Elige el NÚMERO del barco a colocar (1-acorazado, 2-portaaviones, 3-crucero, 4-submarino o 5-destructor): ") # Selector de barcos.
                if barco_elegido not in self.barcos.keys():
                    print("Selección invalida, intente de nuevo")
                else:
                    siSeleccion=True
            longitud = self.barcos[barco_elegido] # Extraemos su longitud
            
            if barco_elegido in self.tablero.barcos_colocados: # Comprobamos que no esté ya colocado.
                print(f"El barco {barco_elegido} ya esta colocado.") # <== Si lo está.
                continue
            barco_colocado = False
            
            while not barco_colocado: # Si no está colocado.
                orientacion = input("Orientación (v/h): ") # Atributos del barco.
                #Control de errores en orientacion del barco
                if orientacion not in ["v","h"]:
                    print("Orientación invalida, introduzca v o h. vertical/horizontal")
                    barco_colocado=False
                else:
                    #Iniciamos la colocación de la fila
                    colocadoF=False
                    # Bucle de control de errores de la fila
                    while colocadoF==False:
                        try:
                            fila = int(input("Fila colocación: "))
                            if fila <0 or fila>9:
                                print("Debe introducir un valor entre 0 y 9")
                                colocadoF=False
                            else:
                                colocadoF=True
                        except ValueError:
                            print("Debe introducir un valor entre 0 y 9. Has introducido una letra.")
                            colocadoF=False
                        colocadoC=False
                    # Bucle de control de errores de la colummna
                    while colocadoC == False:
                        try:
                            columna = int(input("Columna Colocación: "))
                            if columna <0 or columna>9:
                                print("Debe introducir un valor entre 0 y 9")
                                colocadoC=False
                            else:
                                colocadoC=True
                        except ValueError:
                            print("Debe introducir un valor entre 0 y 9. Has introducido una letra")
                            colocadoC=False
                
                if orientacion == "h" and (columna + longitud > len(self.tablero.tablero[0])): # Si queremos poner el barco en hoizontal.
                    print("Barco fuera del tablero.") # Comprobamos que el barco no sobresalga del tablero. Premisa: Si sumamos la longitud del
                    continue                          # barco al numero de la columna y supera la longitud de la fila, está fuera del tablero
                                                # Al ser un cuadrado no importa la fila con la que se realice la comprobación.

                if orientacion == "v" and (fila + longitud > len(self.tablero.tablero)): # Realizamos la misma operación si queremos que el barco esté en vertical.  
                    print("Barco fuera del tablero.") # Premisa: Si sumamos la longitud del barco al número de la fila y el resultado            
                    continue                          # es mayor que la longitud del tablero (Si su índice es mayor que el del tablero), está fuera del tablero.                                     
                
                # Comprobación de coordenadas.
                posicion_ocupada = False
                for i in range(longitud): # Rango = longitud del barco.
                    if orientacion == "h": # Si la orientación es horizontal.
                        if self.tablero.tablero[fila][columna + i] != "·": # Si la posición de inicio del barco es diferente al agua.
                            print("Posición ocupada.")
                            posicion_ocupada = True
                            break
                    elif orientacion == "v": # Si la orientación es vertical.
                        if self.tablero.tablero[fila + i][columna] != "·":  
                            print("Posición ocupada.")
                            posicion_ocupada = True
                            break
                            
                # Colocación del barco
                if not posicion_ocupada: 
                    if orientacion == "h": 
                        for i in range(longitud): 
                            self.tablero.tablero[fila][columna + i] = barco_elegido[0]
                            coordenadas_barcos.append(str(fila)+str(columna+i))
                            coordenadas=str(fila)+str(columna+i)
                            if barco_elegido=="1":
                                acorazado.append(coordenadas)
                            if barco_elegido=="2":
                                portaaviones.append(coordenadas)
                            if barco_elegido=="3":
                                crucero.append(coordenadas)
                            if barco_elegido=="4":
                                submarino.append(coordenadas)
                            if barco_elegido=="5":
                                destructor.append(coordenadas)
                        barco_colocado = True
                        self.tablero.barco_colocado(barco_elegido)
                        print(f"Barco {barco_elegido} colocado en posición {fila}, {columna} con orientación horizontal.")
                        
                    elif orientacion == "v":
                        for i in range(longitud):
                            self.tablero.tablero[fila + i][columna] = barco_elegido[0]
                            coordenadas_barcos.append(str(fila+i)+str(columna))
                            coordenadas=str(fila+i)+str(columna)
                            if barco_elegido=="1":
                                acorazado.append(coordenadas)
                            if barco_elegido=="2":
                                portaaviones.append(coordenadas)
                            if barco_elegido=="3":
                                crucero.append(coordenadas)
                            if barco_elegido=="4":
                                submarino.append(coordenadas)
                            if barco_elegido=="5":
                                destructor.append(coordenadas)
                        barco_colocado = True
                        self.tablero.barco_colocado(barco_elegido)
                        todos_barcos["acorazado"]=acorazado
                        todos_barcos["portaaviones"]=portaaviones
                        todos_barcos["crucero"]=crucero
                        todos_barcos["submarino"]=submarino
                        todos_barcos["destructor"]=destructor
                        print(f"Barco {barco_elegido} colocado en posición {fila}, {columna} con orientación vertical.")