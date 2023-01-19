from Barcos import *
from Computer import *
import random


# total_coordenadas=[] #Guardo las coordenadas para saber si gana el usuario cuando el array esté vacio
# total_coordenadas_Usuario=[] # Guardo las coordenadas del usuario para saber si gana el ordenador
#Diccionarios para saber las caracteristicas de cada navio, es necesario para ir pintando las posiciones
# que van quedando durante el juego
acierto=[]
perdido=[]
acierto_computer=[]
perdido_computer=[]

# Array para saber las posiciones ocupadas, está creado pero aun no lo empleo, si no es necesario, se puede borrar 
#posiciones_ocupadas=[]

class Juego:
    # Función para obtener los disparos del usuario
    def obtener_disparo(disparos_user):
        ok = False
        # Mientras ok sea Falso, o sea que mientras no se hayan introducido unas coordenadas válidas 
        # no se guardará el tiro
        while ok == False:
            try:
                fila = input("Introduzca una fila de tiro: ")
                columna = input("Introduzca una columna de tiro: ")
                #Necesito pasarlo a entero para verificar si es una coordenada válida
                disparo = int(fila+columna)
                if disparo < 0 or disparo > 99:
                    print("Número incorrecto, intente de nuevo")
                else:
                    # En caso de que sea valido lo paso a string para poder concatenarlos
                    disparo=str(fila+columna)
                    #Si el disparo está en el array quiere decir que está repetido
                    if  disparo in disparos_user:
                        print("Número repetido, intente de nuevo")
                    else:
                        ok=True
            except:
                print("Entrada incorrecta - por favor, intentelo de nuevo")
        #Guardo los disparos correctos en el array
        disparos_user.append(disparo)
        return disparo
    # La siguiente funcion me crea un disparo del ordenador teniendo en cuenta
    # los aciertos y los disparos ya realizados
    def obtener_disparo_computer(acierto_computer, disparos_computer):

        disparo=0
        intento=False
        diferente=True
        # Mientras el disparo se considere diferente del disparo guardado en el array
        # El bucle seguirá activo
        while diferente==True:
            fila = random.randint(0,9)
            columna = random.randint(0,9)
            # En caso de que haya datos en el array de aciertos se seguiran las siguientes
            # tácticas de tiro
            if len(acierto_computer)>0:  
                # De los aciertos del computador cogemos del último tiro el número que corresponde
                # a la fila. ej. "16", posición "0"="1" es fila, posición "1"="6" es columna          
                filaMenos=int(acierto_computer[-1][0])-1
                filaMas=int(acierto_computer[-1][0])+1
                columnaMenos=int(acierto_computer[-1][1])-1
                columnaMas=int(acierto_computer[-1][1])+1
                # Mientras el intento de tiro sea falso, el bucle sigue activo.
                # El bucle acaba cuando consigue un disparo válido
                while intento==False:
                    arriba_abajo=random.choice([fila,columna])
                    if arriba_abajo==fila:
                        fila=random.choice([filaMenos,filaMas])
                        columna=int(acierto_computer[-1][1])
                        if filaMenos<0:
                            fila=filaMas
                        elif filaMas>9:
                            fila=filaMenos
                    if arriba_abajo==columna:
                        fila=int(acierto_computer[-1][0])
                        columna=random.choice([columnaMenos,columnaMas])
                        if columnaMenos<0:
                            columna=columnaMas
                        elif columnaMas>9:
                            columna=columnaMenos
                    disparo = str(fila)+str(columna)
                    intento=True
            else:
                disparo = str(fila)+str(columna)
            # Esta condición me comprueba si el disparo es diferente a los que están 
            # guardados en el array de disparos_computer
            if len(disparos_computer)>0:
                if disparo in disparos_computer:
                    diferente=True
                else:
                    #Si no está en el array, me lo guarda y retorna el disparo
                    disparos_computer.append(disparo)
                    diferente=False
                    return disparo
            else:
                #Si no hay datos en el array, me lo guarda y retorna el disparo
                disparos_computer.append(disparo)
                diferente=False
                return disparo

    def comprobar_disparo(disparo): #Comprobamos si el disparo ha tocado una de las posiciones de barco
        # Si el disparo coincide con un elemento del array del computador, es que habrá acertado
        if disparo in total_coordenadas:
            # Guardamos el disparo en el array de aciertos
            acierto.append(disparo)
            # Borramos la coordenada del disparo del array de coordenadas del ordenador
            total_coordenadas.remove(disparo)
        else:
            # En caso de fallo guardamos el disparo en el array de fallos
            perdido.append(disparo)

        return acierto, perdido
    # En esta función comprobamos el disparo del computador
    def comprobar_disparo_computer(disparo):
        # Si el disparo coincide con un elemento del array de coordenadas del usuario
        if disparo in total_coordenadas_Usuario:
            # Guardamos el acierto en el array de aciertos del computador
            acierto_computer.append(disparo)
            # Eliminamos la coordenada del array de coordenadas del usuario
            total_coordenadas_Usuario.remove(disparo)
        else:
            # Si falla guardamos el disparo en el array de disparos perdidos
            perdido_computer.append(disparo)

        return acierto_computer, perdido_computer
    # Comprobación de que se ha hundido un navio
    def comprobar_barco_completo(aciertos,acorazado,crucero,submarino):
        # Cada contador guardará el número de aciertos de cada navio y lo 
        # comparará con la longitud del navio correspondiente
        contadorA=0
        contadorC=0
        contadorS=0
        for aciertos in acierto:
            if aciertos in acorazado["coordenadas"]:
                contadorA+=1
                if len(acorazado["coordenadas"]) == contadorA:
                    print("Has acabado con el acorazado!!")
            elif aciertos in crucero["coordenadas"]:
                contadorC+=1
                if len(acorazado["coordenadas"]) == contadorC:
                    print("Has acabado con el crucero!!")
            elif aciertos in submarino:
                contadorS+=1
                if len(submarino["coordenandas"])==contadorS:
                    print("Has acabado con el submarino")
    # Esta función comprueba quien ha ganado el juego
    def quien_gana():
        if len(total_coordenadas)<=0:
            print("Has ganado, enhorabuena")
            gana=True
        elif len(total_coordenadas_Usuario)<=0:
            print("Ha ganado el Ordenador")
            gana=True
        else:
            gana=False
        return gana