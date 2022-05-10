FILAS=6
COLUMNAS=5

def matriz_tablero():
    tablero=[]
    for i in range(FILAS):
        tablero.append([ "?" for l in range(COLUMNAS)])
    return tablero