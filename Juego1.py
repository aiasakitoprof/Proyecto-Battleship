from Bd_Sh_player import *
from Rd_Sh_ai import *
from colorama import init, Fore, Back, Style
init()
class Juego:
    def __init__(self):
        # Guardamos todas las tiradas posibles del juego para emplearlas en las posibles tiradas
        # del ordenador, se van restando así como se vayan utilizando
        self.tiradasPosibles= [(fila,columna) for fila in range(10) for columna in range(10)]
        self.tablero = Tablero()
        self.radar = Radar()
        self.barcos = Barcos(self.tablero)
        self.barcos_ia = Barcos_ia(self.radar)
        self.disparos_realizados_jg = []
        self.disparos_realizados_ai = []
        self.aciertos_computer=[]
        #self.aciertos_ia=[]
        #self.fallos_computer=[]
        self.disparos_computer=[]
        self.barcos_hundidos=[]
        self.barcos_hundidos_ia=[]
        # Variable que me permite contar los tiros acertados y segun esta información
        # volver a tirar en una zona cercana
        self.contadorTiros=0
        # Variable que guarda el modo de tiro del ordenador, el modo inicial "buscar"
        # es random y el modo "hundir" me permite acceder a la función "buscar_alrededor"
        # que tiene la lógica aplicada para el siguiente tiro
        self.modo="buscar"



    def realizar_disparo(self, todos_barcos_ia):
        seguir=True
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
                print("Valor incorrecto, debe introducir un número entre 0 y 9, es una letra")
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
                print("Valor incorrecto, debe introducir un número entre 0 y 9, es una letra")
                numeroC=True
        disparo = (fila, columna)
        #tiros=str(fila)+str(columna)

        if disparo in self.radar.coordenadas_barcos_ia and seguir==True:
            self.disparos_realizados_jg.append(disparo)
            self.radar.radar[fila][columna] = Fore.GREEN+"X"
            self.radar.coordenadas_barcos_ia.remove(disparo)
            for key, value in todos_barcos_ia.items():
                        for element in value:
                            if element == disparo:
                                todos_barcos_ia[key].remove(disparo)
                            if len(todos_barcos_ia[key]) == 0:
                                print("Has undido un ",key)
                                self.barcos_hundidos_ia.append(key)
        else:
            self.radar.radar[fila][columna] = Fore.RED+"O"
            print("Disparo fallido")
        seguir=False
        return seguir


    def posicion_azar(self):
        #En el modo "buscar" de la tirada del ordenador se realizan las siguientes
        # tiradas random
        fila = random.randint(0,9)
        columna = random.randint(0,9)
        return (fila,columna)
        

    def buscar_alrededor(self):
        # Estrategias empleadas para favorecer que el ordenador sea más intuitivo
        # seleccionamos la fila y la columna de la ultima tirada acertada por el ordenador
        fila=int(self.aciertos_computer[-1][0])
        columna=int(self.aciertos_computer[-1][1])
        # Inicializamos la variable eleccion
        eleccion=(fila,columna)
        # Dirección de la tirada consecutiva (0 = ninguna, 1 = horizontal, 2 = vertical
        direccion_tirada = 0
        # En caso de que "elección" no esté dentro de los disparos realizados por la ia
        while eleccion not in self.disparos_realizados_ai:
            # Si el tamaño de los aciertos es mayor a 1
            if len(self.aciertos_computer) > 1:
                # Comprueba si hay una fila o columna de tiradas acertadas consecutivas
                if self.aciertos_computer[-1][0] == self.aciertos_computer[-2][0]:
                    direccion_tirada = 1
                    #fila = int(self.aciertos_computer[-1][0])
                    # Verificamos que el número de columna no se salga del tablero
                    if columna+1 >9:
                        columna=columna-1
                    elif columna-1 <0:
                        columna=columna+1
                    else:
                        columna = random.choice([columna-1,columna+1])
                    eleccion=(fila,columna)

                elif self.aciertos_computer[-1][1] == self.aciertos_computer[-2][1]:
                    direccion_tirada = 2
                    columna = int(self.aciertos_computer[-1][1])
                    if fila+1 >9:
                        fila=fila-1
                    elif fila-1 <0:
                        fila=fila+1
                    else:
                        fila = random.choice([fila-1,fila+1])
                    eleccion=(fila,columna)
            else:
                # En caso de que no haya un número de aciertos mayor a 1, no sabremos
                # la dirección
                direccion_tirada = 0
                # En caso de que el tiro elegido esté dentro de los disparos ya realizados
                # la dirección será desconocida
            if eleccion in self.disparos_realizados_ai:
                direccion_tirada = 0
        # Si la dirección es desconocida seguimos la siguiente estrategia
        if direccion_tirada==0:
            # Creamos una lista de aproximaciones
            aproximaciones=[(fila-1,columna), (fila+1,columna), (fila,columna-1), (fila,columna+1)]
            # Creamos una lista de aproximaciones válidas, que serán las que no se salgan del tablero
            valid_aproximaciones = [aprox for aprox in aproximaciones if aprox[0] >= 0 and aprox[0] <= 9 and aprox[1] >= 0 and aprox[1] <= 9]
            random.shuffle(valid_aproximaciones)
            for aprox in valid_aproximaciones:
                if aprox not in self.disparos_realizados_ai:
                    eleccion=aprox
                    break
                else:
                    # En caso contrario se eligira una tirada de las posiciones
                    # restantes
                    random.shuffle(self.tiradasPosibles)
                    for posibles in self.tiradasPosibles:
                        eleccion=posibles
                        break               
                    
        return eleccion


    def disparo_ia(self,todos_barcos,coordenadas_user):
        # Inicializamos las variables del ambito del la función
        # Disparo que se realizará en el tablero
        disparo = 0
        # Tiros son lo mismo que disparo, pero en otro formato
        tiros=0
        # Fila donde se realizará el tiro
        fila=0
        # Columna donde se realizará el tiro
        columna=0
        # Booleano para indicar cuando inicia y acaba el disparo
        disparar=True

        while disparar==True:
            # print("modo activo", modo)
            # print("Contador Tiros", contadorTiros)
            if self.modo=="buscar":
                # En este modo hace una tirada al azar
                fila, columna = self.posicion_azar()
                #tiros = str(fila) + str(columna)
                disparo = (fila, columna)

                if disparo in self.disparos_realizados_ai:
                    continue
                # si los tiros no estan en el array de disparos, se guardaran
                # en sus listas correspondientes
                #self.disparos_computer.append(tiros)
                self.disparos_realizados_ai.append(disparo)
                # Si el tiro coincide con las coordenadas de los barcos, será
                # un acierto y se borrará de la lista de coordenadas
                if disparo in coordenadas_user:
                    self.tablero.tablero[fila][columna] = Fore.GREEN+"X"
                    self.aciertos_computer.append(disparo)
                    coordenadas_user.remove(disparo)
                    #Eliminamos los el tiro realizado de las tiradas posibles para 
                    # Validar en otra función que tiradas disponemos
                    self.tiradasPosibles.remove(disparo)
                    self.contadorTiros+=1
                    self.modo = "hundir"
                # if disparo in coordenadas_user:
                #     coordenadas_user.remove(disparo)
                    #disparar=False
                    # En el siguiente bucle comparamos los tiros con los valores
                    # del diccionario
                    for key, value in todos_barcos.items():
                            for element in value:
                                if element == disparo:
                                    # en caso de que haya un acierto se eliminará
                                    # del diccionario
                                    todos_barcos[key].remove(disparo)
                                # si el tamaño de la lista que corresponde al barco
                                # está vacia, el ordenador habrá undido un barco
                                if len(todos_barcos[key]) == 0:
                                    print(key, "undido")
                                    self.barcos_hundidos.append(key)
                                    self.modo = "buscar"
                else:
                    # En caso de fallo, mostramos el simbolo correspondiente en
                    # el tablero y lo añadimos a la lista de fallos
                    self.tablero.tablero[fila][columna] = Fore.RED+"O"
                    #self.fallos_computer.append(tiros)
                    self.tiradasPosibles.remove(disparo)
                    print("Agua")
                    if self.contadorTiros>0:
                        self.modo = "hundir"
                    else:
                        self.modo = "buscar"
                
                    #disparar=False
            # En este modo intentamos hundir el barco
            elif self.modo == "hundir":
                # llamamos a la función buscar_alrededor que tiene la lógica de tiro
                fila,columna = self.buscar_alrededor()
                #tiros = str(fila) + str(columna)
                disparo = (fila, columna)
                # Si el tiro está en la lista volverá a tirar
                if disparo in self.disparos_realizados_ai:
                    continue
                # Se guardan los datos de disparo en las listas correspondientes
                #self.disparos_computer.append(tiros)
                self.disparos_realizados_ai.append(disparo)
                # Si el tiro ha sido un acierto se mostrará el simbolo correspondiente.
                # Se guarda en la lista de aciertos y se borra de las coordenadas del barco
                if disparo in coordenadas_user:
                    # Si el disparo coincide con una coordenada del barco del usuario
                    # sustituimos, marcamos la casilla con X
                    self.tablero.tablero[fila][columna] = Fore.GREEN+"X"
                    # Guardamos el acierto en la lista y borramos el acierto de la lista
                    # de coordenadas del usuario
                    self.aciertos_computer.append(disparo)
                    coordenadas_user.remove(disparo)
                    # Eliminamos el tiro de la lista de tiradas posibles
                    self.tiradasPosibles.remove(disparo)
                    self.contadorTiros+=1
                    self.modo="hundir"
                    #disparar=False
                    # Verificamos si el tiro ha hundido un barco
                    for key, value in todos_barcos.items():
                        for element in value:
                            if element == disparo:
                                todos_barcos[key].remove(disparo)
                            if len(todos_barcos[key]) == 0:
                                print(key, "undido")
                                # En caso de que se haya undido un barco lo guardamos
                                # en la lista de barcos hundidos
                                self.barcos_hundidos.append(key)
                                self.modo = "buscar"
                else:
                    # Si hay un disparo fallido lo marcamos con O
                    self.tablero.tablero[fila][columna] = Fore.RED+"O"
                    print("Agua")
                    # Eliminamos la tirada de las tiradas posibles
                    self.tiradasPosibles.remove(disparo)
                    if self.contadorTiros>0:
                        self.modo = "hundir"
                    else:
                        self.modo = "buscar"
                    #disparar=False
            
            # if contadorTiros==4:
            #     contadorTiros=0
            # Variable que cierra el bucle
            disparar=False
            


            # if len(self.barcos_hundidos) == len(todos_barcos):
            #         print("El ordenador ganó")
            #         return True
    # Función que pinta las palabras "GAME OVER" en rojo al finalizar la partida
    def game_over(self):
        print(Fore.RED+Style.BRIGHT+"███▀▀▀██ ███▀▀▀███ ███▀█▄█▀███ ██▀▀▀")
        print("██    ██ ██     ██ ██   █   ██ ██   ")
        print("██   ▄▄▄ ██▄▄▄▄▄██ ██   ▀   ██ ██▀▀▀")
        print("██    ██ ██     ██ ██       ██ ██   ")
        print("███▄▄▄██ ██     ██ ██       ██ ██▄▄▄")
        print(" ")
        print("███▀▀▀███ ▀███  ██▀ ██▀▀▀ ██▀▀▀▀██▄ ")
        print("██     ██   ██  ██  ██    ██     ██ ")
        print("██     ██   ██  ██  ██▀▀▀ ██▄▄▄▄▄▀▀ ")
        print("██     ██   ██  █▀  ██    ██     ██ ")
        print("███▄▄▄███    ▀█▀    ██▄▄▄ ██     ██▄")
        print(" ")

    def turnos(self, todos_barcos, todos_barcos_ia):
    # Inicializamos la variable turno para indicar que el primer turno es del usuario
        turno = "usuario"
        juego_terminado=False
        # Mientras no se hayan hundido todos los barcos del usuario o del ordenador
        while juego_terminado==False:
            if turno == "usuario":
                # Ejecutamos la función turno_usuario
                self.realizar_disparo(todos_barcos_ia)
                self.print_ambos_tableros()
                if len(self.barcos_hundidos_ia) == len(todos_barcos_ia):
                    self.game_over()
                    print(Fore.RESET+"¡Has ganado!")
                    juego_terminado=True
                    return True
                # Cambiamos el turno a la IA
                turno = "IA"
                
            else:
                # Ejecutamos la función turno_ia
                self.disparo_ia(todos_barcos, coordenadas_user)
                self.print_ambos_tableros()
                if len(self.barcos_hundidos) == len(todos_barcos):
                    self.game_over()
                    print(Fore.RESET+"El ordenador ganó")
                    juego_terminado=True
                    return True
                # Cambiamos el turno al usuario
                turno = "usuario"

    def print_ambos_tableros(self):
        print("\n")
        print("           Radar                        Barcos")
        print(Fore.RESET+"    0 1 2 3 4 5 6 7 8 9          0 1 2 3 4 5 6 7 8 9")
        print(Fore.RESET+"  ┌─────────────────────┐      ┌─────────────────────┐")

        # Imprimir el radar y tablero en una forma de matriz.
        for i in range(self.radar.height):
            print(i, end=Fore.RESET+" │ ")
            print(" ".join(self.radar.radar[i]), end=Fore.RESET+" │")
            print(" "*4, end=Fore.RESET+"")
            print(i, end=Fore.RESET+" │ ")
            print(" ".join(self.tablero.tablero[i]),Fore.RESET+"│")
        print(Fore.RESET+"  └─────────────────────┘      └─────────────────────┘")
        print("\n")



    def jugar(self):
        self.barcos.colocar_barcos()
        self.barcos_ia.colocar_barcos_ia()
        while True:
            clear_terminal()
            # print(self.radar.coordenadas_barcos_ia)
            # print("tiradas posibles", self.tiradasPosibles)
            # print("disparos", self.disparos_computer)
            # print("aciertos",self.aciertos_computer)
            # print("fallos", self.fallos_computer)
            # print("Barcos usuario", todos_barcos)
            # print("Lista valores barcos", todos_barcos.values())
            # print("barcos hundidos", self.barcos_hundidos)
            # print("modo activo", self.modo)
            # print(self.disparo_ia(todos_barcos,coordenadas_barcos))
            self.print_ambos_tableros()
            # Función que decide los turnos de los jugadores
            if self.turnos(todos_barcos, todos_barcos_ia):
                break
            # if self.realizar_disparo():
            #     break
            # if self.disparo_ia(todos_barcos,coordenadas_barcos):
            #     break

partida = Juego()
partida.print_ambos_tableros()
partida.jugar()

