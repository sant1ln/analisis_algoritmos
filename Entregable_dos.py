import random
from time import perf_counter_ns

# Python program for implementation of MergeSort


def mergeSort(arr):
    if len(arr) > 1:

         # Finding the mid of the array
        mid = len(arr)//2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        return arr


def llenado(limite=10):
    data = []
    random_number = 0
    for _ in range(limite):
        random_number = random.randint(1,1000)
        data.append(random_number)

    return data


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# Driver Code
if __name__ == '__main__':
    data = llenado()
    tiempos = []
    datos = [10,100,200,300,400,500,600,700,800,900,1000]
    for i in datos:
      data = llenado(i)
      inicio_timer = perf_counter_ns()
      mergeSort(data)      
      final_timer = perf_counter_ns()
      timpo_total = round(final_timer - inicio_timer)
      tiempos.append(timpo_total)
    ##printList(data)
    print('Data >', datos)  
    print('Tiempos >', tiempos)