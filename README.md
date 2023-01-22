# Proyecto-Battleship
Lógica de la ia en el juego
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
El modo "hundir" pretende acabar con los barcos, así que si al obtener un acierto, seguirá en este modo; en caso de que hunda un barco o el número de tiradas acertadas no sea mayor a 0, volverá al modo "buscar".  
