from initialSetting.colores import obtener_color
from initialSetting.initial_tablero import tablero_initial_setting
from initialSetting.conditions import *
from validators.len_palabra import validar_longitud_palabra
from validators.ganador import valida_ganador
from generadorLista.correcta import palabra_correcta

tablero = tablero_initial_setting()

while (not es_ganador) and (contador_credito< 5):
  print("Palabra a adivinar: ? ? ? ? ?")
  palabra = validar_longitud_palabra()
  if valida_ganador(palabra,palabra_lista):
    es_ganador=True 
    palabra_correcta(palabra)
  else:
    lista_2=[]
    for i in range(len(palabra)):
      if palabra[i] in palabra_lista[i]:
        lista_2.append(obtener_color( palabra[i],"Verde" ))
      elif palabra[i] in palabra_lista:
        lista_2.append( obtener_color( palabra[i],"Amarillo" ))
      else:
        lista_2.append( obtener_color( palabra[i],"Rojo" ))    
      
      tablero[contador_credito]=lista_2 
  
  contador_credito+=1
  print(contador_credito)
  for i in range(5): 
    print(" ".join(tablero[i]))  


if es_ganador :
    print("ganaste")   
else:
    print("la proxima sera la buena ")