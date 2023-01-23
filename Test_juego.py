from Bd_Sh_player import clear_terminal

def titulo():
    print('''  ▄█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▄
▄█▀                                                                                                                       ▀█▄
█   ████████▄     ▄█▀▀▀▀▀▀█▄    ██       ██       ██         ▄█▀▀▀▀▀▀▀▀   ▄███████▄    ▄█        █▄     ██     ▄██████▄     █
█   ██      ██   ██        ██   ██       ██       ██         ██          ██       ██   ██        ██            ██      ██   █
█   ██      ██   ██        ██   ██▀▀▀▀   ██▀▀▀▀   ██         ██          ▀█▄           ██        ██     ██     ██      ██   █
█   █████████    ██▀▀▀▀▀▀▀▀██   ██       ██       ██         ██▄▄▄▄▄▄      ██████▄     ██▄▄▄▄▄▄▄▄██     ██     ███████▀     █
█   ██      ██   ██        ██   ██       ██       ██         ██                  ▀█▄   ██        ██     ██     ██           █
█   ██      ██   ██        ██   ██       ██       ██         ██          ██       ██   ██        ██     ██     ██           █
█   ████████▀    ██        ██    ▀█▄▄▄    ▀█▄▄▄   ██▄▄▄▄▄▄   ▀█▄▄▄▄▄▄▄▄   ▀███████▀    ▀█        █▀     ██     ██           █
▀█▄                                                                                                                       ▄█▀
  ▀█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▀''')

def instrucciones():
    print('''Bienvenido a las instrucciones de Battleship. 
    
    Para jugar al battleship (Hundir la flota en castellano) ambos jugadores reciben dos tableros, la flota (Tablero en este programa) y el radar. 
    
        - La flota constituye el tablero donde los jugadores colocan sus barcos. Este tablero de 10x10 con coordenadas para codificar cada casilla es donde los jugadores               Barcos     
          colocarán sus cinco barcos de forma que estos no estén uno en cima del otro (ver ejemplo de la derecha). En este programa, los barcos colocados se                      0 1 2 3 4 5 6 7 8 9
          codifican en el tablero por la primera letra del nombre del barco (submarino = s).                                                                                    ┌─────────────────────┐
                                                                                                                                                                              0 │ a · · · · · · · · · │
        - El radar constituye la zona de disparo de los jugadores. Esta zona se relaciona con el tablero de flota del adversario, es decir, el radar del jugador 1            1 │ a · · · · · · · c · │
          representa la zona donde se alberga la flota del jugador 2. La primordial diferencia es que se desconoce la posición de los barcons enemigos.                       2 │ a · · · s s · · c · │
                                                                                                                                                                              3 │ a · · · · · · · c · │
                                                                                                                                                                              4 │ a · · · · · · · · · │
    En el transcurso de la partida, y una vez colocados los barcos de ambos jugadores, uno de los jugadores efectuara un disparo, por ejemplo, J1 dispara a                   5 │ · · · · · · · · · · │          
    las coordenadas 0 5 (Siempre se dice primero la fila y luego la columna), de forma que el disparo impacta en el tablero de flota del J2 en la fila 0                      6 │ · · · d d · · · · · │       
    columna 5. Si el disparo falla, es decir, que no alcanza a ningún barco enemigo, se suele decir 'Agua' y el turno pasa al J2. De esta forma, ambos jugadores              7 │ · · · · · · · · · · │               
    irán fallando y acertando los disparos hasta que uno de los jugadores se quede sin barcos (los barcos se consideran hundidos si todas sus coordenadas han                 8 │ · · · · p p p p · · │            
    sido impactadas por disparos del adversario)                                                                                                                              9 │ · · · · · · · · · · │                                           
                                                                                                                                                                                └─────────────────────┘
        
    
    
    
    
    
    
    ''')



















def menu():
    
    clear_terminal()
    titulo()
    
    starter = str(input("\n\nBienvenvenido, selecciona como quieres proceder:\n\n  0 - Jugar\n  1 - Instruciones del juego\n  q - Para salir\n\n >  "))
    while starter not in ["0","1","2","q"]:
        clear_terminal()
        titulo()
        starter = str(input("\n\nSelecciona una opción válida de las propuestas:\n\n  0 - Jugar\n  1 - Instruciones del juego\n  q - Para salir\n\n >  "))
    
    if starter == 0:
        clear_terminal()
        titulo()
        modo = int(input("\n\nSelecciona el modo de juego:\n\n  0 - Juagador vs AI\n  1 - Juagador vs jugador\n\n >  "))
    elif starter == 1:
        clear_terminal()
        titulo()
        tipo = int(input("\n\nSelecciona el modo de juego:\n\n  0 - Modo normal\n  1 - Modo rápido\n\n >  "))
    elif starter == 2:
        print("Github-link")
    
    else: print("Error")
menu()