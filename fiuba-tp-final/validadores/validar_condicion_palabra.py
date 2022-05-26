from helpers.formatear_palabra import formatear_palabra
from initialSetting.datos_iniciales import condiciones_iniciales

def validar_condicion_palabra():
  """
  Esta funcion es la encargrada de cumplir con la validacion de las condiciones para que la palabra
  sea valida,luego que termina con la validacion ,la devuelve en mayusculas
  Recibe por terminal la palabra,la verfifica
  autor omar jaldin
  """
  MAX_LETRAS = condiciones_iniciales()["cantidad_letras"]# busca en un diccionario  la clave ---> CANTIDAD_LETRAS = 5
  
  palabra=input("Arriesgo :")
  while len(palabra)!=MAX_LETRAS or (not palabra.isalpha()):
    if len(palabra)!=MAX_LETRAS:
        #Arriesgo :a
        print(f"la palabra debe tener {MAX_LETRAS} letras y tiene {len(palabra)}")
        #la palabra debe tener 5 letras y tiene 1
    elif not palabra.isalpha() :# si no es string
        #Arriesgo :hola1
        print(f"La palabra debe contener solo letras")
        #La palabra debe contener solo letras
    palabra=input("Arriesgo :") 
  palabra=formatear_palabra(palabra)
  """
  Aqui nos devuelve la palabra sin acentos, " sofás" genera el mismo resultado que "sofas"
  """
  return palabra.upper()# convertir una cadena a mayúsculas "SOFAS"
  

  ''' Turno de ---> Omar
      Arriesgo :2
      la palabra debe tener 5 letras y tiene 1
      Arriesgo :per 
      la palabra debe tener 5 letras y tiene 3 '''