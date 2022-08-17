from time import perf_counter_ns
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
  
  print(f"Maxima subsuma 1: {maxima_suma}")
   
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
  

  print(f"Maxima subsuma 2: {maxima_suma}")

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
  
  print(f"Maxima subsuma 3: {maxima_suma}")


def llenado():
    limit = 10000
    data = []
    random_number = 0
    for _ in range(limit):
        random_number = random.randint(-limit,limit)
        data.append(random_number)
    
    return data

def analizarTiempo():
  data = llenado()
  funciones = [maxima_subsuma,maxima_subsuma_dos,maxima_subsuma_tres]
  tiempos = []
  for funcion in funciones:
    inicio_timer = perf_counter_ns()
    funcion(data)
    final_timer = perf_counter_ns()
    total_time = round(final_timer - inicio_timer)
    tiempos.append(f"{total_time}ns")
  
  print(tiempos)


analizarTiempo()




