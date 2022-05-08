def validar_longitud_palabra(palabra):
  while len(palabra)!=5:
    print(f"la palabra debe tener 5 letras y tiene {len(palabra)}")
    palabra=input("Arriesgo :")