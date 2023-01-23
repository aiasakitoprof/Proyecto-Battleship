import random
import colorama
from tabulate import tabulate

# Creamos una clase para los barcos
class Ship:
    def __init__(self, name, length):
        self.name = name    # Nombre del barco
        self.length = length # Longitud del barco

# Creamos una clase para el tablero
class Board:
    def __init__ (self, name, size):
        self.name = name # Nombre del tablero
        self.rows = size[0] # Filas del tablero
        self.columns = size[1] # Columnas del tablero
        self.board = []  # Creamos una lista vacia para el tablero
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append("")      # Añadimos un espacio a cada posicion
            self.board.append(row)

    def print_board (self):
        # Creamos las cabeceras de las columnas
        header = []
        for i in range(self.columns):
            header.append(colorama.Fore.LIGHTMAGENTA_EX + str(i+0) + colorama.Fore.RESET) 
        # Creamos las cabeceras de las filas
        rows = []
        for i in range(self.rows):
            rows.append(colorama.Fore.LIGHTMAGENTA_EX + chr(i+65) + colorama.Fore.RESET) #Empezamos a partir del 65 que en ASCI es = a "A"

        table = self.board
        print(tabulate(table, header, showindex=rows, numalign="center", stralign="center", tablefmt="fancy_grid"))
         # Imprimimos el tablero formato tabulate con numeros y letras para las coordenadas
    def place_ship (self, ship):
        coordinates = [] # Creamos una lista para guardar las coordenadas de la ocupacion de los barcos
        unique = False  # Variable para verificar si se ha encontrado una posicion valida o no para el barco
        colorama.init()
        while unique != True:
            orientation = random.choice(["horizontal", "vertical"]) # Escoge una orientacion al azar para el barco
            if orientation == "horizontal":
            #Colocamos el barco horizontalmente
            #Nos aseguramos de que el punto de inicio no resulte en el barco siendo colocado fuera del mapa
                start = [random.randint(0,self.rows -1), random.randint(0, self.columns-ship.length)] 
                 # Escoge una posicion al azar para empezar a colocar el barco
                if start[1]+ship.length <= self.columns:
                     #Nos aseguramos de que el barco este entre los limites del tablero y no fuera
                    unique = True # Se devolvera el val true a unique
                    for i in range(ship.length): # En este bucle se comprueba si en cada posicion donde se coloque el barco esta vacia
                        if self.board[start[0]][start[1]+i] != "":
                            unique = False # Si alguna posicion estubiera ocupada se devolveria unique falso y se saldria del bucle
                            break
                if unique: # Si siguiera siendo verdadero
                    for i in range(ship.length):
                        if ship.name == "Acorazado":
                            self.board[start[0]][start[1]+i] = colorama.Fore.LIGHTYELLOW_EX + ship.name[0] + colorama.Fore.RESET
                        elif ship.name == "Portaaviones":
                            self.board[start[0]][start[1]+i] = colorama.Fore.CYAN + ship.name[0] + colorama.Fore.RESET
                        elif ship.name == "Crucero":
                            self.board[start[0]][start[1]+i] = colorama.Fore.RED + ship.name[0] + colorama.Fore.RESET
                        elif ship.name == "Submarino":
                            self.board[start[0]][start[1]+i] = colorama.Fore.GREEN + ship.name[0] + colorama.Fore.RESET
                        elif ship.name == "Destructor":
                            self.board[start[0]][start[1]+i] = colorama.Fore.BLUE + ship.name[0] + colorama.Fore.RESET
                        coordinates.append([start[0],start[1]+i]) # Se guardaria las coordenadar en la lista
            else:   # Ahora se haria el mismo bucle pero para la orientacion en vertical
                start = [random.randint(0,self.rows-ship.length), random.randint(0, self.columns-1)]
                if start[0]+ship.length <= self.rows:   
                    unique = True
                    for i in range(ship.length):
                        if self.board[start[0]+i][start[1]] != "":
                            unique = False
                            break
                if unique:
                    for i in range(ship.length):
                        if ship.name == "Acorazado":
                            self.board[start[0]+i][start[1]] = colorama.Fore.LIGHTYELLOW_EX + ship.name[0] + colorama.Fore.RESET
                        elif ship.name == "Portaaviones":
                            self.board[start[0]+i][start[1]] = colorama.Fore.CYAN + ship.name[0] + colorama.Fore.RESET
                        elif ship.name == "Crucero":
                            self.board[start[0]+i][start[1]] = colorama.Fore.RED + ship.name[0] + colorama.Fore.RESET
                        elif ship.name == "Submarino":
                            self.board[start[0]+i][start[1]] = colorama.Fore.GREEN + ship.name[0] + colorama.Fore.RESET
                        elif ship.name == "Destructor":
                            self.board[start[0]+i][start[1]] = colorama.Fore.BLUE + ship.name[0] + colorama.Fore.RESET
                        coordinates.append([start[0]+i,start[1]])
        colorama.deinit()
        return coordinates

# Creamos un objeto tablero con el tamaño de 10x10
board = Board("Test Board", [10, 10])
# Creamos un objeto barco con el nombre "Acorazado" y longitud de 5
acorazado = Ship("Acorazado", 5)
# Creamos un objeto barco con el nombre "Portaaviones" y longitud de 4
portaaviones = Ship("Portaaviones", 4)
# Creamos un objeto barco con el nombre "Crucerp" y longitud de 3
crucero = Ship("Crucero", 3)
# Creamos un objeto barco con el nombre "Submarino" y longitud de 2
submarino = Ship("Submarino", 2)
# Creamos un objeto barco con el nombre "Destructor" y longitud de 2
destructor = Ship("Destructor", 2)

# Lugar de los barcos en el tablero
board.place_ship(acorazado)
board.place_ship(portaaviones)
board.place_ship(crucero)
board.place_ship(submarino)
board.place_ship(destructor)
# Printeamos el tablero
board.print_board()
