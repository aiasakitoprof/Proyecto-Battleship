# Proyecto-Battleship
En el archivo battleship_pygame.py está toda la lógica del juego en pygame.     
Las reglas del juego y su lógica son muy similares al juego realizado en terminal, pero mucho del trabajo ya estaba realizado.    
Lo que se ha pretendido en esta versión es mostrar otra forma diferente y más avanzada de realizar el mismo juego.  
Pygame permite realizar juegos más interactivos.  
Aparte de esta libreria he añadido otra, llamada PySimpleGUI que permite crear una ventana paralela donde introducir datos para el juego.    
El juego, cuando se inicia se presentan dos tableros, el Radar, donde lanzará las tiradas el usuario hacia el ordenador y el tablero de 
Barcos, donde se muestran los barcos colocados por el usuario y las tiradas del ordenador.  
También sale una pequeña ventana donde introducir los datos para colocar cada barco.  
![Imagen inicial del juego de hundir la flota](https://github.com/aiasakitoprof/Proyecto-Battleship/blob/pygame/assets/juego1.jpg)  
Una vez colocados los 5 barcos por sus medidas y colores se inicia la ventana de tiradas del usuario, por cada tirada del usuario
se lanzará una tirada del ordenador.  
![Imagen de barcos colocados e inicio de tirada](https://github.com/aiasakitoprof/Proyecto-Battleship/blob/pygame/assets/juego.jpg)  
El juego acaba cuando uno de los dos jugadores ha destruido todos los barcos del oponente.  
![pop-up de fin de juego](https://github.com/aiasakitoprof/Proyecto-Battleship/blob/pygame/assets/popup.jpg)  
#### Mejoras a realizar
* Se deberían dividir la lógica del juego en archivo diferentes por clases y llamarlas en un archivo inicial de juego  
* Se debe depurar más el código para descartar algunos fallos.  
* Se puede mejorar mucho más el juego, este es un pequeño ejemplo de como realizar un juego de hundir la flota en pygame. 
* Queria añadir un botón de cierre del juego, pero por alguna razón no he conseguido hacerlo funcionar.

#### Errores solucionados
* Posicionamiento de los barcos en el tablero, posicionamiento del tiro y borrado de imagen anterior al cambio hacia acierto o fallo.
* Posicionamiento de la numeración de las coordenadas.
* Cuando el usuario seleccionaba una posición en el tablero y se intentaba a colocar otro barco en la misma posición se superponian.
* Despues de arreglar el error anterior, si se intentaba colocar un barco en la misma posición se volvian a pedir las coordenadas del primer barco, provocando que se añadieran barcos extras.
* Se ha quedado colgado varias veces el código y era por errores de identación o de variables no inicializadas o no accesibles.
