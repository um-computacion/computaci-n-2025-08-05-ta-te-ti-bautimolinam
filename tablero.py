class PosOcupadaException(Exception):
    pass

class Tablero:
    def __init__(self):
        self.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]

    def poner_la_ficha(self, fil, col, ficha):
        if self.contenedor[fil][col] == "":
            self.contenedor[fil][col] = ficha
        else:
            raise PosOcupadaException("Posición ocupada!")

    def hay_ganador(self):
        
        for fila in self.contenedor:
            if fila[0] != "" and fila[0] == fila[1] == fila[2]:
                return True
       
        for col in range(3):
            if self.contenedor[0][col] != "" and self.contenedor[0][col] == self.contenedor[1][col] == self.contenedor[2][col]:
                return True
        
        if self.contenedor[0][0] != "" and self.contenedor[0][0] == self.contenedor[1][1] == self.contenedor[2][2]:
            return True
        if self.contenedor[0][2] != "" and self.contenedor[0][2] == self.contenedor[1][1] == self.contenedor[2][0]:
            return True
        return False

    def tablero_lleno(self):
        for fila in self.contenedor:
            for casilla in fila:
                if casilla == "":
                    return False
        return True

    def mostrar(self):
        for i, fila in enumerate(self.contenedor):
            print(" | ".join(casilla if casilla != "" else " " for casilla in fila))
            if i < 2:
                print("-" * 9)
