from Jugador import *
from Jugador_rapido import *
from AI import *
from Menu_y_extras import *
from colorama import Fore,Style    # Fore.BLACK +     + Style.RESET_ALL

class Juego:
    def __init__(self):
        self.tablero = Tablero()
        self.radar = Radar()
        
        self.barcos = Barcos(self.tablero)
        self.barcos_rapidos = Barcos_rapidos(self.tablero)
        self.barcos_ia = Barcos_ia(self.radar)
        
        self.disparos_realizados_jg = []
        self.disparos_realizados_ai = []

    def realizar_disparo(self):
        fila = int(input("Introduce la fila para realizar el disparo: "))
        columna = int(input("Introduce la columna para realizar el disparo: "))
        disparo = (fila, columna)
        
        while disparo in self.disparos_realizados_jg:
            fila = int(input("Introduce una fila no repetida para realizar el disparo: "))
            columna = int(input("Introduce una columna no repetida para realizar el disparo: "))
            disparo = (fila, columna)
        
        if disparo in self.radar.coordenadas_barcos_ia:
            self.disparos_realizados_jg.append(disparo)
            self.radar.radar[fila][columna] = Fore.RED +"X"+ Style.RESET_ALL
            self.radar.coordenadas_barcos_ia.remove(disparo)
            print("¡Hundiste un barco!")
            if len(self.radar.coordenadas_barcos_ia) == 0:
                print("¡Has ganado!")
                return True
        else:
            self.radar.radar[fila][columna] = Fore.BLUE +"O"+ Style.RESET_ALL
            print("Disparo fallido")
        return False


    def disparo_ia(self):
        
        fila = random.randint(0,9)
        columna = random.randint(0,9)
        disparo = (fila, columna)
        vida = 16
        
        if disparo not in self.disparos_realizados_ai:
            self.disparos_realizados_ai.append(disparo)
            
            if self.tablero.tablero[fila][columna] != "·":
                self.tablero.tablero[fila][columna] = Fore.RED +"X"+ Style.RESET_ALL
                print("Tocado")
                vida -= 1
            else: 
                self.tablero.tablero[fila][columna] = Fore.BLUE +"O"+ Style.RESET_ALL
                print("Agua")
            
            if vida == 0:
                print("El ordenador ganó")
                return True


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
            print(self.radar.coordenadas_barcos_ia)
            self.print_ambos_tableros()
            if self.realizar_disparo():
                break
            if self.disparo_ia():
                break

partida = Juego()
partida.jugar()
# print(partida.barcos_ia)