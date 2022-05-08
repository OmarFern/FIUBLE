from initialSetting.colores import obtener_color
from initialSetting.initial_tablero import tablero_initial_setting
from initialSetting.conditions import *
from validators.len_palabra import validar_longitud_palabra
from validators.ganador import valida_ganador
from generadorLista.correcta import palabra_correcta
from validators.analizar_palabra import analizar_palabra
from validators.gana_juego import gana_juego

tablero = tablero_initial_setting()

while (not es_ganador) and (contador_credito< 5):
  print("Palabra a adivinar: ? ? ? ? ?")
  palabra = validar_longitud_palabra()
  if valida_ganador(palabra,palabra_lista):
    es_ganador=True 
    tablero = palabra_correcta(palabra)
  else:
    lista_2 = analizar_palabra(palabra)
    tablero[contador_credito]=lista_2 
  
  contador_credito+=1
  for i in range(5): 
    print(" ".join(tablero[i]))  

gana_juego(es_ganador)
