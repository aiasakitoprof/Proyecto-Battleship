# Proyecto-Battleship

## Creación del documento IDC

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

Creamos un tablero para el jugador con arrays

Creamos los barcos

Añadimos los barcos al tablero

Creamos otro tablero para la IA con arrays

Añadimos los barcos en el tablero de la IA

Creamos un random para colocar los barcos

Creamos listas para guardar los barcos en los tableros

### Jugar turnos

Se crea un bucle para gestionar los turnos mientras queden barcos por hundir

Si el turno es del usuario, debera introducir las coordenadas

Si el turno es de la IA con un random escogera sus coordenadas

### Interacción del jugador

Se mostrará por pantalla un menú en el que el jugador podra escoger si quiere una partida rapida o normal

Si escoge partida rapida los barcos se colocaran con un random aleatoriamente en su tablero y en el de la IA


