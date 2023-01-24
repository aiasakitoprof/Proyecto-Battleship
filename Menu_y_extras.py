from Jugador import clear_terminal

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
    print(f'''\n\nBienvenido a las instrucciones de Battleship. 
    
Para jugar al battleship (Hundir la flota en castellano) ambos jugadores reciben dos tableros, la flota (Tablero en este programa) y el radar. 

    - La flota constituye el tablero donde los jugadores colocan sus barcos. Este tablero de 10x10 con coordenadas para codificar cada casilla es donde los jugadores
      colocarán sus cinco barcos de forma que estos no estén uno en cima del otro (ver ejemplo de la derecha). En este programa, los barcos colocados se               
      codifican en el tablero por la primera letra del nombre del barco (submarino = s).                                                                                 

    - El radar constituye la zona de disparo de los jugadores. Esta zona se relaciona con el tablero de flota del adversario, es decir, el radar del jugador 1           
      representa la zona donde se alberga la flota del jugador 2. La primordial diferencia es que se desconoce la posición de los barcons enemigos.                      


En el transcurso de la partida, y una vez colocados los barcos de ambos jugadores, uno de los jugadores efectuara un disparo, por ejemplo, J1 dispara a                   
las coordenadas 0 5 (Siempre se dice primero la fila y luego la columna), de forma que el disparo impacta en el tablero de flota del J2 en la fila 0                            
columna 5. Si el disparo falla, es decir, que no alcanza a ningún barco enemigo, se suele decir 'Agua' y el turno pasa al J2. De esta forma, ambos jugadores                            
irán fallando y acertando los disparos hasta que uno de los jugadores se quede sin barcos (los barcos se consideran hundidos si todas sus coordenadas han                            
sido impactadas por disparos del adversario)                                                                                                                                                                        

A continuación se muestra una partida empezada como referencia:
    
           Radar                       Barcos
    0 1 2 3 4 5 6 7 8 9          0 1 2 3 4 5 6 7 8 9
  ┌─────────────────────┐      ┌─────────────────────┐
0 │ · · · · O X · · · · │    0 │ · · · O · · · O · · │
1 │ · · · O · X · · O · │    1 │ · · O · d X · c · O │
2 │ · · · · · X · · · · │    2 │ O · p O · O · c · · │
3 │ · · · · · X · · · · │    3 │ · · p · · · · c O · │
4 │ · · · O · X · · · · │    4 │ O · p O · · · · · · │
5 │ · · · · · O · · · · │    5 │ · · p · · · · · · · │
6 │ · · · · O · · · · · │    6 │ · · · · · · · · · · │
7 │ · · · · · · · O · · │    7 │ · · · · O a a X a a │
8 │ O · O · · · · · · · │    8 │ O · · · · · · · · · │
9 │ · · · · O · · · · · │    9 │ s s · · · · · · · · │
  └─────────────────────┘      └─────────────────────┘
''')


def menu():
    
    while True:
      starter = "b"
      break
    

    while True:
    
      if starter == "b":
        
        clear_terminal()
        titulo()
        starter = str(input("\n\nBienvenvenido, selecciona como quieres proceder:\n\n  0 - Jugar\n  1 - Instruciones del juego\n  2 - Link a nuestro Github\n  q - Para salir\n\n >  "))
        
        
        while starter not in ["0","1","2","q"]:
            clear_terminal()
            titulo()
            starter = str(input("\n\nBienvenvenido, selecciona como quieres proceder:\n\n  0 - Jugar\n  1 - Instruciones del juego\n  2 - Link a nuestro Github\n  q - Para salir\n\n Selecciona una opción válida >  "))
    
    
      if starter == "0":
        
        clear_terminal()
        titulo()
        modo = str(input("\n\nSelecciona el modo de juego:\n\n  0 - Juego rápido\n  1 - Colocación manual\n  b - Volver atrás\n  q - Para salir\n\n >  "))
        
        while modo not in ["0","1","b","q"]:
          
          clear_terminal()
          titulo()
          modo = str(input("\n\nSelecciona el modo de juego:\n\n  0 - Juego rápido\n  1 - Colocación manual\n  b - Volver atrás\n  q - Para salir\n\n Selecciona una opción válida >  "))

        if modo in ["b","q"]:
          starter = modo

      elif starter == "1":
        
        clear_terminal()
        titulo()
        instrucciones()
        starter = str(input("\n  b - Volver atrás\n  q - Para salir\n\n >  "))
        
        
        while starter not in ["b","q"]:
          
          clear_terminal()
          titulo()
          instrucciones()
          starter = str(input("\n  b - Volver atrás\n  q - Para salir\n\n Selecciona una opción válida >  "))
    
    
      elif starter == "2":
        
        clear_terminal()
        titulo()
        print("\n\nGithub-link")
        starter = str(input("\n  b - Volver atrás\n  q - Para salir\n\n >  "))
        
        
        while starter not in ["b","q"]:

          clear_terminal()
          titulo()
          print("\n\nGithub-link")
          starter = str(input("\n  b - Volver atrás\n  q - Para salir\n\n Selecciona una opción válida >  "))
      
      elif starter == "q":
        clear_terminal()
        titulo()
        print("\n\nQue tengas un buen día.\n")
        exit()
      
      else: print("Error")

      if modo in ["0","1"]:
        break
      else: pass
    return modo