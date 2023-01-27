import random
from colorama import Fore,Style    # Fore.BLACK +     + Style.RESET_ALL

class AI_strat:
    def __init__(self, tablero):
    # ---| Tablero |---
        self.tablero = tablero
        
    # ---| Switches |---
        self.modo_aleatorio = True
        self.modo_cruz = False
        self.ady_en = False
        
    # ---| Orientación |---
        self.orientacion = None
        self.direccion = None
        self.counter = 1
        
    # ---| Vida |---
        self.vida = 16
        
    # ---| Listas |---
        self.disparos_realizados = []
        self.resultados = []
        self.adyacentes = []

    # ---| Conservadores |---
        self.ultimo_disparo = None
        self.keeper = None

    def c_vida(self):
        if self.vida == 0:
            return True

    def r_disparo(self):
        fila = random.randint(0,9)
        columna = random.randint(0,9)
        disparo = (fila,columna)

        while disparo in self.disparos_realizados:
            fila = random.randint(0,9)
            columna = random.randint(0,9)
            disparo = (fila,columna)
        
        self.disparos_realizados.append(disparo)
        self.ultimo_disparo = self.disparos_realizados[-1]
        
        if self.tablero.tablero[fila][columna] != "·":
            self.tablero.tablero[fila][columna] = Fore.RED +"X"+ Style.RESET_ALL
            self.resultados.append("X")
            self.vida -= 1
            self.modo_aleatorio = False
            self.modo_cruz = True
        
        
        else:
            self.tablero.tablero[fila][columna] = Fore.BLUE +"O"+ Style.RESET_ALL
            self.resultados.append("O")
        
        if self.vida == 0:
            return False

    def adyacencia(self):
        self.keeper = self.disparos_realizados[-1]
        
        if self.keeper[0] > 0:
            if (self.keeper[0]-1,self.keeper[1]) not in self.disparos_realizados:
                self.adyacentes.append((self.keeper[0]-1,self.keeper[1]))
        
        if self.keeper[0] < 9:
            if (self.keeper[0]+1,self.keeper[1]) not in self.disparos_realizados:
                self.adyacentes.append((self.keeper[0]+1,self.keeper[1]))
        
        if self.keeper[1] > 0:
            if (self.keeper[0],self.keeper[1]-1) not in self.disparos_realizados:
                self.adyacentes.append((self.keeper[0],self.keeper[1]-1))
        
        if self.keeper[1] < 9:
            if (self.keeper[0],self.keeper[1]+1) not in self.disparos_realizados:
                self.adyacentes.append((self.keeper[0],self.keeper[1]+1))



    def disparo_ia(self):
        
        if self.orientacion == None:
            

            if self.ady_en:

                self.ultimo_disparo = self.disparos_realizados[-1]

                if self.keeper[0] == self.ultimo_disparo[0]:
                    self.orientacion = "h"
                    self.direccion = "d"
                    self.adyacentes = []
                
                elif self.keeper[1] == self.ultimo_disparo[1]:
                    self.orientacion = "v"
                    self.direccion = "ar"
                    self.adyacentes = []
            
            
            elif self.modo_cruz:
                
                if len(self.adyacentes) == 0:
                    self.adyacencia()

                disparo = random.choice(self.adyacentes)

                while disparo in self.disparos_realizados:
                    
                    if len(self.adyacentes) == 0:
                        self.modo_aleatorio = True
                        self.modo_cruz = False
                        self.adyacentes = []
                        break
                    
                    disparo = random.choice(self.adyacentes)
                self.disparos_realizados.append(disparo)

                fila = disparo[0]
                columna = disparo[1]

                if self.tablero.tablero[fila][columna] == "·":
                    self.tablero.tablero[fila][columna] = Fore.BLUE +"O"+ Style.RESET_ALL
                    self.resultados.append("O")
                else:
                    self.tablero.tablero[fila][columna] = Fore.RED +"X"+ Style.RESET_ALL
                    self.resultados.append("X")
                    self.vida -=1
                    self.modo_cruz = False
                    self.ady_en = True
                    if self.c_vida():
                        return True

            elif self.modo_aleatorio:
                self.r_disparo()
                if self.c_vida():
                    return True



        if self.orientacion == "h":
            

            disparo = (self.keeper[0],self.ultimo_disparo[1]+self.counter)
            

            if self.direccion == "d":
                while disparo in self.disparos_realizados:
                    self.counter += 1
                    disparo = (self.keeper[0],self.ultimo_disparo[1]+self.counter)
                self.disparos_realizados.append(disparo)

            elif self.direccion == "i":
                while disparo in self.disparos_realizados:
                    self.counter -= 1
                    disparo = (self.keeper[0],self.ultimo_disparo[1]+self.counter)
                self.disparos_realizados.append(disparo)


            if 0 <= disparo[0] <= 9 and  0 <= disparo[1] <= 9:
                self.disparos_realizados.append(disparo)

            else:
                self.orientacion = None
                self.direccion = None
                self.counter = 1
                self.modo_aleatorio = True
                self.modo_cruz = False
                self.ady_en = False
                self.r_disparo()
            

            fila = disparo[0]
            columna = disparo[1]
            

            if self.direccion == "d": 
                if self.tablero.tablero[fila][columna] == "·": 
                    self.tablero.tablero[fila][columna] = Fore.BLUE +"O"+ Style.RESET_ALL
                    self.resultados.append("O")
                    self.counter = -1
                    self.direccion = "i"
                
                else:
                    self.tablero.tablero[fila][columna] = Fore.RED +"X"+ Style.RESET_ALL
                    self.resultados.append("X")
                    self.vida -=1
                    if self.c_vida():
                        return True
            
            elif self.direccion == "i":
                if self.tablero.tablero[fila][columna] == "·": 
                    self.tablero.tablero[fila][columna] = Fore.BLUE +"O"+ Style.RESET_ALL
                    self.resultados.append("O")
                    self.orientacion = None
                    self.direccion = None
                    self.counter = 1
                    self.modo_aleatorio = True
                    self.modo_cruz = False
                    self.ady_en = False
                
                else:
                    self.tablero.tablero[fila][columna] = Fore.RED +"X"+ Style.RESET_ALL
                    self.resultados.append("X")
                    self.vida -=1
                    if self.c_vida():
                        return True



        if self.orientacion == "v":
            

            disparo = (self.ultimo_disparo[0]+self.counter,self.keeper[1])
            

            if self.direccion == "ar":
                while disparo in self.disparos_realizados:
                    self.counter += 1
                    disparo = (self.ultimo_disparo[0]+self.counter,self.keeper[1])

            elif self.direccion == "ab":
                while disparo in self.disparos_realizados:
                    self.counter -= 1
                    disparo = (self.ultimo_disparo[0]+self.counter,self.keeper[1])


            if 0 <= disparo[0] <= 9 and  0 <= disparo[1] <= 9:
                self.disparos_realizados.append(disparo)

            else:
                self.orientacion = None
                self.direccion = None
                self.counter = 1
                self.modo_aleatorio = True
                self.modo_cruz = False
                self.ady_en = False
                self.r_disparo()


            fila = disparo[0]
            columna = disparo[1]
            

            if self.direccion == "ar": 
                if self.tablero.tablero[fila][columna] == "·": 
                    self.tablero.tablero[fila][columna] = Fore.BLUE +"O"+ Style.RESET_ALL
                    self.resultados.append("O")
                    self.counter = -1
                    self.direccion = "ab"
                
                else:
                    self.tablero.tablero[fila][columna] = Fore.RED +"X"+ Style.RESET_ALL
                    self.resultados.append("X")
                    self.vida -=1
                    if self.c_vida():
                        return True
            
            elif self.direccion == "ab":
                if self.tablero.tablero[fila][columna] == "·": 
                    self.tablero.tablero[fila][columna] = Fore.BLUE +"O"+ Style.RESET_ALL
                    self.resultados.append("O")
                    self.orientacion = None
                    self.direccion = None
                    self.counter = 1
                    self.modo_aleatorio = True
                    self.modo_cruz = False
                    self.ady_en = False
                
                else:
                    self.tablero.tablero[fila][columna] = Fore.RED +"X"+ Style.RESET_ALL
                    self.resultados.append("X")
                    self.vida -=1
                    if self.c_vida():
                        return True