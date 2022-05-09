from initialSetting.initial_tablero import initial_tablero
from initialSetting.initial_conditions import palabra_secreta
from validadores.fin_juego import fin_juego
from app import app
import time

res="si"

while res == "si" or res =="s":
  inicia_juego = time.time()
  tablero = initial_tablero()
  palabra_lista=palabra_secreta()
  print(palabra_lista)
  es_ganador=False
  contador_credito=0
  [es_ganador,palabra_lista,finaliza_juego,contador_credito] = app(tablero,palabra_lista,contador_credito,es_ganador)
  
  res =fin_juego(es_ganador,palabra_lista,inicia_juego,finaliza_juego,contador_credito)



