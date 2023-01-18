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
