from Juego import *
# Los siguientes arrays son necesarios para iniciar el juego
# acierto=[]
# perdido=[]
disparos_computer=[]
disparos_user=[]
# acierto_computer=[]
# perdido_computer=[]
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
    disparo = Juego.obtener_disparo(disparos_user)
    # Comprobamos si el disparo ha sido acierto o fallo
    Juego.comprobar_disparo(disparo)
    print(disparo)
    print("acierto",acierto,"perdido",perdido)
    # Comprobamos si hemos completado un navio según el número de aciertos
    Juego.comprobar_barco_completo(acierto,acorazado,crucero,submarino)
    # Imprimimos las coordenadas del ordenador
    # Mostramos el tablero del ordenador y las posiciones de tiro correspondientes
    print("Tablero Ordenador")
    juego_user.view_board(acierto,perdido)
    # Comprobación si ha ganado el juego
    ganado=Juego.quien_gana()
    # Si ha ganado acaba el juego
    if ganado==True:
        break

    print("Juega el computador")
    # Obtenemos el disparo del ordenador
    disparo_computer = Juego.obtener_disparo_computer(acierto_computer, disparos_computer)
    # Comprobamos si el disparo es acierto o fallo
    Juego.comprobar_disparo_computer(disparo_computer)
    print("acierto computador", acierto_computer, "perdido_computador", perdido_computer)
    # Comprobamos si ha completado uno de los navios
    Juego.comprobar_barco_completo(acierto_computer,acorazado_user,crucero_user, submarino_user)
    # Mostramos las coordenadas del usuario, solo para pruebas
    print("User",total_coordenadas_Usuario)
    print("Tablero Usuario")
    # Mostramos el tablero el usuario con las posiciones de los barcos, los aciertos
    # del ordenador y los fallos
    juego_computer.view_board_juego(acierto_computer,perdido_computer)
    # Comprobamos si ha ganado el ordenador
    ganado=Juego.quien_gana()
    # Si ha ganado acaba el juego
    if ganado==True:
        break