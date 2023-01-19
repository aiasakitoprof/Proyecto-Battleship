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
        self.barcos = {"acorazado": 5, "portaaviones":4, "crucero": 3, "submarino": 2, "destructor":2,} # Diccionario con los barcos y sus longitudes.

    def colocar_barcos(self):
        
        while len(self.tablero.barcos_colocados) < len(self.barcos): # Premisa, si no están todos los barcos colocados seguimos ejecutando.
            
            clear_terminal()
            self.tablero.view_tablero()
            barco_elegido = input("Elige el barco a colocar (acorazado, portaaviones, crucero, submarino o destructor): ") # Selector de barcos.
            longitud = self.barcos[barco_elegido] # Extraemos su longitud
            
            if barco_elegido in self.tablero.barcos_colocados: # Comprobamos que no esté ya colocado.
                print(f"El barco {barco_elegido} ya esta colocado.") # <== Si lo está.
                continue
            barco_colocado = False
            
            while not barco_colocado: # Si no está colocado.
                orientacion = input("Orientación (v/h): ") # Atributos del barco.
                fila = int(input("Fila colocación: "))
                columna = int(input("Columna Colocación: "))
                
                # Comprobación de orientación.
                if orientacion not in ["v", "h"]: # Comprobación de errores
                    print("Orientación inválida")
                    continue
                
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
                        barco_colocado = True
                        self.tablero.barco_colocado(barco_elegido)
                        print(f"Barco {barco_elegido} colocado en posición {fila}, {columna} con orientación horizontal.")
                        
                    elif orientacion == "v":
                        for i in range(longitud):
                            self.tablero.tablero[fila + i][columna] = barco_elegido[0]
                        barco_colocado = True
                        self.tablero.barco_colocado(barco_elegido)
                        print(f"Barco {barco_elegido} colocado en posición {fila}, {columna} con orientación vertical.")