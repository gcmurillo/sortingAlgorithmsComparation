
from time import *
import configuraciones

# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)


# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

#PARA LA CONFIGURACION A
arreglo = configuraciones.confA('HeapSort')

archivo = open('ordenadoAHeapSort.txt', 'a')
archivoTiempo = open('tiempoHeap.txt', 'a')
total = 0

for i in arreglo:
    start_time = time()
    heapSort(i)
    transcurrido = time() - start_time
    archivo.write(str(i) + '\n')
    total = transcurrido + total

archivoTiempo.write('ConfA: ' + str(total) + '\n')
archivo.close()

#PARA LA CONFIGURACION B
arreglo = configuraciones.confB('HeapSort')

archivo = open('ordenadoBHeapSort.txt', 'a')
total = 0

for i in arreglo:
    start_time = time()
    heapSort(i)
    transcurrido = time() - start_time
    archivo.write(str(i) + '\n')
    total = transcurrido + total

archivoTiempo.write('ConfB: ' + str(total) + '\n')
archivo.close()

#PARA LA CONFIGURACION C
arreglo = configuraciones.confC('HeapSort')

archivo = open('ordenadoCHeapSort.txt', 'a')
total = 0

for i in arreglo:
    start_time = time()
    heapSort(i)
    transcurrido = time() - start_time
    archivo.write(str(i) + '\n')
    total = transcurrido + total

archivoTiempo.write('ConfC: ' + str(total) + '\n')
archivo.close()

#PARA LA CONFIGURACION D
arreglo = configuraciones.confD('HeapSort')

archivo = open('ordenadoDHeapSort.txt', 'a')
total = 0

for i in arreglo:
    start_time = time()
    heapSort(i)
    transcurrido = time() - start_time
    archivo.write(str(i) + '\n')
    total = transcurrido + total

archivoTiempo.write('ConfD: ' + str(total) + '\n')
archivo.close()

#PARA LA CONFIGURACION E
arreglo = configuraciones.confE('HeapSort')

archivo = open('ordenadoEHeapSort.txt', 'a')
total = 0

for i in arreglo:
    start_time = time()
    heapSort(i)
    transcurrido = time() - start_time
    archivo.write(str(i) + '\n')
    total = transcurrido + total

archivoTiempo.write('ConfE: ' + str(total) + '\n')
archivo.close()

#PARA LA CONFIGURACION F
arreglo = configuraciones.confF('HeapSort')

archivo = open('ordenadoFHeapSort.txt', 'a')
total = 0

for i in arreglo:
    start_time = time()
    heapSort(i)
    transcurrido = time() - start_time
    archivo.write(str(i) + '\n')
    total = transcurrido + total

archivoTiempo.write('ConfF: ' + str(total) + '\n')
archivo.close()