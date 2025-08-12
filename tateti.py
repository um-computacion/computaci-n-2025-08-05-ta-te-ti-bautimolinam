from tablero import Tablero

class Tateti:
    def __init__(self):
        self.turno = "X"
        self.tablero = Tablero()
        self.juego_terminado = False
        self.ganador = None

    def ocupar_una_de_las_casillas(self, fil, col):
        if self.juego_terminado:
            raise Exception("El juego ya terminó")
        self.tablero.poner_la_ficha(fil, col, self.turno)
        
        if self.tablero.hay_ganador():
            self.juego_terminado = True
            self.ganador = self.turno
        elif self.tablero.tablero_lleno():
            self.juego_terminado = True
            self.ganador = None  
        else:
           
            self.turno = "0" if self.turno == "X" else "X"
