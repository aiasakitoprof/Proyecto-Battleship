import random
from tabulate import tabulate

# Creamos una clase para los barcos
class Ship:
    def __init__(self, name, length):
        self.name = name # Nombre del barco
        self.length = length # Longitud del barco

# Creamos una clase para el tablero
class Board:
    def __init__ (self, name, size):
        self.name = name # Nombre del tablero
        self.rows = size[0] # Filas del tablero
        self.columns = size[1] # Columnas del tablero
        self.board = []
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append("")
            self.board.append(row)

    def print_board (self):
        # Creamos las cabeceras de las columnas
        header = []
        for i in range(self.columns):
            header.append(i+0)
        # Creamos las cabeceras de las filas
        rows = []
        for i in range(self.rows):
            rows.append(i+0)

        table = self.board
        print(tabulate(table, header, showindex=rows, numalign="center", stralign="center", tablefmt="fancy_grid"))
    def place_ship (self, ship):
        orientation = random.choice(["horizontal", "vertical"])
        coordinates = []
        if orientation == "horizontal":
            #Colocamos el barco horizontalmente
            #Nos aseguramos de que el punto de inicio no resulte en el barco siendo colocado fuera del mapa
            while True:
                start = [random.randint(0,self.rows -1), random.randint(0, self.columns-1)]
                while (start[1] + ship.length > self.columns):
                    start[1] -=1
                #Nos aseguramos de que el barco no sea colocado encima de otro barco
                unique = True
                for i in range(ship.length):
                    if self.board[start[0]][start[1]+i] != "":
                        unique = False
                        break
                if unique == True:
                    break
            for i in range(ship.length):
                self.board[start[0]][start[1]+i] = ship.name[0]
                coordinates.append






# Creamos un objeto tablero con el tamaño de 10x10
board = Board("Test Board", [10, 10])
# Creamos un objeto barco con el nombre "Cruiser" y longitud de 3
cruiser = Ship("Cruiser", 3)

# Lugar del barco en el tablero
board.place_ship(cruiser)
# Printeamos el tablero
board.print_board()
