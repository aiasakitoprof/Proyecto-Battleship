from Jugador import *
from Jugador_rapido import *
from AI import *
from Menu_y_extras import *
from colorama import Fore,Style

class Juego:
    def __init__(self):
        self.tablero = Tablero()
        self.radar = Radar()
        
        self.barcos = Barcos(self.tablero)
        self.barcos_rapidos = Barcos_rapidos(self.tablero)
        self.barcos_ia = Barcos_ia(self.radar)
        
        self.disparos_realizados_jg = []
        self.disparos_realizados_ai = []
        self.vida = 16  # Vida del jugador.

    def realizar_disparo(self):

    # ---/ Filtros de disparo /---
        coord = input("Selecciona unas coordenadas de disparo (formato '00'):\n >  ")
        while True:  # Control de errores.
            if len(coord) == 2:
                if coord[0] in ["0","1","2","3","4","5","6","7","8","9"]:
                    if coord[1] in ["0","1","2","3","4","5","6","7","8","9"]:
                        break
            clear_terminal()
            self.print_ambos_tableros()
            coord = input("Selecciona unas coordenadas válidas de disparo (formato '00'):\n >  ")
        
        fila = int(coord[0])  # Nos quedamos co el primer elemento de coords para la fila.
        columna = int(coord[1])  # Segundo elemento de coords para columnas.
        disparo = (fila, columna)  # Juntamos las fila y columna para dejarlo en el formato deseado. (Pasamos de 00 a 0,0)

        while disparo in self.disparos_realizados_jg:  # Si el disparo ya ha sido realizado pedimos otro.
            clear_terminal()
            self.print_ambos_tableros()
            coord = input("Selecciona coordenadas de disparo no repetidas:\n >  ")
            while True:  # Control de errores.
                if len(coord) == 2:
                    if coord[0] in ["0","1","2","3","4","5","6","7","8","9"]:
                        if coord[1] in ["0","1","2","3","4","5","6","7","8","9"]:
                            break
                
            fila = int(coord[0])
            columna = int(coord[1])
            disparo = (fila, columna)
        
        self.disparos_realizados_jg.append(disparo)  # Como ha pasado todos los filtros guardamos el disparo en la lista de realizados.

        # --- / Evaluación de tiro /---
        if disparo in self.radar.coordenadas_barcos_ia:  # Si el disparo coindice con las coordenadas de un barco de la ia.
            self.radar.radar[fila][columna] = Fore.RED +"X"+ Style.RESET_ALL  # Marcamos en el radar como 'tocado' / 'alcanzado' mediante la X.
            self.radar.coordenadas_barcos_ia.remove(disparo)  # Quitamos la coordenada alcanzada de la lista de la ia.
            if len(self.radar.coordenadas_barcos_ia) == 0:  # Si la lista donde están los barcos de la ia se queda vacia, hemos ganado.
                print("¡Has ganado!")
                return True  # <-- Finaliza el bucle de juego
        else:
            self.radar.radar[fila][columna] = Fore.BLUE +"O"+ Style.RESET_ALL  # Si fallamos el tiro apuntamos el fallo.
        return False


    def disparo_ia(self):

    # ---/ Selección aleatoria de disparo /---
        fila = random.randint(0,9)
        columna = random.randint(0,9)
        disparo = (fila, columna)
        
    # ---/ Filtros de disparo /---
        while disparo in self.disparos_realizados_ai:  # Si el disparo es repetido pedimos otro.
            fila = random.randint(0,9)
            columna = random.randint(0,9)
            disparo = (fila, columna)
        
    # --- / Evaluación de tiro /---
        if disparo not in self.disparos_realizados_ai:
            self.disparos_realizados_ai.append(disparo)  # Guardamos el disparo en la lista de realizados.
            
            if self.tablero.tablero[fila][columna] != "·":  # Evaluamos si el disparo le da al mar, si no es así, procedemos.
                self.tablero.tablero[fila][columna] = Fore.RED +"X"+ Style.RESET_ALL  # Apuntamos el acierto en el tablero.
                self.vida -= 1  # Restamos 1 a la vida del jugador.
            else: 
                self.tablero.tablero[fila][columna] = Fore.BLUE +"O"+ Style.RESET_ALL  # En caso de fallo lo apuntamos en el tablero.
            
            if self.vida == 0:  # Si la vida del jugador llega a cero, partida perdida.
                print("Has perdido")
                return True


    def print_ambos_tableros(self):
        print("\n")
        print("           Radar                        Barcos")
        print("    0 1 2 3 4 5 6 7 8 9          0 1 2 3 4 5 6 7 8 9")
        print("  ┌─────────────────────┐      ┌─────────────────────┐")
        for i in range(self.radar.height):
            print(i, end=" │ ")
            print(" ".join(self.radar.radar[i]), end=" │")
            print(" "*4, end="")
            print(i, end=" │ ")
            print(" ".join(self.tablero.tablero[i]), "│")
        print("  └─────────────────────┘      └─────────────────────┘")
        print("\n")


    def jugar(self):
        
        x = menu()  # Ejecutamos el menú en una variable para poder analizar el valor retornado.
        
        if x == "0":  # Juego rápido (barcos autocolocados)
            self.barcos_rapidos.colocar_barcos_rapidos()
            self.barcos_ia.colocar_barcos_ia()
        
        if x == "1":  # El jugador coloca sus barcos
            self.barcos.colocar_barcos()
            self.barcos_ia.colocar_barcos_ia()
        
        
        while True:  # Bucle de juego
            clear_terminal()
            self.print_ambos_tableros()
            if self.realizar_disparo():
                break
            if self.disparo_ia():
                break
partida = Juego()
partida.jugar()