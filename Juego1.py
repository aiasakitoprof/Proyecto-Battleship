from Bd_Sh_player import *
from Rd_Sh_ai import *
class Juego:
    def __init__(self):
        self.tablero = Tablero()
        self.radar = Radar()
        self.barcos = Barcos(self.tablero)
        self.barcos_ia = Barcos_ia(self.radar)
        self.disparos_realizados_jg = []
        self.disparos_realizados_ai = []
        self.aciertos_computer=[]
        self.fallos_computer=[]
        self.disparos_computer=[]



    def realizar_disparo(self):
        numeroF=True
        while numeroF == True:
            try:
                fila = int(input("Introduce la fila para realizar el disparo: "))
                if fila<0 or fila>9:
                    print("Valor incorrecto, debe introducir un número entre 0 y 9")
                    numeroF=True
                else:
                    numeroF=False
            except ValueError:
                print("Valor incorrecto, debe introducir un número entre 0 y 9")
                numeroF=True
        numeroC=True
        while numeroC==True:
            try:
                columna = int(input("Introduce la columna para realizar el disparo: "))
                if columna<0 or columna>9:
                    print("Valor incorrecto, debe introducir un número entre 0 y 9")
                    numeroC=True
                else:
                    numeroC=False
            except ValueError:
                print("Valor incorrecto, debe introducir un número entre 0 y 9")
                numeroC=True
        disparo = (fila, columna)

        while disparo in self.disparos_realizados_jg:
            fila = int(input("Introduce una fila no repetida para realizar el disparo: "))
            columna = int(input("Introduce una columna no repetida para realizar el disparo: "))
            disparo = (fila, columna)

        if len(self.radar.coordenadas_barcos_ia) == 0:
            print("¡Has ganado!")
            return True

        if disparo in self.radar.coordenadas_barcos_ia:
            self.disparos_realizados_jg.append(disparo)
            self.radar.radar[fila][columna] = "X"
            self.radar.coordenadas_barcos_ia.remove(disparo)
            print("¡Hundiste un barco!")
            return False
        else:
            self.radar.radar[fila][columna] = "O"
            print("Disparo fallido")
            return False

    def posicion_azar(self):
        fila = random.randint(0,9)
        columna = random.randint(0,9)
        return (fila,columna)


    def buscar_alrededor(self):
        filaMenos=int(self.aciertos_computer[-1][0])-1
        filaMas=int(self.aciertos_computer[-1][0])+1
        columnaMenos=int(self.aciertos_computer[-1][1])-1
        columnaMas=int(self.aciertos_computer[-1][1])+1


        arriba_abajo=random.choice([fila,columna])
        if arriba_abajo==fila:
            fila=random.choice([filaMenos,filaMas])
            columna=int(self.aciertos_computer[-1][1])
            if filaMenos<0:
                fila=filaMas
            elif filaMas>9:
                fila=filaMenos
        elif arriba_abajo==columna:
            fila=int(self.aciertos_computer[-1][0])
            columna=random.choice([columnaMenos,columnaMas])
            if columnaMenos<0:
                columna=columnaMas
            elif columnaMas>9:
                columna=columnaMenos
            disparo_cerca=(fila,columna)
            for elem in self.aciertos_computer:
                if filaMenos or filaMas == elem[0]:
                    fila=elem[0]
                    columna = int(self.aciertos_computer[-1][1])
                elif columnaMenos or columnaMas == elem[1]:
                    columna=elem[1]
                    fila = int(self.aciertos_computer[-1][1])
            disparo_aprox=(fila,columna)

        return (disparo_cerca,disparo_aprox)


    def disparo_ia(self,todos_barcos,coordenadas_barcos):
        # Inicializamos las variables del ambito del la función
        # Disparo que se realizará en el tablero
        disparo = 0
        # Tiros son lo mismo que disparo, pero en otro formato
        tiros=0
        # Fila donde se realizará el tiro
        fila=0
        # Columna donde se realizará el tiro
        columna=0
        # Contabiliza el numero de barcos hundidos, cuando alcance el número
        # de barcos totales habrá ganado la partida
        barco_hundido=0
        # Modo para inicializar el juego, hay tres modos, buscar, hundir y aprox
        # El modo hundir se activa cuando hay un acierto, y el modo aprox cuando hay 
        # mas de un acierto
        modo="buscar"
        # Contador de aciertos
        acierto=0
        # Booleano para indicar cuando inicia y acaba el disparo
        disparar=True
        

        while disparar==True:
            if modo=="buscar":
                # En este modo hace una tirada al azar
                fila, columna = self.posicion_azar()
                tiros = str(fila) + str(columna)
                disparo = (fila, columna)

                if tiros in self.disparos_computer:
                    continue
                # si los tiros no estan en el array de disparos, se guardaran
                # en sus listas correspondientes
                self.disparos_computer.append(tiros)
                self.disparos_realizados_ai.append(disparo)
                # Si el tiro coincide con las coordenadas de los barcos, será
                # un acierto y se borrará de la lista de coordenadas
                if tiros in coordenadas_barcos:
                    self.tablero.tablero[fila][columna] = "X"
                    self.aciertos_computer.append(tiros)
                    coordenadas_barcos.remove(tiros)
                    #aumentamos los aciertos
                    acierto+=1
                    #si los aciertos superan a 1 pasaremos al modo aprox
                    if acierto>1:
                        modo = "aprox"
                    else:
                    # en caso contrario seguiremos intentando hundir otra posición
                        modo = "hundir"
                    disparar=False
                    # En el siguiente bucle comparamos los tiros con los valores
                    # del diccionario
                    for key, value in todos_barcos.items():
                            for element in value:
                                if element == tiros:
                                    # en caso de que haya un acierto se eliminará 
                                    # del diccionario
                                    todos_barcos[key].remove(tiros)
                                # si el tamaño de la lista que corresponde al barco
                                # está vacia, el ordenador habrá undido un barco
                                if len(todos_barcos[key]) == 0:
                                    print(key, "undido")
                                    barco_hundido += 1
                                    modo = "buscar"
                else:
                    # En caso de fallo, mostramos el simbolo correspondiente en
                    # el tablero y lo añadimos a la lista de fallos
                    self.tablero.tablero[fila][columna] = "O"
                    self.fallos_computer.append(tiros)
                    print("Agua")
                    modo = "buscar"
                    disparar=False
            # En este modo intentamos hundir el barco
            elif modo == "hundir":
                # llamamos a la función buscar_alrededor que tiene la lógica de tiro
                disparo_cerca,disparo_aprox = self.buscar_alrededor()
                fila, columna = disparo_cerca
                tiros = str(fila) + str(columna)
                disparo = (fila, columna)    
                # Si el tiro está en la lista volverá a tirar
                if tiros in self.disparos_computer:
                    continue
                # Se guardan los datos de disparo en las listas correspondientes
                self.disparos_computer.append(tiros)
                self.disparos_realizados_ai.append(disparo)
                # Si el tiro ha sido un acierto se mostrará el simbolo correspondiente.
                # Se guarda en la lista de aciertos y se borra de las coordenadas del barco
                if tiros in coordenadas_barcos:
                    self.tablero.tablero[fila][columna] = "X"
                    self.aciertos_computer.append(tiros)
                    coordenadas_barcos.remove(tiros)
                    modo="aprox"
                    disparar=False

                    for key, value in todos_barcos.items():
                        for element in value:
                            if element == tiros:
                                todos_barcos[key].remove(tiros)
                            if len(todos_barcos[key]) == 0:
                                print(key, "undido")
                                barco_hundido += 1
                                modo = "buscar"
                else:
                    self.tablero.tablero[fila][columna] = "O"
                    self.fallos_computer.append(tiros)
                    print("Agua")
                    modo = "buscar"
                    disparar=False
            
            elif modo == "aprox":
                disparo_cerca,disparo_aprox = self.buscar_alrededor()
                fila, columna = disparo_aprox
                tiros = str(fila) + str(columna)
                disparo = (fila, columna)    
                
                if tiros in self.disparos_computer:
                    continue

                self.disparos_computer.append(tiros)
                self.disparos_realizados_ai.append(disparo)

                if tiros in coordenadas_barcos:
                    self.tablero.tablero[fila][columna] = "X"
                    self.aciertos_computer.append(tiros)
                    coordenadas_barcos.remove(tiros)
                    modo="hundir"
                    disparar=False

                    for key, value in todos_barcos.items():
                        for element in value:
                            if element == tiros:
                                todos_barcos[key].remove(tiros)
                            if len(todos_barcos[key]) == 0:
                                print(key, "undido")
                                barco_hundido += 1
                                modo = "buscar"
                else:
                    self.tablero.tablero[fila][columna] = "O"
                    self.fallos_computer.append(tiros)
                    print("Agua")
                    modo = "buscar"
                    disparar=False
    
            if barco_hundido == len(todos_barcos):
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
        self.barcos.colocar_barcos()
        self.barcos_ia.colocar_barcos_ia()
        while True:
            clear_terminal()
            print(self.radar.coordenadas_barcos_ia)
            print("disparos", self.disparos_computer)
            print("aciertos",self.aciertos_computer)
            print("fallos", self.fallos_computer)
            print("Barcos usuario", todos_barcos)
            print("Lista valores barcos", todos_barcos.values())
            self.print_ambos_tableros()
            if self.realizar_disparo():
                break
            if self.disparo_ia(todos_barcos,coordenadas_barcos):
                break

partida = Juego()
partida.print_ambos_tableros()
partida.jugar()

