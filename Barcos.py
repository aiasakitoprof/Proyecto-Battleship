from Tablero_user import *
class Barcos:
    # La siguiente clase inicia los barcos del usuario
    def __init__(self, board): # Llamada al objeto tablero.

        self.board = board # Importa el tablero
        self.barcos = {"1": 4, "2": 3, "3": 2,} # Diccionario con los barcos y sus longitudes.

    def colocar_barcos(self):
        coordenadas=[]
        seleccion=["1","2","3"]

        while len(self.board.barcos_colocados) < len(self.barcos):# Premisa, si no están todos los barcos colocados seguimos ejecutando.
            siSeleccion=False
            # Bucle para asegurarse de que el usuario elige en navio correcto - Control de errores
            while siSeleccion==False:
                barco_elegido = input("Elige el barco a colocar (1=acorazado, 2=crucero, 3=submarino): ")# Selector de barcos.
                if barco_elegido not in seleccion:
                    print("Selección invalida, intente de nuevo")
                    siSeleccion=False
                else:
                    siSeleccion=True

            longitud = self.barcos[barco_elegido] # Extraemos su longitud

            if barco_elegido in self.board.barcos_colocados: # Comprobamos que no esté ya colocado.
                print(f"El barco {barco_elegido} ya esta colocado.") # <== Si lo está.
                continue
            barco_colocado = False

            longitud = self.barcos[barco_elegido] # Extraemos su longitud

            if barco_elegido in self.board.barcos_colocados: # Comprobamos que no esté ya colocado.
                print(f"El barco {barco_elegido} ya esta colocado.") # <== Si lo está.
                continue
            barco_colocado = False
            #Condiciones que me permiten guardar los datos de cada navio en el diccionario
            if barco_elegido == "1":
                acorazado_user["id"]="1"
                acorazado_user["L"]=longitud
            elif barco_elegido == "2":
                crucero_user["id"]="2"
                crucero_user["L"]=longitud
            elif barco_elegido=="3":
                submarino_user["id"]="3"
                submarino_user["L"]=longitud

            orientaciones=["v","h"]
            while barco_colocado == False: # Si no está colocado.
                orientacion = input("Orientación (v/h): ")# Atributos del barco.
                # Control de errores en la seleccion de orientacion
                if orientacion not in orientaciones:
                    print("Orientación invalida, introduzca v o h. vertical/horizontal")
                    barco_colocado=False
                else:
                    colocadoF=False
                    # Buche de control de errores en la seleccion de coordenadas.
                    while colocadoF == False:
                        try:
                            fila = int(input("Fila colocación: "))
                            if fila <0 or fila>9:
                                print("Debe introducir un valor entre 0 y 9")
                                colocadoF=False
                            else:
                                colocadoF=True
                        except ValueError:
                            print("Debe introducir un valor entre 0 y 9. Has introducido una letra.")
                            colocadoF=False
                        colocadoC=False
                    while colocadoC == False:
                        try:
                            columna = int(input("Columna Colocación: "))
                            if columna <0 or columna>9:
                                print("Debe introducir un valor entre 0 y 9")
                                colocadoC=False
                            else:
                                colocadoC=True
                        except ValueError:
                            print("Debe introducir un valor entre 0 y 9. Has introducido una letra")
                            colocadoC=False

                # Antes de pasar a poner los barcos en el tablero comprobamos que se puedan colocar en la posición especificada.
                if orientacion == "h": # Si queremos poner el barco en hoizontal.
                    #He cambiado la condicion de la longitud porque así queda más claro
                    #He hecho comprobaciones y la suma de columna o fila más longitud no debe sobrepasar 10
                    if columna + longitud > 10:
                        print("Barco fuera del tablero.")
                        barco_colocado = False
                    else:
                        barco_colocado = True    # Comprobamos que el barco no sobresalga del tablero. Premisa: Si sumamos la longitud del
                        # barco al numero de la columna y supera la longitud de la fila, está fuera del tablero
                        # Al ser un cuadrado no importa la fila con la que se realice la comprobación.
                elif orientacion == "v":                              # Realizamos la misma operación si queremos que el barco esté en vertical.
                    if fila + longitud > 10:
                        print("Barco fuera del tablero.")
                        barco_colocado = False 
                    else:
                        barco_colocado = True        # Premisa: Si sumamos la longitud del barco al número de la fila y el resultado
                        # es mayor que la longitud del tablero (Si su índice es mayor que el del tablero),
                        # está fuera del tablero.

                # Procedemos a colocar los barcos.
                posicion_ocupada = False
                bucle_activo = True
                #Aquí guardamos la orientación elegida de cada navio en el diccionario
                if barco_elegido == "1":
                    acorazado_user["orienta"]=orientacion
                elif barco_elegido == "2":
                    crucero_user["orienta"]=orientacion
                elif barco_elegido=="3":
                    submarino_user["orienta"]=orientacion

            while bucle_activo:
                    if orientacion == "h": # Si la orientación es horizontal.
                        for i in range(longitud): # Rango = longitud del barco.
                            if self.board.board[fila][columna + i] != ".": # Si la posición de inicio del barco es diferente al agua.
                                print("Posición ocupada.")
                                posicion_ocupada = True
                                bucle_activo = False

                    elif orientacion == "v":  # Si la orientación es vertical.
                        for i in range(longitud): # Rango = longitud del barco.
                            if self.board.board[fila + i][columna] != ".":  # Si la posición de inicio del barco es diferente al agua.
                                print("Posición ocupada.")
                                posicion_ocupada = True
                                bucle_activo = False

                                coordenadas=[]

                    if not posicion_ocupada: # Si la posición no está ocupada.

                        if orientacion == "h": # Orientación horizontal.
                            for i in range(longitud): # Rango = longitud del barco.
                                self.board.board[fila][columna + i] = barco_elegido[0] # Sustituimos el agua de las coordenadas por el barco.
                                #Aquí guardamos las coordenadas de cada navio
                                #Las paso a string para poder concatenar valores
                                coordenadas.append(str(fila)+str(columna+i))
                                total_coordenadas_Usuario.append(str(fila)+str(columna+i))
                                if barco_elegido == "1":
                                    acorazado_user["coordenadas"]=coordenadas
                                elif barco_elegido == "2":
                                    crucero_user["coordenadas"]=coordenadas
                                elif barco_elegido == "3":
                                    submarino_user["coordenadas"]=coordenadas

                            barco_colocado = True
                            coordenadas=[]
                            self.board.barco_colocado(barco_elegido) # Guardamos el arco para que no se pueda colocar de nuevo.
                            print(f"Barco {barco_elegido} colocado en posición {fila}, {columna} con orientación horizontal.")

                        elif orientacion == "v": # Orientación Vertical.
                            for i in range(longitud): # Rango = longitud del barco.
                                self.board.board[fila + i][columna] = barco_elegido[0] # Sustituimos el agua de las coordenadas por el barco.
                                #Aquí guardamos las coordenadas de cada navio
                                #Las paso a string para poder concatenar valores
                                coordenadas.append(str(fila+i)+str(columna))
                                total_coordenadas_Usuario.append(str(fila+i)+str(columna))
                                if barco_elegido == "1":
                                    acorazado_user["coordenadas"]=coordenadas
                                elif barco_elegido == "2":
                                    crucero_user["coordenadas"]=coordenadas
                                elif barco_elegido == "3":
                                    submarino_user["coordenadas"]=coordenadas
                            
                            barco_colocado = True
                            coordenadas=[]
                            self.board.barco_colocado(barco_elegido) # Guardamos el arco para que no se pueda colocar de nuevo.
                            print(f"Barco {barco_elegido} colocado en posición {fila}, {columna} con orientación vertical.")
            #Muestro las coordenadas del usuario, solo para pruebas
            #print("User",total_coordenadas_Usuario)
            self.board.view_board()