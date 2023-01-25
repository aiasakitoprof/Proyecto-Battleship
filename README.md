# Proyecto-Battleship
En el archivo battleship_pygame.py está toda la lógica del juego en pygame.   
Las reglas del juego y su lógica son muy similares al juego realizado en terminal, pero adaptadas a pygame.  
Pygame permite realizar juegos más interactivos  
Aparte de esta libreria he añadido otra llamada PySimpleGUI que permite crear una ventana paralela donde introducir datos para el juego.  
El juego, cuando se inicia se presentan dos tableros, el Radar, donde lanzará las tiradas el usuario hacia el ordenador y el tablero de 
Barcos, donde se muestran los barcos colocados por el usuario y las tiradas del ordenador.  
También sale una pequeña ventana donde introducir los datos para colocar cada barco.  
![Imagen inicial del juego de hundir la flota](https://github.com/aiasakitoprof/Proyecto-Battleship/blob/pygame/assets/juego1.jpg)  
Una vez colocados los 5 barcos por sus medidas y colores se inicia la ventana de tiradas del usuario, por cada tirada del usuario
se lanzará una tirada del ordenador.  
El juego acaba cuando uno de los dos jugadores ha destruido todos los barcos del oponente.  
#### Mejoras a realizar
* Se deberían dividir la lógica del juego en archivo diferentes por clases y llamarlas en un archivo inicial de juego  
* Se debe depurar más el código para descartar pequeños fallos.  
* Se puede mejorar mucho más el juego, este es un pequeño ejemplo de como realizar un juego de hundir la flota en pygame.  
