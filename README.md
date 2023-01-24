# Proyecto-Battleship

## Creacion del documento IDC

Cómo jugar al Battleship (1persona vs IA)

### 1. - Preparación.

1. Cada jugador recibe un tablero
2. Cada jugador en su tablero tiene 5 barcos
3. Cada barco es de distinto tamaño (Acorazado 5, Portaaviones 4, Crucero 3, Submarino 2 y Destructor 2)
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

## Creación del documento CCF(Codificación y creación de funciones)  

El primer paso ha sido crear archivos diferentes con las clases empleadas en el proyecto de juego.  

A continuación hemos definido las variables utilizadas en el código, estas han sido modificadas a lo largo de la ejecución del proyecto así como añadir varibles nuevas.    

A continuación se han ido haciendo funciones en cada clase para ir llamandolas según se han ido necesitando para el desarrollo del juego. También hemos creado una función que nos limpia la pantalla despues de cada jugada.  
Tenemos las siguientes clases, cada una con sus funciones correspondientes:  
### Archivo Jugador.py  
Tablero:  
* init: Función que define el objeto tablero   
* view_tablero: Función que pinta el tablero por pantalla  
* barco_colocado: Función que define el estado del barco  

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
