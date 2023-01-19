import random
import os

total_coordenadas=[] #Guardo las coordenadas para saber si gana el usuario cuando el array esté vacio
total_coordenadas_Usuario=[] # Guardo las coordenadas del usuario para saber si gana el ordenador
#Diccionarios para saber las caracteristicas de cada navio, es necesario para ir pintando las posiciones
# que van quedando durante el juego
acorazado={} 
crucero={}
submarino={}
acorazado_user={}
crucero_user={}
submarino_user={}
# Array para saber las posiciones ocupadas, está creado pero aun no lo empleo, si no es necesario, se puede borrar 
posiciones_ocupadas=[]
# Ancho y alto definido inicialmente, necesito definirlas aqui para poder emplear estas variables en otras partes 
#del código
width=10
height=10

def LimpiarPantalla(): #Definimos la función para limpiar la pantalla despues de cada ejecución
    #Función no empleada aun
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

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
class Barcos:
    # La siguiente clase inicia los barcos del usuario
    def __init__(self, board): # Llamada al objeto tablero.

        self.board = board # Importa el tablero
        self.barcos = {"1": 4, "2": 3, "3": 2,} # Diccionario con los barcos y sus longitudes.

    def colocar_barcos(self):
        coordenadas=[]
        seleccion=["1","2","3"]

        while len(self.board.barcos_colocados) < len(self.barcos):# Premisa, si no están todos los barcos colocados seguimos ejecutando.
            siSeleccion=False
            # Bucle para asegurarse de que el usuario elige en navio correcto - Control de errores
            while siSeleccion==False:
                barco_elegido = input("Elige el barco a colocar (1=acorazado, 2=crucero, 3=submarino): ")# Selector de barcos.
                if barco_elegido not in seleccion:
                    print("Selección invalida, intente de nuevo")
                    siSeleccion=False
                else:
                    siSeleccion=True

            longitud = self.barcos[barco_elegido] # Extraemos su longitud

            if barco_elegido in self.board.barcos_colocados: # Comprobamos que no esté ya colocado.
                print(f"El barco {barco_elegido} ya esta colocado.") # <== Si lo está.
                continue
            barco_colocado = False

            longitud = self.barcos[barco_elegido] # Extraemos su longitud

            if barco_elegido in self.board.barcos_colocados: # Comprobamos que no esté ya colocado.
                print(f"El barco {barco_elegido} ya esta colocado.") # <== Si lo está.
                continue
            barco_colocado = False
            #Condiciones que me permiten guardar los datos de cada navio en el diccionario
            if barco_elegido == "1":
                acorazado_user["id"]="1"
                acorazado_user["L"]=longitud
            elif barco_elegido == "2":
                crucero_user["id"]="2"
                crucero_user["L"]=longitud
            elif barco_elegido=="3":
                submarino_user["id"]="3"
                submarino_user["L"]=longitud

            orientaciones=["v","h"]
            while barco_colocado == False: # Si no está colocado.
                orientacion = input("Orientación (v/h): ")# Atributos del barco.
                # Control de errores en la seleccion de orientacion
                if orientacion not in orientaciones:
                    print("Orientación invalida, introduzca v o h. vertical/horizontal")
                    barco_colocado=False
                else:
                    colocadoF=False
                    # Buche de control de errores en la seleccion de coordenadas.
                    while colocadoF == False:
                        try:
                            fila = int(input("Fila colocación: "))
                            if fila <0 or fila>9:
                                print("Debe introducir un valor entre 0 y 9")
                                colocadoF=False
                            else:
                                colocadoF=True
                        except ValueError:
                            print("Debe introducir un valor entre 0 y 9. Has introducido una letra.")
                            colocadoF=False
                        colocadoC=False
                    while colocadoC == False:
                        try:
                            columna = int(input("Columna Colocación: "))
                            if columna <0 or columna>9:
                                print("Debe introducir un valor entre 0 y 9")
                                colocadoC=False
                            else:
                                colocadoC=True
                        except ValueError:
                            print("Debe introducir un valor entre 0 y 9. Has introducido una letra")
                            colocadoC=False

                # Antes de pasar a poner los barcos en el tablero comprobamos que se puedan colocar en la posición especificada.
                if orientacion == "h": # Si queremos poner el barco en hoizontal.
                    #He cambiado la condicion de la longitud porque así queda más claro
                    #He hecho comprobaciones y la suma de columna o fila más longitud no debe sobrepasar 10
                    if columna + longitud > 10:
                        print("Barco fuera del tablero.")
                        barco_colocado = False
                    else:
                        barco_colocado = True    # Comprobamos que el barco no sobresalga del tablero. Premisa: Si sumamos la longitud del
                        # barco al numero de la columna y supera la longitud de la fila, está fuera del tablero
                        # Al ser un cuadrado no importa la fila con la que se realice la comprobación.
                elif orientacion == "v":                              # Realizamos la misma operación si queremos que el barco esté en vertical.
                    if fila + longitud > 10:
                        print("Barco fuera del tablero.")
                        barco_colocado = False 
                    else:
                        barco_colocado = True        # Premisa: Si sumamos la longitud del barco al número de la fila y el resultado
                        # es mayor que la longitud del tablero (Si su índice es mayor que el del tablero),
                        # está fuera del tablero.

                # Procedemos a colocar los barcos.
                posicion_ocupada = False
                bucle_activo = True
                #Aquí guardamos la orientación elegida de cada navio en el diccionario
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
                                #Aquí guardamos las coordenadas de cada navio
                                #Las paso a string para poder concatenar valores
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
                                #Aquí guardamos las coordenadas de cada navio
                                #Las paso a string para poder concatenar valores
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
            #Muestro las coordenadas del usuario, solo para pruebas
            #print("User",total_coordenadas_Usuario)
            self.board.view_board()
class BarcosComputer:
    #Esta clase me permite colocar los navios en posiciones random
    def __init__(self, board): # Llamada al objeto tablero.

        self.board = board # Importa el tablero
        self.barcos = {"1": 4,  "2": 3, "3": 2,} # Diccionario con los barcos y sus longitudes.

    def colocar_barcos(self):

        coordenadas=[]
        
        global total_coordenadas

        barcosRandom = ["1","2","3"]
        while len(self.board.barcos_colocados) < len(self.barcos): # Premisa, si no están todos los barcos colocados seguimos ejecutando.
            #Elegimos un barco del array, cada número pertenece a un navio diferente
            barco_elegido =random.choice(barcosRandom) # Selector de barcos.
            longitud = self.barcos[barco_elegido] # Extraemos su longitud

            if barco_elegido in self.board.barcos_colocados: # Comprobamos que no esté ya colocado.
                #print(f"El barco {barco_elegido} ya esta colocado.") # <== Si lo está.
                continue
            barco_colocado = False
            #Guardamos los datos en el diccionario de cada navio
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
                #El ordenador elige una orientación al azar
                orientacionRandom = random.choice(orientacion)
                #print("orientacion",orientacionRandom) # Atributos del barco.
                #El ordenador elige una fila random entre 0 y 9
                fila =random.randint(0,9)
                #print("fila",fila)
                #El ordenador elige una columna random entre 0 y 9
                columna = random.randint(0,9)
                #print("columna",columna)
                # Antes de pasar a poner los barcos en el tablero comprobamos que se puedan colocar en la posición especificada.
                if orientacionRandom == "h" and columna + longitud > 10: # Si queremos poner el barco en horizontal.
                    #print(f"Barco {barco_elegido} fuera del tablero, en fila.{columna+longitud}")
                    barco_colocado=False

                elif orientacionRandom == "v" and  fila + longitud > 10:                              # Realizamos la misma operación si queremos que el barco esté en vertical.
                    #print(f"Barco {barco_elegido} fuera del tablero, en columna. {fila+longitud}")
                    barco_colocado=False
                else:
                    barco_colocado=True
                # Guardamos la orientación de cada navio en su diccionario correspondiente
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
                                # Guardamos las coordenadas de cada navio en su diccionario
                                # correspondiente, es necesario tener un array de coordenadas
                                # para introducirlas posteriormente en el diccionario
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

                            self.board.barco_colocado(barco_elegido) # Guardamos el barco para que no se pueda colocar de nuevo.

                        elif orientacionRandom == "v": # Orientación Vertical.
                            for i in range(longitud): # Rango = longitud del barco.
                                #print("fila",fila,"i",i)
                                self.board.board[fila+i][columna] = barco_elegido[0] # Sustituimos el agua de las coordenadas por el barco.
                                # Guardamos las coordenadas de cada navio en su diccionario
                                # correspondiente, es necesario tener un array de coordenadas
                                # para introducirlas posteriormente en el diccionario
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

                            self.board.barco_colocado(barco_elegido) # Guardamos el barco para que no se pueda colocar de nuevo.

            # Mostramos las coordenadas del ordenador para detectar errores, no mostrar en el juego definitivo
            #print("Computer",total_coordenadas)

# Función para obtener los disparos del usuario
def obtener_disparo(disparos_user):
    ok = False
    # Mientras ok sea Falso, o sea que mientras no se hayan introducido unas coordenadas válidas 
    # no se guardará el tiro
    while ok == False:
        try:
            fila = input("Introduzca una fila de tiro: ")
            columna = input("Introduzca una columna de tiro: ")
            #Necesito pasarlo a entero para verificar si es una coordenada válida
            disparo = int(fila+columna)
            if disparo < 0 or disparo > 99:
                print("Número incorrecto, intente de nuevo")
            else:
                # En caso de que sea valido lo paso a string para poder concatenarlos
                disparo=str(fila+columna)
                #Si el disparo está en el array quiere decir que está repetido
                if  disparo in disparos_user:
                    print("Número repetido, intente de nuevo")
                else:
                    ok=True
        except:
            print("Entrada incorrecta - por favor, intentelo de nuevo")
    #Guardo los disparos correctos en el array
    disparos_user.append(disparo)
    return disparo
# La siguiente funcion me crea un disparo del ordenador teniendo en cuenta
# los aciertos y los disparos ya realizados
def obtener_disparo_computer(acierto_computer, disparos_computer):

    disparo=0
    intento=False
    diferente=True
    # Mientras el disparo se considere diferente del disparo guardado en el array
    # El bucle seguirá activo
    while diferente==True:
        fila = random.randint(0,9)
        columna = random.randint(0,9)
        # En caso de que haya datos en el array de aciertos se seguiran las siguientes
        # tácticas de tiro
        if len(acierto_computer)>0:  
            # De los aciertos del computador cogemos del último tiro el número que corresponde
            # a la fila. ej. "16", posición "0"="1" es fila, posición "1"="6" es columna          
            filaMenos=int(acierto_computer[-1][0])-1
            filaMas=int(acierto_computer[-1][0])+1
            columnaMenos=int(acierto_computer[-1][1])-1
            columnaMas=int(acierto_computer[-1][1])+1
            # Mientras el intento de tiro sea falso, el bucle sigue activo.
            # El bucle acaba cuando consigue un disparo válido
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
        # Esta condición me comprueba si el disparo es diferente a los que están 
        # guardados en el array de disparos_computer
        if len(disparos_computer)>0:
            if disparo in disparos_computer:
                diferente=True
            else:
                #Si no está en el array, me lo guarda y retorna el disparo
                disparos_computer.append(disparo)
                diferente=False
                return disparo
        else:
            #Si no hay datos en el array, me lo guarda y retorna el disparo
            disparos_computer.append(disparo)
            diferente=False
            return disparo

def comprobar_disparo(disparo): #Comprobamos si el disparo ha tocado una de las posiciones de barco
    # Si el disparo coincide con un elemento del array del computador, es que habrá acertado
    if disparo in total_coordenadas:
        # Guardamos el disparo en el array de aciertos
        acierto.append(disparo)
        # Borramos la coordenada del disparo del array de coordenadas del ordenador
        total_coordenadas.remove(disparo)
    else:
        # En caso de fallo guardamos el disparo en el array de fallos
        perdido.append(disparo)

    return acierto, perdido
# En esta función comprobamos el disparo del computador
def comprobar_disparo_computer(disparo):
    # Si el disparo coincide con un elemento del array de coordenadas del usuario
    if disparo in total_coordenadas_Usuario:
        # Guardamos el acierto en el array de aciertos del computador
        acierto_computer.append(disparo)
        # Eliminamos la coordenada del array de coordenadas del usuario
        total_coordenadas_Usuario.remove(disparo)
    else:
        # Si falla guardamos el disparo en el array de disparos perdidos
        perdido_computer.append(disparo)

    return acierto_computer, perdido_computer
# Comprobación de que se ha hundido un navio
def comprobar_barco_completo(aciertos,acorazado,crucero,submarino):
    # Cada contador guardará el número de aciertos de cada navio y lo 
    # comparará con la longitud del navio correspondiente
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
# Esta función comprueba quien ha ganado el juego
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
# Los siguientes arrays son necesarios para iniciar el juego
acierto=[]
perdido=[]
disparos_computer=[]
disparos_user=[]
acierto_computer=[]
perdido_computer=[]
# Llamamos al la clase "Board_player" para iniciar el tablero vacio y guardar
# las posiciones de los navios
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
# Mientras el tamaño de las coordenadas de cualquiera de los jugadores sea máyor de 0 y no 
# haya un ganador el juego continua
while (len(total_coordenadas)>0 or len(total_coordenadas_Usuario)>0) and ganado==False:
    # Visualizamos las coordenadas del ordenador, solo para pruebas
    print("computer",total_coordenadas)
    print("Juega el usuario")
    # Obtenemos los disparos del usuario
    disparo = obtener_disparo(disparos_user)
    # Comprobamos si el disparo ha sido acierto o fallo
    comprobar_disparo(disparo)
    print(disparo)
    print("acierto",acierto,"perdido",perdido)
    # Comprobamos si hemos completado un navio según el número de aciertos
    comprobar_barco_completo(acierto,acorazado,crucero,submarino)
    # Imprimimos las coordenadas del ordenador
    # Mostramos el tablero del ordenador y las posiciones de tiro correspondientes
    print("Tablero Ordenador")
    juego_user.view_board(acierto,perdido)
    # Comprobación si ha ganado el juego
    ganado=quien_gana()
    # Si ha ganado acaba el juego
    if ganado==True:
        break

    print("Juega el computador")
    # Obtenemos el disparo del ordenador
    disparo_computer = obtener_disparo_computer(acierto_computer, disparos_computer)
    # Comprobamos si el disparo es acierto o fallo
    comprobar_disparo_computer(disparo_computer)
    print("acierto computador", acierto_computer, "perdido_computador", perdido_computer)
    # Comprobamos si ha completado uno de los navios
    comprobar_barco_completo(acierto_computer,acorazado_user,crucero_user, submarino_user)
    # Mostramos las coordenadas del usuario, solo para pruebas
    print("User",total_coordenadas_Usuario)
    print("Tablero Usuario")
    # Mostramos el tablero el usuario con las posiciones de los barcos, los aciertos
    # del ordenador y los fallos
    juego_computer.view_board_juego(acierto_computer,perdido_computer)
    # Comprobamos si ha ganado el ordenador
    ganado=quien_gana()
    # Si ha ganado acaba el juego
    if ganado==True:
        break