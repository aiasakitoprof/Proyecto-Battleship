import random
import colorama
from tabulate import tabulate

colorama.init()

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
        print(colorama.Fore.CYAN, end="")
        table = self.board
        print(tabulate(table, header, showindex=rows, numalign="center", stralign="center", tablefmt="fancy_grid"))
        print(colorama.Style.RESET_ALL)    

# Creamos un objeto tablero con el tamaño de 10x10
board = Board("Test Board", [10, 10])

# Printeamos el tablero
board.print_board()