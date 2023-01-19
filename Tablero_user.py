
total_coordenadas_Usuario=[]
acorazado_user={}
crucero_user={}
submarino_user={}
width=10
height=10
class Tablero_User:
    #Clase necesaria para pintar el tablero del usuario durante el JUEGO
    def __init__(self): # Llamada al objeto tablero.
        pinta="."
        self.board = [[pinta for i in range(width)] for j in range(height)]
    #La siguiente funcion me recoge los aciertos del computador y los fallos
    #y me pinta el tablero según estos datos
    def view_board_juego(self,acierto_computer, perdido_computer): # Printeo de tablero.
        pinta="."
        self.board = [[pinta for i in range(width)] for j in range(height)]
        #print(self.board)
        board=self.board
        #Bucle para recorrer el tablero y sustituir los aciertos y los fallos por su simbolo correspondiente
        for i in range(len(board)):
            for j in range(len(board[i])):
                posiciones=(str(i)+str(j))
                if posiciones in acierto_computer:
                    #print("la posicion",posiciones)
                    board[i][j]="o"
                elif posiciones in perdido_computer:
                    board[i][j]="x"
                elif len(total_coordenadas_Usuario)>0:
                    #Comparamos las coordenadas de cada navio para saber donde
                    #pintar las posiciones que aun no se han acertado
                    if posiciones in acorazado_user["coordenadas"]:
                        board[i][j]="1"
                    elif posiciones in crucero_user["coordenadas"]:
                        board[i][j]="2"
                    elif posiciones in submarino_user["coordenadas"]:
                        board[i][j]="3"

        print("  ", end="") # Hueco separador de coordenadas.

        for i in range(len(self.board[0])): # Coordenadas de columnas (Encima del tablero).
            print(i, end=" ")
        print()

        for i, row in enumerate(self.board): # Coordenadas de filas (A la derecha del tablero).
            print(i, end=" ")
            print(" ".join(row))       
class Board_player:
    #Esta clase pinta el tablero inicial vacio y permite guardar las posiciones
    def __init__(self, width=10, height=10): # Llamada al objeto tablero.
        self.board = [["." for i in range(width)] for i in range(height)] #  Bucle para crear el tablero.
        self.barcos_colocados = {} # Guarda los barcos ya colocados.

    def view_board(self): # Printeo de tablero.
    
            print("  ", end="") # Hueco separador de coordenadas.

            for i in range(len(self.board[0])): # Coordenadas de columnas (Encima del tablero).
                print(i, end=" ")
            print()

            for i, row in enumerate(self.board): # Coordenadas de filas (A la derecha del tablero).
                print(i, end=" ")
                print(" ".join(row))

    def barco_colocado(self, barco):
            self.barcos_colocados[barco] = True
