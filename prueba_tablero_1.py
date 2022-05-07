#------NUMEROS MAGUICOS-------
FILAS=5
COLUMNAS=5
#-----------------------------
def matriz_tablero():
    tablero=[]
    for i in range(FILAS):
        tablero.append([ "?" for l in range(COLUMNAS)])
    return tablero
  
def mostar_tablero():
    tablero=matriz_tablero()
    for i in range(FILAS): 
        print(" ".join(tablero[i]))
mostar_tablero()        
    
