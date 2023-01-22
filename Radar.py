class Radar: # Definimos la clase radar
    def __init__(self, width=10, height=10): # Definimos el objeto radar
        self.width = width # Se establece el ancho del radar
        self.height = height # Se establece el alto del radar
        self.radar = [["·" for i in range(width)] for i in range(height)] # Creamos el radar con una matriz de  '.' con el ancho y el alto
        self.barcos_ia = [] # Creamos una lista para almacenar los barcos en el radar

    def view_radar(self): # Definimos la funcion que imprimira el radar
        print("  ", end="") # Creamos un espacio separador de coordenadas
        for i in range(self.width): #Se imprimen las coordenadas de las columnas en el radar
            print(i, end=" ")
        print()
        for i, row in enumerate(self.radar):  # Se imprimen las coordenadas de las filas en el radar
            print(i, end=" ")
            print(" ".join(row))  
