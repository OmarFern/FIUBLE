from unicodedata import numeric
from initialSetting.obtener_palabra import obtener_palabras_validas
import random

num_random = random.randint(0,len(obtener_palabras_validas()))

print(num_random)
es_ganador=False
palabra_lista=obtener_palabras_validas()[num_random]
contador_credito = 0

