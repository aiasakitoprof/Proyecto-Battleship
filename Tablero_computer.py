acorazado={} 
crucero={}
submarino={}
# Ancho y alto definido inicialmente, necesito definirlas aqui para poder emplear estas variables en otras partes 
#del código
width=10
height=10
class Board_computer:
    #Esta clase la llamo para iniciar la posición del los barcos del computador
    def __init__(self, width=10, height=10): # Llamada al objeto tablero.
        self.board = [["." for i in range(width)] for i in range(height)] #  Bucle para crear el tablero.
        self.barcos_colocados = {} # Guarda los barcos ya colocados.
        #barquitos=self.barcos_colocados
        #print(barquitos)

    def barco_colocado(self, barco):
        self.barcos_colocados[barco] = True
        
class Tablero_Computer:
#La siguiente clase la llamo para ir pintando el tablero del computador durante el juego
# Va cambiando según el usuario vaya acertando o fallando, va pintando las posiciones
    def __init__(self): # Llamada al objeto tablero.
        pinta="."
        self.board = [[pinta for i in range(width)] for j in range(height)]

    def view_board(self,acierto,perdido): # Printeo de tablero.
        pinta="."
        self.board = [[pinta for i in range(width)] for j in range(height)]
        #print(self.board)
        board=self.board
        #Bucle para recorrer el tablero y sustituir los aciertos y los fallos por su simbolo correspondiente
        for i in range(len(board)):
            for j in range(len(board[i])):
                posiciones=(str(i)+str(j))
                if posiciones in acierto:
                    #print("la posicion",posiciones)
                    board[i][j]="o"
                if posiciones in perdido:
                    board[i][j]="x"
        # A partir de aqui me inicia el pintado del tablero
        print("  ", end="") # Hueco separador de coordenadas.

        for i in range(len(self.board[0])): # Coordenadas de columnas (Encima del tablero).
            print(i, end=" ")
        print()

        for i, row in enumerate(self.board): # Coordenadas de filas (A la derecha del tablero).
            print(i, end=" ")
            print(" ".join(row))
