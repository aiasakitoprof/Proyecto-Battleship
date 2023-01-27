from colorama import Fore, Style
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
        self.width = width
        self.height = height
        self.tablero = [["·" for i in range(width)] for i in range(height)] # Bucle para crear el tablero.
        self.barcos_colocados = {} # Guarda los barcos ya colocados.
    
    def view_tablero(self): # Printeo de tablero.
        
        print(Fore.BLUE +"          Tablero" +Style.RESET_ALL)
        print(Fore.CYAN +"    0 1 2 3 4 5 6 7 8 9" +Style.RESET_ALL) # Cabecera del tablero
        print("  ┌─────────────────────┐")
        
        for i, row in enumerate(self.tablero): # Coordenadas de filas (A la derecha del tablero).
            print(Fore.CYAN+ str(i) + Style.RESET_ALL, end=" │ ")
            print(" ".join(row),"│")
        
        print("  └─────────────────────┘") # Pie del tablero.
    
    def barco_colocado(self, barco):
        self.barcos_colocados[barco] = True

class Barcos:

    def __init__(self, tablero): # Llamada del objeto tablero.
        
        self.tablero = tablero # Importa el tablero.
        self.barcos_input = {0:"acorazado", 1:"portaaviones", 2:"crucero", 3:"submarino", 4:"destructor",} # Acceso rápido a los barcos.
        self.barcos = {"acorazado": 5, "portaaviones":4, "crucero": 3, "submarino": 3, "destructor":2,} # Diccionario con los barcos y sus longitudes.
        
    def colocar_barcos(self):
        
        while len(self.tablero.barcos_colocados) < len(self.barcos): # Premisa, si no están todos los barcos colocados seguimos ejecutando.
            
            clear_terminal()
            self.tablero.view_tablero()
            barco_elegido = input("Elige el barco a colocar (0 = acorazado,  1 = portaaviones, 2 = crucero, 3 = submarino, 4 = destructor)\n\n >  ") # Selector de barcos.
            
            while barco_elegido not in ["0","1","2","3","4"]:
                clear_terminal()
                self.tablero.view_tablero()
                barco_elegido = input("Elige una opción válida (0 = acorazado,  1 = portaaviones, 2 = crucero, 3 = submarino, 4 = destructor)\n\n >  ") # Selector de barcos.
            barco_elegido = int(barco_elegido)
            
            longitud = self.barcos[self.barcos_input[barco_elegido]] # Extraemos su longitud
            
            while barco_elegido in self.tablero.barcos_colocados: # Comprobamos que no esté ya colocado.
                
                clear_terminal()
                self.tablero.view_tablero()
                barco_elegido = input("Elige otro barco a colocar (0 = acorazado,  1 = portaaviones, 2 = crucero, 3 = submarino, 4 = destructor)\n\n >  ")
                while barco_elegido not in ["0","1","2","3","4"]:
                    clear_terminal()
                    self.tablero.view_tablero()
                    barco_elegido = input("Elige una opción válida (0 = acorazado,  1 = portaaviones, 2 = crucero, 3 = submarino, 4 = destructor)\n\n >  ") # Selector de barcos.
                barco_elegido = int(barco_elegido)
                continue
            
            barco_colocado = False
            
            while not barco_colocado: # Si no está colocado.
                
                # --------| Atributos del barco |--------

                clear_terminal()
                self.tablero.view_tablero()
                orientacion = input(f"Barco elegido: {self.barcos_input[barco_elegido]}, Lon: {self.barcos[self.barcos_input[barco_elegido]]} \n\nElige la oriantación del barco (v/h). El barco siempre se orienta de proa a popa.\n\n >  ") # Orientación (siempre se orienta de proa a popa).
                
                while orientacion not in ["v","h"]: # Control de errores.
                    clear_terminal()
                    self.tablero.view_tablero()
                    orientacion = input(f"Barco elegido: {self.barcos_input[barco_elegido]}, Lon: {self.barcos[self.barcos_input[barco_elegido]]} \n\nElige una oriantación válida (v/h).\nRecuerda que barco siempre se orienta de proa a popa.\n\n >  ")
                

                clear_terminal()
                self.tablero.view_tablero()
                coord = input(f"Barco elegido: {self.barcos_input[barco_elegido]}, Lon: {self.barcos[self.barcos_input[barco_elegido]]} / Oriantación elegida: {orientacion}\n\nIntroduce la coordenada para colocar el barco (ejemplo: '00')\n\n >  ")
                
                while True:
                    
                    if len(coord) == 2:
                        if coord[0] in ["0","1","2","3","4","5","6","7","8","9"]:
                            if coord[1] in ["0","1","2","3","4","5","6","7","8","9"]:
                                break
                    clear_terminal()
                    self.tablero.view_tablero()
                    coord = input(f"Barco elegido: {self.barcos_input[barco_elegido]}, Lon: {self.barcos[self.barcos_input[barco_elegido]]} / Oriantación elegida: {orientacion}\n\nIntroduce la coordenada válidas para colocar el barco (ejemplo: '00')\n\n >  ")

                fila = int(coord[0])
                columna = int(coord[1])

                if orientacion == "h" and (columna + longitud > len(self.tablero.tablero[0])): # Si queremos poner el barco en hoizontal.
                    print("Barco fuera del tablero.")                                          # Comprobamos que el barco no sobresalga del tablero. Premisa: Si sumamos la longitud del
                    continue                                                                   # barco al numero de la columna y supera la longitud de la fila, está fuera del tablero
                                                                                               # Al ser un cuadrado no importa la fila con la que se realice la comprobación.

                if orientacion == "v" and (fila + longitud > len(self.tablero.tablero)): # Realizamos la misma operación si queremos que el barco esté en vertical.  
                    print("Barco fuera del tablero.")                                    # Premisa: Si sumamos la longitud del barco al número de la fila y el resultado            
                    continue                                                             # es mayor que la longitud del tablero (Si su índice es mayor que el del tablero), está fuera del tablero.                                     
                
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
                            self.tablero.tablero[fila][columna + i] = Fore.YELLOW + self.barcos_input[barco_elegido][0].upper() + Style.RESET_ALL
                        barco_colocado = True
                        self.tablero.barco_colocado(barco_elegido)
                        print(f"Barco {self.barcos_input[barco_elegido]} colocado en posición {fila}, {columna} con orientación horizontal.")
                        
                    elif orientacion == "v":
                        for i in range(longitud):
                            self.tablero.tablero[fila + i][columna] =  Fore.YELLOW + self.barcos_input[barco_elegido][0].upper() + Style.RESET_ALL
                        barco_colocado = True
                        self.tablero.barco_colocado(barco_elegido)
                        print(f"Barco {self.barcos_input[barco_elegido]} colocado en posición {fila}, {columna} con orientación vertical.")