from time import perf_counter
import random


def maxima_subsuma(data):
  cantidad = len(data)
  suma_actual = 0
  maxima_suma = 0
  for n in range(cantidad):
    for m in range(cantidad):
      suma_actual = 0
      for o in range(n, m+1):
        suma_actual += data[o]      
      if(suma_actual > maxima_suma):
        maxima_suma = suma_actual
  
  print(maxima_suma)
   
def maxima_subsuma_dos(data):
  cantidad = len(data)
  suma_actual = 0
  maxima_suma = 0
  for n in range(cantidad):
      suma_actual = 0
      for m in range(n,cantidad):
          suma_actual += data[m]
          if(suma_actual > maxima_suma):
             maxima_suma = suma_actual

  print(maxima_suma)

def maxima_subsuma_tres(data):
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


def llenado():
    limit = 10000
    data = []
    random_number = 0
    for _ in range(limit):
        random_number = random.randint(-20,20)
        data.append(random_number)
    
    return data

data = llenado()

maxima_subsuma(data)
maxima_subsuma_dos(data)
maxima_subsuma_tres(data)



