from colorama import Fore, Back, Style
from Bd_Sh_player import clear_terminal
def game_over():
        print("███▀▀▀██ ███▀▀▀███ ███▀█▄█▀███ ██▀▀▀")
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



def titulo():
    print('''▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▄
                                                                                                                      ▀█▄
████████▄     ▄█▀▀▀▀▀▀█▄    ██       ██       ██         ▄█▀▀▀▀▀▀▀▀   ▄███████▄    ▄█        █▄     ██     ▄██████▄     █
██      ██   ██        ██   ██       ██       ██         ██          ██       ██   ██        ██            ██      ██   █
██      ██   ██        ██   ██▀▀▀▀   ██▀▀▀▀   ██         ██          ▀█▄           ██        ██     ██     ██      ██   █
█████████    ██▀▀▀▀▀▀▀▀██   ██       ██       ██         ██▄▄▄▄▄▄      ██████▄     ██▄▄▄▄▄▄▄▄██     ██     ███████▀     █
██      ██   ██        ██   ██       ██       ██         ██                  ▀█▄   ██        ██     ██     ██           █
██      ██   ██        ██   ██       ██       ██         ██          ██       ██   ██        ██     ██     ██           █
████████▀    ██        ██    ▀█▄▄▄    ▀█▄▄▄   ██▄▄▄▄▄▄   ▀█▄▄▄▄▄▄▄▄   ▀███████▀    ▀█        █▀     ██     ██           █
                                                                                                                      ▄█▀
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▀''')

def menu():
    clear_terminal()
    titulo()
    starter = input("\n\nBienvenvenido, selecciona como quieres proceder:\n\n  0 - Jugar\n  1 - Instruciones del juego\n  2 - Repositorio de github\n\n >  ")
    
    clear_terminal()
    titulo()
    modo = input("\n\nSelecciona el modo de juego:\n\n  0 - Juagador vs AI\n  1 - Juagador vs jugador\n\n >  ")
    
    clear_terminal()
    titulo()
    tipo = input("\n\nSelecciona el modo de juego:\n\n  0 - Modo normal\n  1 - Modo rápido\n\n >  ")

menu()