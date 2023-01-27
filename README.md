# Proyecto-Battleship

## Creacion del documento IDC

Cómo jugar al Battleship (1persona vs IA)

### 1. - Preparación.

1. Cada jugador recibe un tablero
2. Cada jugador en su tablero tiene 5 barcos
3. Cada barco es de distinto tamaño (Acorazado 5, Portaaviones 4, Crucero 3, Submarino 3 y Destructor 2)
4. Cada jugador en su turno tiene una oportunidad de disparo


### 2. - Jugar turnos.

1. Se empieza con el turno del usuario
2. El usuario lanza su disparo introcuciendo las coordenadas de la fila primero seguida de la de la columna ejem. '00'
3. Si no da al objetivo saldra una 'O'
4. Si alzanza uno de los barcos Saldra marcado con una 'X'
5. A continuacion sera el turno de la IA

### 3. - Finalizar partida

1. La partida finaliza cuando uno de los dos jugadores hunde todos los barcos del oponente
2. La partida finalizara enseñando por pantalla si has ganado o has perdido

### 4. - Reglas del turno

1. Cada jugador solo dispondra de un disparo por turno

## Creación del documento TEP

### Preparación

* Creamos un tablero para el jugador con arrays

* Creamos los barcos

* Añadimos los barcos al tablero

* Creamos otro tablero para la IA con arrays

* Añadimos los barcos en el tablero de la IA

* Creamos un random para colocar los barcos

* Creamos listas para guardar los barcos en los tableros

### Jugar turnos

* Se crea un bucle para gestionar los turnos mientras queden barcos por hundir

* Si el turno es del usuario, debera introducir las coordenadas

* Si el turno es de la IA con un random escogera sus coordenadas

### Interacción del jugador

* Se mostrará por pantalla un menú en el que el jugador podra escoger si quiere una partida rapida o normal

* Si escoge partida rapida los barcos se colocaran con un random aleatoriamente en su tablero y en el de la IA

* Se le pedira al jugador que escoja unas coordenadas para disparar (fila, columna)

* Se mostrara si el usuario ha acertado a uno de los barcos 'X' o no 'O'

* Se mostrara si el jugador ha ganado la partida o ha perdido

* Si escoge partida normal

* El usuario debera colocaro los barcos asignando sus coordenadas de donde sera la punta del barco usando un bucle

* Tambien debera asignarle si lo quiere colocar en vertical o horizontal usando un buble

* Asi hasta el total de 5 barcos

* Seguidamente se le pedira al usuario que escoja unas coordenadas para disparar (fila, columna)

* Se mostrara si el usuario ha acertado a uno de los barcos 'X' o no 'O'

* Se mostrara si el jugador ha ganado la partida o  ha perdido

### Interacción de la IA

* En los dos modos de juego se asignaran con un random los barcos a la IA

* En cada turno de la IA en su tablero aparecera si ha acertado con una 'X' o si ha fallado con 'O'

* Cada turno de la IA sera con un random

* Se hara un bucle para que si acierta se le sume o se le reste cerca de la posicion, asi haremos que la IA sea mas inteligente y descubra un barco entero en menos disparos

### Terminar Partida

* Cuando el bucle principal a medida que le vamos restando las posciones donde se encuentra cada uno de los barcos hasta llegar a 0.

* Si el jugador llega antes a 0 ganará el jugador

* En el caso contrario ganará la IA

* No puede haber empate

* Al finalizar saldra el mensaje de si el jugador ha ganado o ha perdido

## Creación del documento CCF  
### (Codificación y creación de funciones)  

El primer paso ha sido crear archivos diferentes con las clases empleadas en el proyecto de juego.  

A continuación hemos definido las variables utilizadas en el código, estas han sido modificadas a lo largo de la ejecución del proyecto así como añadir varibles nuevas.  
Hemos empleado las librerias "random" para la creación de las posiciones del los barcos por parte del ordenador y sus tiradas, y la libreria "colorama" para introducir algunos colores y hacer el juego mas vistoso.  
También se han empleado la libreria "os" que permite introducir funcionalidades que dependen del sistema operativo y la libreria "platform" que permite verificar la identidad del sistema operativo.    

A continuación se han ido haciendo funciones en cada clase para ir llamandolas según se han ido necesitando para el desarrollo del juego. También hemos creado una función que nos limpia la pantalla despues de cada jugada.  
Tenemos las siguientes clases, cada una con sus funciones correspondientes:  
### Archivo Jugador.py  
Tablero:  
* init: Función que define el objeto tablero   
* view_tablero: Función que pinta el tablero por pantalla  
* barco_colocado: Función que guarda en un diccionario el estado del barco  

Barcos:  
* init : Función que llama al objeto Tablero  
* colocar_barcos: Función que nos permite colocar todos los barcos del usuario  

### Archivo AI.py  
Radar:  
* init : Función que define el objeto Radar, basicamente es el tablero donde el jugador lanzará sus ataques hacia el ordenador  
* view_radar: Función que pinta por pantalla el tablero con las actualizaciones de los ataques  
Barcos_ia:  
* init: Función que define el objeto, indica los barcos que dispone y sus longitudes en un diccionario    
* colocar_barcos_ia: Función que coloca los barcos del ordenador de manera aleatoria  

### Archivo Jugador_rapido.py  
Barcos_rapidos:  
* init: Define el objeto y sus caracteristicas  
* colocar_barcos_rapidos: Permite colocar los barcos del usuario aleatoriamente  

### Archivo Battleship.py  
Este archivo es el que permite iniciar el juego, importa las clases para poder emplearlas  
Juego:  
* init: Función que define el objeto Juego e inicializa las funciones de cada clase  
* realizar_disparo: En esta función se recogen los valores del tiro del usuario y se validan  * disparo_ia: En esta función se realiza el disparo del ordenador, comprobando que no ha sido realizado anteriormente  
* print_ambos_tableros: Esta función pinta por pantalla los tableros del ordenador y del usuario con sus barcos  
* jugar: Permite inicializar el juego permitiendo que juegue el usuario y el ordenador en un turno cada vez, también actualiza el tablero con las jugadas realizadas.  

### Archivo Menu_y_extras.py  
* Instrucciones: Informa al usuario de las instrucciones para jugar y la descripción del juego  
* menu: Nos permite seleccionar las opciones del menú  

## Creación del documento PCE
### (Errores en las pruebas unitarias e integradas)

El 90% de los fallos derivan del input del usuario. Estos se pueden solucionar mediante control de errores. Un ejemplo práctico:
Pedimos al usuario unas coordenadas para disparar en el formato '00'. El usuario por error o de forma intencional podría introducir '0', '123'
'p4', '1021', 'qw', etc. Todo esto provocaría un fallo fatal en el programa, para ello se introduce lo siguiente:

        while disparo in self.disparos_realizados_jg:
                    coord = input("Selecciona coordenadas de disparo no repetidas:\n >  ")
                    while True:
                        if len(coord) == 2:
                            if coord[0] in ["0","1","2","3","4","5","6","7","8","9"]:
                                if coord[1] in ["0","1","2","3","4","5","6","7","8","9"]:
                                    break

Esto se traduce en, mientras el disparo sea repetido, pido coordenadas, si estas no son de longitud dos, y sus dos componentes no están entre 0 y 9 (estos incluidos), y además son repetidas, no aceptará el imput como válido. De esta forma evitamos la introducción de letras o signos que no se pueden traducir a número (int), coordenadsa fuera del tablero o de longitud diferente a 2.

Otro ejemplo es el siguiente, con el que se evita que el usuario introduzca valores fuera de aquellos que queremos.

        while orientacion not in ["v","h"]:  # Control de errores.
            orientacion = input()  
            
# Proyecto en Pygame 
______________________
### Objetivos y descripción  
____________________________
Esta parte del proyecto es una mejora del juego en terminal, tiene las mismas reglas y formatos de juego. No está del todo acabado y depurado, por lo que se ha quedado en un ejemplo de como se podría ir mejorando las funcionalidades del juego teniendo la base de la lógica empleada.
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
Imagen final del juego, con el mensaje de Game Over    
![Game over](https://github.com/aiasakitoprof/Proyecto-Battleship/blob/pygame/assets/end_game.jpg)     

Para instalar Pygame en Windows, MacOS o Linux, abra la terminal y escriba el siguiente comando:  
pip install pygame  
Para instalar PySimpleGUI, escriba el siguiente comando en la terminal:  
pip install pysimplegui  
Una vez que se completen las instalaciones, podrá ejecutar el programa.

### CCF
#### (Codificación y creación de funciones)
___________________________________________

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
______________________________________________________  
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

***Fallo:***    
Colocación de los barcos. Por la manera que tenia programado el código, nunca llegaban al borde del tablero.

***Solución:***    
Comprobar los cálculos que se hacian y cambiar las cantidades para adaptarlas al tablero.  
```
    if orientation == "h" and col + longitud >=11:  
                sg.popup("El barco se sale del tablero.", keep_on_top=True)  
                # El barco sale del tablero en fila  
                return colocar_barco(barcos, screen, cell_size, ANCHO, ALTO, coordenadas, coordenadas_str, barco_actual)  

            elif orientation == "v" and  row + longitud >=11:  
                sg.popup("El barco se sale del tablero.", keep_on_top=True)  
                # El barco sale del tablero en columna  
                return colocar_barco(barcos, screen, cell_size, ANCHO, ALTO, coordenadas, coordenadas_str, barco_actual)  
```
***Fallo:***    
Fallo al introducir imagenes en el ejecutable.  
***Solución:***      
Añadir una función que acceda a la ruta de la imagen y cargar la imagen con esta función.  
def resolver_ruta(ruta_relativa):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath('.'), ruta_relativa)
imagen=pygame.image.load(resolver_ruta("game_over.png"))
                
#### Enlace de descarga del archivo ejecutable .exe: Solo disponibles para miembros del IES Borja Moll  
https://drive.google.com/file/d/1WBrOjEsybVub6lPoHw-cWwwH-X1sFvWG/view?usp=share_link  
```diff
- Es muy posible que al realizar la descarga, google la bloquee por ser un ejecutable.  
- Se debe acceder al menú de descargas de google y aceptar la descarga desde allí.  
- Una vez descargado, a veces el sistema de seguridad del ordenador también lo bloquea,  
- también se debe desbloquear para poderlo ejecutar.  
- NO ES UN VIRUS!!!
```

### Mejoras posibles
________________________
* Se deberían dividir la lógica del juego en archivo diferentes por clases y llamarlas en un archivo inicial de juego. 
* Se podría crear una pantalla inicial del juego con la explicación de las reglas y sus carácteristicas.
* Para hacerlo más fluido se podría hacer uso de las pulsaciones del ratón para ir colocando los barcos y hacer los ataques.
* Se debe depurar más el código para descartar algunos fallos.  
* Queria añadir un botón de cierre del juego, pero por alguna razón no he conseguido hacerlo funcionar. El problema actual es que si intentas cerrar el juego mediante el botón de cierre de ventana, no se cierra hasta que acaba de ejecutar todos los procesos del juego.
* Se puede mejorar mucho más el juego, este es un pequeño ejemplo de como realizar un juego de hundir la flota en pygame. 

### Intentos de mejora fallidos
________________________
* He intentado crear un botón de cierre, por si se quiere cerrar el juego antes de terminar y he averiguado que pySimpleGUI bloquea el uso de la pantalla de pygame cuando su ventana está activa.
* Otra cosa que he intentado es crear un botón con pygame, pero por la programación de esta libreria, no me permitia cerrar el juego.
Capturas de los fallos que me daba pygame por el conflicto con pySimpleGUI
![Imagen de error de pygame1](https://github.com/aiasakitoprof/Proyecto-Battleship/blob/pygame/assets/errorPygame.jpg)  
![Imagen de error de pygame2](https://github.com/aiasakitoprof/Proyecto-Battleship/blob/pygame/assets/errorPygame2.jpg)  


### Algunos enlaces de interes para poder ejecutar el juego
Instalación de pygame  
https://aprendewindows.org/como-instalar-pygame-en-windows-10/  
Uso e instalacion de pySimpleGUI  
https://decodigo.com/crear-una-interfaz-con-pysimplegui

## Webgrafía
* Colores rgb   
https://www.calculadoraconversor.com/colores-rgb   

* Ejemplos de juegos similares   
https://www.pygame.org/tags/ship  

* Ejemplo juego battleship   
https://framagit.org/bailandoconbuitres/pybattleship-classic/-/tree/master  

* Fuentes en windows 10   
https://learn.microsoft.com/en-us/typography/fonts/windows_10_font_list

* Pygame 
https://github.com/josecodetech/Pygame

* Sonidos  
https://freesound.org/people/bareform/sounds/218721/

* 6 videos de juego battleships  
https://www.youtube.com/watch?v=GmWHhAGvaQA&list=PLpeS0xTwoWAsn3SwQbSsOZ26pqZ-0CG6i&index=6

* visual studio code y github<br>
https://www.youtube.com/watch?v=qdec2M4NwT0  
http://programarcadegames.com/index.php?lang=es&chapter=labs  
https://github.com/GrizzlyH/Battleship_Walkthrough

* Colorama  
https://recursospython.com/guias-y-manuales/colorama-texto-fondo-coloreados-la-consola/

* Tabulate
https://python-para-impacientes.blogspot.com/2017/01/tablas-con-estilo-con-tabulate.html

* W3chools
https://www.w3schools.com/python/default.asp

* Chat-GPT (Solución de errores y aprendizaje de programación orientada a objetos)<br>
https://chat.openai.com/chat  
https://openai.com/blog/chatgpt/qwe.sh/%2F../

* Python-tutor
https://pythontutor.com/visualize.html#mode=edit

* Curso de desarrollo de juego con pygame  
https://www.udemy.com/course/crea-tu-propio-juego-con-python/

* Convertir archivos python en un ejecutable .exe  
https://www.youtube.com/watch?v=FFE1VNMAZfc

* Incluir imagenes en el ejecutable  
https://www.youtube.com/watch?v=diZ4a4pTtUU  

* Programar Juegos Arcade con Python y Pygame  
http://programarcadegames.com/index.php?lang=es&chapter=array_backed_grids
