class Radar:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.radar = [["·" for i in range(width)] for i in range(height)]
        self.coordenadas_barcos_ia = []

    def view_radar(self):
        print("  ", end="")
        for i in range(self.width):
            print(i, end=" ")
        print()
        for i, row in enumerate(self.radar):
            print(i, end=" ")
            print(" ".join(row))
