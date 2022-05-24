from matiz_tablero import*
def mostar_tablero(tablero):
    #tablero=matriz_tablero()
    for i in range(FILAS): 
        print(" ".join(tablero[i]))