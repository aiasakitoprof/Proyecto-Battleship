import random
import os

total_coordenadas=[]
total_coordenadas_Usuario=[]
acorazado={}
crucero={}
submarino={}
acorazado_user={}
crucero_user={}
submarino_user={}
posiciones_ocupadas=[]
width=10
height=10

def LimpiarPantalla(): #Definimos la función para limpiar la pantalla despues de cada ejecución
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


class Board_computer:

    def __init__(self, width=10, height=10): # Llamada al objeto tablero.

        self.board = [["." for i in range(width)] for i in range(height)] #  Bucle para crear el tablero.
        self.barcos_colocados = {} # Guarda los barcos ya colocados.
        barquitos=self.barcos_colocados
        print(barquitos)



    def barco_colocado(self, barco):
        self.barcos_colocados[barco] = True

class Tablero_Computer:


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
                
            
        
        print("  ", end="") # Hueco separador de coordenadas.

        for i in range(len(self.board[0])): # Coordenadas de columnas (Encima del tablero).
            print(i, end=" ")
        print()

        for i, row in enumerate(self.board): # Coordenadas de filas (A la derecha del tablero).
            print(i, end=" ")
            print(" ".join(row))
    


class Tablero_User:


    def __init__(self): # Llamada al objeto tablero.
        pinta="."
        self.board = [[pinta for i in range(width)] for j in range(height)]
    


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
    
                

                
            
        
            print("  ", end="") # Hueco separador de coordenadas.

            for i in range(len(self.board[0])): # Coordenadas de columnas (Encima del tablero).
                print(i, end=" ")
            print()

            for i, row in enumerate(self.board): # Coordenadas de filas (A la derecha del tablero).
                print(i, end=" ")
                print(" ".join(row))

class Barcos:

    def __init__(self, board): # Llamada al objeto tablero.

        self.board = board # Importa el tablero
        self.barcos = {"1": 4, "2": 3, "3": 2,} # Diccionario con los barcos y sus longitudes.


    def colocar_barcos(self):
        coordenadas=[]
        ok=False

        while len(self.board.barcos_colocados) < len(self.barcos):# Premisa, si no están todos los barcos colocados seguimos ejecutando.
            while ok==False:
                try:
                    barco_elegido = input("Elige el barco a colocar (1=acorazado, 2=crucero, 3=submarino): ")
                    barco_elegido=int(barco_elegido) # Selector de barcos.
                    if barco_elegido <0 or barco_elegido>3:
                        print("Barco incorrecto")
                    else:
                        barco_elegido=str(barco_elegido)
                        ok=True
                except ValueError:
                    print("Has introducido una letra, debes introducir 1, 2 o 3")
                    ok==False

            longitud = self.barcos[barco_elegido] # Extraemos su longitud

            if barco_elegido in self.board.barcos_colocados: # Comprobamos que no esté ya colocado.
                print(f"El barco {barco_elegido} ya esta colocado.") # <== Si lo está.
                continue
            barco_colocado = False

            if barco_elegido == "1":
                acorazado_user["id"]="1"
                acorazado_user["L"]=longitud
            elif barco_elegido == "2":
                crucero_user["id"]="2"
                crucero_user["L"]=longitud
            elif barco_elegido=="3":
                submarino_user["id"]="3"
                submarino_user["L"]=longitud

            while barco_colocado == False: # Si no está colocado.
                try:
                    orientacion = input("Orientación (v/h): ")
                except ValueError: # Atributos del barco.
                    print("Orientación invalida, introduzca v o h. vertical/horizontal")
                    barco_colocado=False
                try:
                    fila = int(input("Fila colocación: "))
                    if fila <0 or fila>9:
                        print("Debe introducir un valor entre 0 y 9")
                        fila = int(input("Fila colocación: "))
                except ValueError:
                    print("Debe introducir un valor entre 0 y 9")
                    fila = int(input("Fila colocación: "))
                try:
                    columna = int(input("Columna Colocación: "))
                    if columna <0 or columna>9:
                        print("Debe introducir un valor entre 0 y 9")
                        columna = int(input("Columna colocación: "))
                except ValueError:
                    print("Debe introducir un valor entre 0 y 9")
                    columna = int(input("Columna colocación: "))


                # Antes de pasar a poner los barcos en el tablero comprobamos que se puedan colocar en la posición especificada.
                if orientacion == "h": # Si queremos poner el barco en hoizontal.
                    if columna + longitud > 9:
                        print("Barco fuera del tablero.")
                        barco_colocado = False
                    else:
                        barco_colocado = True    # Comprobamos que el barco no sobresalga del tablero. Premisa: Si sumamos la longitud del
                        
                        # barco al numero de la columna y supera la longitud de la fila, está fuera del tablero
                        # Al ser un cuadrado no importa la fila con la que se realice la comprobación.

                elif orientacion == "v":                              # Realizamos la misma operación si queremos que el barco esté en vertical.
                    if fila + longitud > 9:
                        print("Barco fuera del tablero.")
                        barco_colocado = False 
                    else:
                        barco_colocado = True        # Premisa: Si sumamos la longitud del barco al número de la fila y el resultado
                
                        # es mayor que la longitud del tablero (Si su índice es mayor que el del tablero),
                        # está fuera del tablero.

                else:
                    print("Orientación inválida")
                    barco_colocado = False
                    

                # Procedemos a colocar los barcos.
                posicion_ocupada = False
                bucle_activo = True


                if barco_elegido == "1":
                    acorazado_user["orienta"]=orientacion
                elif barco_elegido == "2":
                    crucero_user["orienta"]=orientacion
                elif barco_elegido=="3":
                    submarino_user["orienta"]=orientacion

            while bucle_activo:

                    if orientacion == "h": # Si la orientación es horizontal.
                        for i in range(longitud): # Rango = longitud del barco.
                            if self.board.board[fila][columna + i] != ".": # Si la posición de inicio del barco es diferente al agua.
                                print("Posición ocupada.")
                                posicion_ocupada = True
                                bucle_activo = False

                    elif orientacion == "v":  # Si la orientación es vertical.
                        for i in range(longitud): # Rango = longitud del barco.
                            if self.board.board[fila + i][columna] != ".":  # Si la posición de inicio del barco es diferente al agua.
                                print("Posición ocupada.")
                                posicion_ocupada = True
                                bucle_activo = False

                                coordenadas=[]

                    if not posicion_ocupada: # Si la posición no está ocupada.

                        if orientacion == "h": # Orientación horizontal.
                            for i in range(longitud): # Rango = longitud del barco.
                                self.board.board[fila][columna + i] = barco_elegido[0] # Sustituimos el agua de las coordenadas por el barco.
                            
                                coordenadas.append(str(fila)+str(columna+i))
                                total_coordenadas_Usuario.append(str(fila)+str(columna+i))
                                if barco_elegido == "1":
                                    acorazado_user["coordenadas"]=coordenadas
                                elif barco_elegido == "2":
                                    crucero_user["coordenadas"]=coordenadas
                                elif barco_elegido == "3":
                                    submarino_user["coordenadas"]=coordenadas
                            
                            
                            
                            barco_colocado = True
                            coordenadas=[]
                            self.board.barco_colocado(barco_elegido) # Guardamos el arco para que no se pueda colocar de nuevo.
                            print(f"Barco {barco_elegido} colocado en posición {fila}, {columna} con orientación horizontal.")

                        elif orientacion == "v": # Orientación Vertical.
                            for i in range(longitud): # Rango = longitud del barco.
                                self.board.board[fila + i][columna] = barco_elegido[0] # Sustituimos el agua de las coordenadas por el barco.
                            
                                coordenadas.append(str(fila+i)+str(columna))
                                total_coordenadas_Usuario.append(str(fila+i)+str(columna))
                                if barco_elegido == "1":
                                    acorazado_user["coordenadas"]=coordenadas
                                elif barco_elegido == "2":
                                    crucero_user["coordenadas"]=coordenadas
                                elif barco_elegido == "3":
                                    submarino_user["coordenadas"]=coordenadas
                            
                            
                            barco_colocado = True
                            coordenadas=[]
                            self.board.barco_colocado(barco_elegido) # Guardamos el arco para que no se pueda colocar de nuevo.
                            print(f"Barco {barco_elegido} colocado en posición {fila}, {columna} con orientación vertical.")
            print("User",total_coordenadas_Usuario)
            # print(acorazado_user)
            # print(crucero_user)
            # print(submarino_user)
            self.board.view_board()

class BarcosComputer:


    def __init__(self, board): # Llamada al objeto tablero.

        self.board = board # Importa el tablero
        self.barcos = {"1": 4,  "2": 3, "3": 2,} # Diccionario con los barcos y sus longitudes.

    def colocar_barcos(self):
        # acorazado={}
        # crucero={}
        # submarino={}
        coordenadas=[]
        
        global total_coordenadas

        barcosRandom = ["1","2","3"]
        while len(self.board.barcos_colocados) < len(self.barcos): # Premisa, si no están todos los barcos colocados seguimos ejecutando.

            barco_elegido =random.choice(barcosRandom) # Selector de barcos.
            longitud = self.barcos[barco_elegido] # Extraemos su longitud

            if barco_elegido in self.board.barcos_colocados: # Comprobamos que no esté ya colocado.
                #print(f"El barco {barco_elegido} ya esta colocado.") # <== Si lo está.

                continue
            barco_colocado = False

            if barco_elegido == "1":
                acorazado["id"]="1"
                acorazado["L"]=longitud
            elif barco_elegido == "2":
                crucero["id"]="2"
                crucero["L"]=longitud
            elif barco_elegido=="3":
                submarino["id"]="3"
                submarino["L"]=longitud


            while barco_colocado==False: # Si no está colocado.
                orientacion=["v","h"]
                orientacionRandom = random.choice(orientacion)
                #print("orientacion",orientacionRandom) # Atributos del barco.
                fila =random.randint(0,9)
                #print("fila",fila)
                columna = random.randint(0,9)
                #print("columna",columna)

                # Antes de pasar a poner los barcos en el tablero comprobamos que se puedan colocar en la posición especificada.
                if orientacionRandom == "h" and columna + longitud > 9: # Si queremos poner el barco en horizontal.
                    #print(f"Barco {barco_elegido} fuera del tablero, en fila.{columna+longitud}")
                    barco_colocado=False


                elif orientacionRandom == "v" and  fila + longitud > 9:                              # Realizamos la misma operación si queremos que el barco esté en vertical.
                    #print(f"Barco {barco_elegido} fuera del tablero, en columna. {fila+longitud}")
                    barco_colocado=False

                else:
                    barco_colocado=True




                if barco_elegido == "1":
                    acorazado["orienta"]=orientacionRandom
                elif barco_elegido == "2":
                    crucero["orienta"]=orientacionRandom
                elif barco_elegido=="3":
                    submarino["orienta"]=orientacionRandom



                # Procedemos a colocar los barcos.
                posicion_ocupada = False
                bucle_activo = True



            while bucle_activo:

                    if orientacionRandom == "h": # Si la orientación es horizontal.

                        for i in range(longitud): # Rango = longitud del barco.
                            #print("longitud",longitud)
                            #print("barco",barco_elegido,"columna",columna+i)
                            #print("posicion fila",fila, "posicion columna",columna,"i",i,"columna + i",columna+i)
                            if self.board.board[fila][columna + i] != ".": # Si la posición de inicio del barco es diferente al agua.
                                #print("Posición ocupada.")

                                posicion_ocupada = True
                                bucle_activo=False
                                coordenadas=[]





                    elif orientacionRandom == "v":  # Si la orientación es vertical.

                        for i in range(longitud): # Rango = longitud del barco.
                            #print(longitud)
                            #print("barco",barco_elegido,"fila",fila+i)

                            # print(self.board.board[fila + i][columna])
                            #print("posicion fila",fila, "i",i,"fila+i",fila+i,"columna",columna)
                            if self.board.board[fila + i][columna] != ".":  # Si la posición de inicio del barco es diferente al agua.
                                #print("Posición ocupada.")


                                posicion_ocupada = True
                                bucle_activo = False
                                coordenadas=[]

                    if not posicion_ocupada: # Si la posición no está ocupada.

                        if orientacionRandom == "h": # Orientación horizontal.
                            for i in range(longitud): # Rango = longitud del barco.
                                #print("columna",columna,"i",i)
                                self.board.board[fila][columna + i] = barco_elegido[0] # Sustituimos el agua de las coordenadas por el barco.
                            
                                coordenadas.append(str(fila)+str(columna+i))
                                total_coordenadas.append(str(fila)+str(columna+i))
                                if barco_elegido == "1":
                                    acorazado["coordenadas"]=coordenadas
                                elif barco_elegido == "2":
                                    crucero["coordenadas"]=coordenadas
                                elif barco_elegido == "3":
                                    submarino["coordenadas"]=coordenadas

                            barco_colocado = True
                            coordenadas=[]
                            # todosBarcos.append(acorazado)
                            # todosBarcos.append(crucero)
                            # todosBarcos.append(submarino)

                            # todasCoordenadas.append(acorazado["coordenadas"])
                            # todasCoordenadas.append(crucero["coordenadas"])
                            # todasCoordenadas.append(submarino["coordenadas"])


                            self.board.barco_colocado(barco_elegido) # Guardamos el barco para que no se pueda colocar de nuevo.

                            # print(f"Barco {barco_elegido} colocado en posición {fila}, {columna} con orientación horizontal.")

                        elif orientacionRandom == "v": # Orientación Vertical.
                            for i in range(longitud): # Rango = longitud del barco.
                                #print("fila",fila,"i",i)
                                self.board.board[fila+i][columna] = barco_elegido[0] # Sustituimos el agua de las coordenadas por el barco.

                                coordenadas.append(str(fila+i)+str(columna))
                                total_coordenadas.append(str(fila+i)+str(columna))
                                if barco_elegido == "1":
                                    acorazado["coordenadas"]=coordenadas
                                elif barco_elegido == "2":
                                    crucero["coordenadas"]=coordenadas
                                elif barco_elegido == "3":
                                    submarino["coordenadas"]=coordenadas

                            barco_colocado = True
                            coordenadas=[]
                            # todosBarcos.append(acorazado)
                            # todosBarcos.append(crucero)
                            # todosBarcos.append(submarino)

                            # todasCoordenadas.append(acorazado["coordenadas"])
                            # todasCoordenadas.append(crucero["coordenadas"])
                            # todasCoordenadas.append(submarino["coordenadas"])
                            self.board.barco_colocado(barco_elegido) # Guardamos el barco para que no se pueda colocar de nuevo.


                            #print(f"Barco {barco_elegido} colocado en posición {fila}, {columna} con orientación vertical.")



            #self.board.view_board()
            #print(acorazado)
            #print(crucero)
            #print(submarino)
            print("Computer",total_coordenadas)
            



def obtener_disparo(disparos_user):

    ok = False
    while ok == False:
        try:
            fila = input("Introduzca una fila de tiro: ")
            columna = input("Introduzca una columna de tiro: ")
            disparo = int(fila+columna)
            if disparo < 0 or disparo > 99:
                print("Número incorrecto, intente de nuevo")
            
            else:
                disparo=str(fila+columna)
                if  disparo in disparos_user:
                    print("Número repetido, intente de nuevo")
                else:
                    ok=True
        except:
            print("Entrada incorrecta - por favor, intentelo de nuevo")
    disparos_user.append(disparo)
    return disparo

def obtener_disparo_computer(acierto_computer, disparos_computer):

    
    disparo=0
    intento=False
    diferente=True
    while diferente==True:
        fila = random.randint(0,9)
        columna = random.randint(0,9)
        if len(acierto_computer)>0:            
            filaMenos=int(acierto_computer[-1][0])-1
            filaMas=int(acierto_computer[-1][0])+1
            columnaMenos=int(acierto_computer[-1][1])-1
            columnaMas=int(acierto_computer[-1][1])+1
            
            while intento==False:
                arriba_abajo=random.choice([fila,columna])
                if arriba_abajo==fila:
                    fila=random.choice([filaMenos,filaMas])
                    columna=int(acierto_computer[-1][1])
                    if filaMenos<0:
                        fila=filaMas
                    elif filaMas>9:
                        fila=filaMenos
                if arriba_abajo==columna:
                    fila=int(acierto_computer[-1][0])
                    columna=random.choice([columnaMenos,columnaMas])
                    if columnaMenos<0:
                        columna=columnaMas
                    elif columnaMas>9:
                        columna=columnaMenos
                disparo = str(fila)+str(columna)
                intento=True
        else:
            disparo = str(fila)+str(columna)
            
        
        if len(disparos_computer)>0:
            if disparo in disparos_computer:
                diferente=True
            else:
                disparos_computer.append(disparo)
                diferente=False
                return disparo
        else:
            diferente=False
            return disparo
    


def comprobar_disparo(disparo): #Comprobamos si el disparo ha tocado una de las posiciones de barco

    if disparo in total_coordenadas:
        acierto.append(disparo)
        total_coordenadas.remove(disparo)
    else:
        perdido.append(disparo)

    return acierto, perdido

def comprobar_disparo_computer(disparo):
    if disparo in total_coordenadas_Usuario:
        acierto_computer.append(disparo)
        total_coordenadas_Usuario.remove(disparo)
    else:
        perdido_computer.append(disparo)

    return acierto_computer, perdido_computer

def comprobar_barco_completo(aciertos,acorazado,crucero,submarino):
    contadorA=0
    contadorC=0
    contadorS=0
    for aciertos in acierto:
        if aciertos in acorazado["coordenadas"]:
            contadorA+=1
            if len(acorazado["coordenadas"]) == contadorA:
                print("Has acabado con el acorazado!!")
        elif aciertos in crucero["coordenadas"]:
            contadorC+=1
            if len(acorazado["coordenadas"]) == contadorC:
                print("Has acabado con el crucero!!")
        elif aciertos in submarino:
            contadorS+=1
            if len(submarino["coordenandas"])==contadorS:
                print("Has acabado con el submarino")

def quien_gana():
    if len(total_coordenadas)<=0:
        print("Has ganado, enhorabuena")
        gana=True
    elif len(total_coordenadas_Usuario)<=0:
        print("Ha ganado el Ordenador")
        gana=True
    else:
        gana=False
    return gana


acierto=[]
perdido=[]
disparos_computer=[]
disparos_user=[]
acierto_computer=[]
perdido_computer=[]

test_board = Board_player()
print("Tablero Usuario")
test_board.view_board()
barcos = Barcos(test_board)
barcos.colocar_barcos()
juego_computer =Tablero_User()





test_board2 = Board_computer()
#test_board2.view_board()
barcos2 = BarcosComputer(test_board2)
barcos2.colocar_barcos()
#Accedemos al Tablero del computador
juego_user = Tablero_Computer()

#Visualizamos el Tablero
print("Tablero Ordenador")
juego_user.view_board(acierto,perdido)
ganado=False
while (len(total_coordenadas)>0 or len(total_coordenadas_Usuario)>0) and ganado==False:
    print("Juega el usuario")
    disparo = obtener_disparo(disparos_user)
    comprobar_disparo(disparo)
    print(disparo)
    print("acierto",acierto,"perdido",perdido)
    comprobar_barco_completo(acierto,acorazado,crucero,submarino)
    print("computer",total_coordenadas)
    print("Tablero Ordenador")
    juego_user.view_board(acierto,perdido)
    ganado=quien_gana()
    if ganado==True:
        break
    #print(ganado)

    print("Juega el computador")
    disparo_computer = obtener_disparo_computer(acierto_computer, disparos_computer)
    comprobar_disparo_computer(disparo_computer)
    print("acierto computador", acierto_computer, "perdido_computador", perdido_computer)
    comprobar_barco_completo(acierto_computer,acorazado_user,crucero_user, submarino_user)
    print("User",total_coordenadas_Usuario)
    print("Tablero Usuario")
    juego_computer.view_board_juego(acierto_computer,perdido_computer)
    ganado=quien_gana()
    if ganado==True:
        break
    #print(ganado)
    




    
