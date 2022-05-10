from colores import*

#------NUMEROS MAGUICOS-------
FILAS=6
COLUMNAS=5
#-----------------------------
def matriz_tablero():
    tablero=[]
    for i in range(FILAS):
        tablero.append([ "?" for l in range(COLUMNAS)])
    return tablero
  
def mostar_tablero(tablero):
    #tablero=matriz_tablero()
    for i in range(FILAS): 
        print(" ".join(tablero[i]))
def ganador_perdedor(ganador):
        if ganador :
            print("ganó el juego")   
        else:
            print("la proxima sera la buena ")
        return ganador # truen o false               
#mostar_tablero()
def bucle_juego(tablero):
    palabra_lista="bardo"
    ganador=False
    contador_credito=0
    while (not ganador) and (contador_credito< 6):
    #----------------------------------pedir datos----------------------------------
    #validacion
            print("Palabra a adivinar: ? ? ? ? ?")
            palabra=input("Arriesgo :")
            while len(palabra)!=5:
            #break  
                    print(f"la palabra debe tener 5 letras y tiene {len(palabra)}")
                    palabra=input("Arriesgo :")   
            # ganador         
            if palabra==palabra_lista:
                tablero[contador_credito]=[obtener_color( x,"Verde" ) for x in palabra]    
                ganador=True # si es igual gana   
            # si esta 
            else:
                #acumulador ver uno por uno 
                lista_2=[]
                for i in range(len(palabra)):
                    if palabra[i] in palabra_lista[i]:
                         lista_2.append(obtener_color( palabra[i],"Verde" ))

                    elif palabra[i] in palabra_lista:
                         lista_2.append( obtener_color( palabra[i],"Amarillo" ))
                    else:
                         lista_2.append( obtener_color( palabra[i],"Rojo" ))    
                tablero[contador_credito]=lista_2   # ACUMULA EN EL TABLERO PRINCIPAL

            # mostar el tablero nuevo del acumulado
            mostar_tablero(tablero) 
            """ for i in range(5): 
                print(" ".join(tablero[i]))   """
    #--------------------------------fin de pedir datos--------------------------    
            contador_credito+=1 # cuenta las veses que intente
    ganador_perdedor(ganador)        
"""     if ganador :
        print("ganó el juego")   
    else:
        print("la proxima sera la buena ")
    return ganador # truen o false """
#1
def main():
    
    tablero=matriz_tablero()
    bucle_juego(tablero)
  
    
main()    
