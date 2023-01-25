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
**colocar_barco:**  
Función que permite colocar los barcos del usuario según las posiciones de fila y columna definidas por el usuario, el usuario introduce la orientación, v- vertical u h- horizontal y la fila y columna de inicio del barco y la función hace el proceso de colocación y verificación de posiciones.  
**colocar_barcos_ia:**     
La siguiente función permite que el ordenador coloque sus barcos de manera random respetando los limites del tablero y colocando todos los barcos según su longitud de manera vertical u horizontal.  
**disparo_ia:**     
Función que permite que el ordenador realize un disparo según dos modos de tiro, buscar y hundir. En el modo buscar se activa una función que permite crear tiradas random y en el modo hundir se activa otra función que permite refinar el tiro por parte del ordenador.  
**posicion_azar:**      
Función a la que llama la función disparo_ia para crear tiradas random.  
**buscar_alrededor:**      
Función que permite seguir una serie de estrategias de disparo mas eficientes según los aciertos y su número.  
**borrar_posicion:**      
Función que pinta un cuadrado en negro(color pantalla) antes de crear la imagen de acierto o fallo.  
**dibujar_acierto:**     
Función que permite dibujar una X en verde si el tiro ha sido un acierto por parte del ordenador, que se dibujará en el segundo tablero.  
**dibujar_fallo:**      
Función que permite dibujar un circulo en rojo en cada tirada fallida por parte del ordenador.    
**borrar_posicion_ia:**   
Función que pinta un circulo negro (color pantalla) antes de crear un acierto o fallo por parte del usuario.  
**dibujar_acierto_user:**      
Función que permite dibujar una X en verde si el tiro ha sido un acierto por parte del usuario, que se dibujará en el primer tablero.  
**disparo_user:**       
Función que permite realizar un disparo al usuario, abre una ventana de introducción de datos y valida si estos datos no han sido repetidos. Según sea un acierto o un fallo, llama a las funciones correspondientes.  
**turnos:**      
Función que decide cual es el turno de cada usuario y cuando gana uno de los jugadores.    

La funciones llamadas son colocar_barco, colocar_barcos_ia y turnos, estas conectan a todas las demás en el codigo.  

### Lógica de la ia en el juego
___________________________
Cuando es el turno del ordenador se inicia la función disparo_ia().  
Esta tiene dos modos de juego, el modo "buscar" y el modo "hundir"  
En el modo "buscar" se llama a la función posicion_azar() que crea una tirada de fila y columna random entre 0 y 9  
En el modo "hundir" se llama a la función buscar_alrededor(), que se activa cuando ha habido aciertos por parte del ordenador.  
En esta función hay diferentes estrategias de juego, inicialmente se crean las variables fila y columna que contienen los datos de la última tirada válida.  
Teniendo esto en cuenta, en caso de que haya más de un acierto consecutivo, se buscará en que dirección se encuentran los aciertos.  
En caso de que la dirección sea horizontal (coinciden dos aciertos en la misma fila) dirigiremos el disparo a una posición que no se haya tirado anteriormente y se cambiará la posición de la columna, manteniendose en la misma fila.  
En caso de que la dirección sea vertical (coinciden dos aciertos en la misma columna) dirigiremos el disparo a una posición que no se haya tirado anteriormente y se cambiará la posición de la fila, manteniendose en la misma columna.  
La estrategia a seguir en caso de que solo haya un acierto es hacer un tiro aproximado en la misma fila o columna siguiente o anterior, siempre que no se salga del tablero.  
En caso de que el tiro aproximado ya este en la lista de disparos realizados, el disparo se hará en una posición disponible.  
La elección de modos se realiza en la función disparo_ia()  
El primer modo, al iniciar el juego es el de "buscar"; en caso de que haya un acierto en el disparo, cambiaremos al modo "hundir".  
El modo "hundir" pretende acabar con los barcos, así que si obtiene un acierto, seguirá en este modo; en caso de que hunda un barco o el número de tiradas acertadas no sea mayor a 1, volverá al modo "buscar". 

### PCE
#### (Errores en las pruebas unitarias e integradas)  
***Fallo:***  
Posicionamiento de los barcos en el tablero y posicionamiento del tiro.  
***Solución:***  
Tener en cuenta en tamaño de la celda para pintar el cuadrado.  
Variar las posiciones x e y para adaptarlas a la posición del tablero.  

***Fallo:***  
Superposición de imagen al introducir las imagenes de acierto o fallo en el tablero de juego.
***Solución:***  
Creación de un cuadrado en negro con una función que se activa antes del proceso de creación de las imagenes de acierto o fallo.

***Fallo:***  
Posicionamiento de la numeración de las coordenadas.
***Solución:***  
Ir probando de posicionar las numeraciones de filas y columnas variando su posicionamiento x e y.

***Fallo:***  
Superposición de la ventana de pygame con la ventana de pySimpleGUI, provocando que no se vea la ventana para introducir los datos si se cambia la posición de la ventana de pygame.
***Solución:***  
Añadir un parametro de visualización de ventana de pySimpleGUI que siempre quede en la parte superior.

***Fallo:***  
Cuando el usuario seleccionaba una posición en el tablero y se intentaba a colocar otro barco en la misma posición se superponen.
***Solución:***  
Crear una validación de coordenadas ya colocadas y compararlas con las que se quieren introducir.

***Fallo:***  
Visualización de la ventana de PySimpleGUI varias veces.
***Solución:***  
Cambiar la identación de los bucles y cierre correctos de los mismos.

***Fallo:***  
si se intenta colocar un barco en la misma posición se vuelven a pedir las coordenadas del primer barco, provocando que se añadan barcos extras.
***Solución:***   
Creación de un nuevo diccionario que incluya los indices de cada barco y un contador de barcos ya colocados y creando una condicion que valide que el barco a colocar coincide con el contador para seguir el proceso de colocación de barcos.

***Fallo:***  
Fallo general del juego, cierre automático.
***Solución:***   
Verificar la terminal para encontrar los errores indicados y arreglar dichos errores. Muchos de estos errores se debian a variables no inicializadas correctamente, listas que se vaciaban al volver a definirlas dentro del código o variables no introducidas en los parametros de la función.


#### Mejoras a realizar
* Se deberían dividir la lógica del juego en archivo diferentes por clases y llamarlas en un archivo inicial de juego  
* Se debe depurar más el código para descartar algunos fallos.  
* Queria añadir un botón de cierre del juego, pero por alguna razón no he conseguido hacerlo funcionar. El problema actual es que si intentas cerrar el juego mediante el botón de cierre de ventana, no se cierra hasta que acaba de ejecutar todos los procesos del juego.
* Se puede mejorar mucho más el juego, este es un pequeño ejemplo de como realizar un juego de hundir la flota en pygame. 


#### Algunos enlaces de interes para poder ejecutar el juego
Instalación de pygame  
https://aprendewindows.org/como-instalar-pygame-en-windows-10/  
Uso e instalacion de pySimpleGUI  
https://decodigo.com/crear-una-interfaz-con-pysimplegui
