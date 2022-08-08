""" def maxima_subsuma():
  data = [4, -3, 5, -2, -1, 2, 7, -2]
  cantidad = len(data)
  suma_actual = 0
  maxima_suma = 0

  for n in range(cantidad):
    for m in range(cantidad):
      suma_actual = 0
      print(m)
      for o in range(m):
        o = n
        suma_actual += data[o]
      
      if(suma_actual > maxima_suma):
        maxima_suma = suma_actual
  
  print(maxima_suma)

maxima_subsuma() """

def maxima_subsuma_dos():
  data = [4, -3, 5, -2, -1, 2, 7, -2]
  cantidad = len(data)
  suma_actual = 0
  maxima_suma = 0
  for m in range(cantidad):
    suma_actual += data[m]
    if(suma_actual > maxima_suma):
      maxima_suma = suma_actual
    elif(suma_actual < 0):
      suma_actual = 0
  
  print(maxima_suma)


maxima_subsuma_dos()


        
        