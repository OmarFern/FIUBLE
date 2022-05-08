from initialSetting.initial_tablero import tablero_initial_setting
from initialSetting.conditions import contador_credito
from initialSetting.colores import obtener_color

def palabra_correcta(palabra):
  tablero =tablero_initial_setting()
  tablero[contador_credito]=[obtener_color( letra,"Verde" ) for letra in palabra]
  return tablero