## Proyecto en Pygame  
### Objetivos y descripción  
El objetivo de esta parte del proyecto ha sido la creación del mismo juego de hundir la flota por terminal en formato Pygame, una libreria que permite crear juegos e incluir entorno gráfico en la programación con python.  
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

### CCF
#### (Codificación y creación de funciones)
El código se ha realizado en un sólo archivo, se han habilitado las librerias principales a utilizar, pygame, PySimpleGUI y random.  
A continuación se han creado las variables principales necesarias, listas y disccionarios que se han ido modificando y añadiendo a lo largo del proceso de creación.
Con pygame se ha hecho una primera prueba básica de crear una pantalla visual con las medidas adecuadas para una pantalla de portatil de 15,6" y a continuación se ha procedido a crear los tableros de juego con la codificación de pygame, esto ha sido un proceso algo complicado, ya que se han tenido que hacer varias pruebas de visualización por pantalla.  
Seguidamente se ha procedido a crear la codificación para la numeración de filas y columnas y la parte donde debe introducir los datos el usuario, con una ventana de pySimpleGUI.  
En el proceso de creación de funciones se han empleado algunas de las funciones creadas para el juego en terminal y se han añadido de nuevas para adaptar el juego al formato de pygame.  
##### Descripción de funciones
* colocar_barco: Función que permite colocar los barcos del usuario según las posiciones de fila y columna definidas por el usuario, el usuario introduce la orientación, v- vertical u h- horizontal y la fila y columna de inicio del barco y la función hace el proceso de colocación y verificación de posiciones.
* colocar_barcos_ia: La siguiente función permite que el ordenador coloque sus barcos de manera random respetando los limites del tablero y colocando todos los barcos según su longitud de manera vertical u horizontal.
* disparo_ia: Función que permite que el ordenador realize un disparo según dos modos de tiro, buscar y hundir. En el modo buscar se activa una función que permite crear tiradas random y en el modo hundir se activa otra función que permite refinar el tiro por parte del ordenador.
* posicion_azar: Función a la que llama la función disparo_ia para crear tiradas random.
* buscar_alrededor: Función que permite seguir una serie de estrategias de disparo mas eficientes según los aciertos y su número.
* borrar_posicion: Función que pinta un cuadrado en negro(color pantalla) antes de crear la imagen de acierto o fallo.
* dibujar_acierto: Función que permite dibujar una X en verde si el tiro ha sido un acierto por parte del ordenador, que se dibujará en el segundo tablero
* dibujar_fallo: Función que permite dibujar un circulo en rojo en cada tirada fallida por parte del ordenador.  
* borrar_posicion_ia: Función que pinta un circulo negro (color pantalla) antes de crear un acierto o fallo por parte del usuario.
* dibujar_acierto_user: Función que permite dibujar una X en verde si el tiro ha sido un acierto por parte del usuario, que se dibujará en el primer tablero.
* disparo_user: Función que permite realizar un disparo al usuario, abre una ventana de introducción de datos y valida si estos datos no han sido repetidos. Según sea un acierto o un fallo, llama a las funciones correspondientes.
* turnos: Función que decide cual es el turno de cada usuario y cuando gana uno de los jugadores.  

La funciones llamadas son colocar_barco, colocar_barcos_ia y turnos, estas conectan a todas las demás en el codigo.

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

#### Algunos enlaces de interes para poder ejecutar el juego
Instalación de pygame  
https://aprendewindows.org/como-instalar-pygame-en-windows-10/  
Uso e instalacion de pySimpleGUI  
https://decodigo.com/crear-una-interfaz-con-pysimplegui
