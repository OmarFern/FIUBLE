from colores import* #importo carpeta colores.py y con * comodin puedo usar todas la funciones 

""" colores = {"Verde" : "\x1b[32m",
            "Amarillo" : "\x1b[33m",
            "GrisOscuro" : "\x1b[90m",
             "Defecto" : "\x1b[39m" ,
             "Rojo" : "\x1b[31m",
             "END": "\x1b[0m"
              }


def obtener_color(letra,color):
    return colores[color] + letra + colores["END"]
 """

#iniciar ale tablero
ganador=False
palabra_lista="bardo"
tablero=[]
for i in range(5):
    tablero.append([ "?" for l in range(5)])
#print(tablero) 
contador_credito=0
# bucle
while (not ganador) and (contador_credito< 6):
#----------------------------------pedir datos----------------------------------
#validacion
        palabra=input("ingrese una palabra a buscar :")
        while len(palabra)!=5:
        #break
                print(f"la palabra debe tener 5 letras y tiene {len(palabra)}")
                palabra=input("ingrese una palabra a buscar :")   
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
            tablero[contador_credito]=lista_2   




        # mostar el tablero
        for i in range(5): 
            print(" ".join(tablero[i]))  
#--------------------------------fin de pedir datos--------------------------    
        contador_credito+=1 # cuenta las veses que intente
if ganador :
    print("ganaste")   
else:
    print("la proxima sera la buena ")    
