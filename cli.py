from tateti import Tateti

def main():
    print("Bienvenidos al Tateti")
    juego = Tateti()
    while True:
        print("\nTablero:")
        juego.tablero.mostrar()
        print(f"Turno: {juego.turno}")
        try:
            fil = int(input("Ingrese fila (0-2): "))
            col = int(input("Ingrese columna (0-2): "))
            juego.ocupar_una_de_las_casillas(fil, col)
            if juego.juego_terminado:
                print("\nTablero final:")
                juego.tablero.mostrar()
                if juego.ganador:
                    print(f"¡Ganó el jugador {juego.ganador}!")
                else:
                    print("¡Empate!")
                break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()
