from Jugador import Tablero, Barcos, clear_terminal
from Jugador_rapido import Barcos_rapidos

from AI import Radar, Barcos_ia, random

from Menu_y_extras import menu

from colorama import Fore,Style    # Fore.BLACK +     + Style.RESET_ALL

from test import ia

class Juego:
    def __init__(self):
    # ---| Tableros |---
        self.tablero = Tablero()
        self.radar = Radar()

    # ---| Colocación de barcos |---
        self.barcos = Barcos(self.tablero)
        self.barcos_rapidos = Barcos_rapidos(self.tablero)
        self.barcos_ia = Barcos_ia(self.radar)
        
    # ---| Apartado del jugador|---
        self.disparos_realizados_jg = []

    # ---| Apartado de la ia |---
        self.ia = ia(self.tablero)
        # self.disparos_realizados_ai = []
        # self.vida = 16



    def realizar_disparo(self):

        coord = input("Selecciona unas coordenadas de disparo (formato '00'):\n >  ")
        while True:
            if len(coord) == 2:
                if coord[0] in ["0","1","2","3","4","5","6","7","8","9"]:
                    if coord[1] in ["0","1","2","3","4","5","6","7","8","9"]:
                        break
            clear_terminal()
            self.print_ambos_tableros()
            coord = input("Selecciona unas coordenadas válidas de disparo (formato '00'):\n >  ")
        fila = int(coord[0])
        columna = int(coord[1])
        disparo = (fila, columna)

        while disparo in self.disparos_realizados_jg:
            clear_terminal()
            self.print_ambos_tableros()
            coord = input("Selecciona coordenadas de disparo no repetidas:\n >  ")
            while len(coord) < 2 or len(coord) > 2 or int(coord[0]) < 0 or int(coord[0]) > 9 or int(coord[1]) < 0 or int(coord[1]) > 9: # Control de errores.
                clear_terminal()
                self.print_ambos_tableros()
                coord = input("Selecciona coordenadas válidas de disparo:\n >  ")
                
            fila = int(coord[0])
            columna = int(coord[1])
            disparo = (fila, columna)
        
        # self.disparos_realizados_jg.append(disparo)
        
        if disparo in self.radar.coordenadas_barcos_ia:
            self.radar.radar[fila][columna] = Fore.RED +"X"+ Style.RESET_ALL
            self.radar.coordenadas_barcos_ia.remove(disparo)
            if len(self.radar.coordenadas_barcos_ia) == 0:
                print("¡Has ganado!")
                return True
        else:
            self.radar.radar[fila][columna] = Fore.BLUE +"O"+ Style.RESET_ALL
        return False

    def print_ambos_tableros(self):
        print("\n")
        print("           Radar                        Barcos")
        print("    0 1 2 3 4 5 6 7 8 9          0 1 2 3 4 5 6 7 8 9")
        print("  ┌─────────────────────┐      ┌─────────────────────┐")

        # Imprimir el radar y tablero en una forma de matriz.
        for i in range(self.radar.height):
            print(i, end=" │ ")
            print(" ".join(self.radar.radar[i]), end=" │")
            print(" "*4, end="")
            print(i, end=" │ ")
            print(" ".join(self.tablero.tablero[i]), "│")
        print("  └─────────────────────┘      └─────────────────────┘")
        print("\n")


    def jugar(self):
        
        x = menu()
        
        if x == "0":
            self.barcos_rapidos.colocar_barcos_rapidos()
            self.barcos_ia.colocar_barcos_ia()
        
        if x == "1":
            self.barcos.colocar_barcos()
            self.barcos_ia.colocar_barcos_ia()
        
        
        while True:
            clear_terminal()
            print(self.ia.orientacion)
            print(self.ia.direccion)
            print(self.ia.keeper)
            self.print_ambos_tableros()
            
            
            if self.realizar_disparo():
                break
            if self.ia.disparo_ia():
                break

partida = Juego()
partida.jugar()