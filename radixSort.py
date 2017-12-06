from math import log10
from time import *
import configuraciones

def get_digit(number, base, pos):
  return (number // base ** pos) % base

def prefix_sum(array):
  for i in range(1, len(array)):
    array[i] = array[i] + array[i-1]
  return array

def radixsort(l, base=10):
  passes = int(log10(max(l))+1)
  output = [0] * len(l)

  for pos in range(passes):
    count = [0] * base

    for i in l:
      digit = get_digit(i, base, pos)
      count[digit] +=1

    count = prefix_sum(count)

    for i in reversed(l):
      digit = get_digit(i, base, pos)
      count[digit] -= 1
      new_pos = count[digit]
      output[new_pos] = i

    l = list(output)
  return output

#PARA LA CONFIGURACION A
arreglo = configuraciones.confA('RadixSort')

archivo = open('ordenadoARadixSort.txt', 'a')
archivoTiempo = open('tiempoRadix.txt', 'a')
total = 0

for i in arreglo:
    start_time = time()
    radixsort(i)
    transcurrido = time() - start_time
    archivo.write(str(i) + '\n')
    total = transcurrido + total

archivoTiempo.write('ConfA: ' + str(total) + '\n')
archivo.close()

#PARA LA CONFIGURACION B
arreglo = configuraciones.confB('RadixSort')

archivo = open('ordenadoBRadixSort.txt', 'a')
total = 0

for i in arreglo:
    start_time = time()
    radixsort(i)
    transcurrido = time() - start_time
    archivo.write(str(i) + '\n')
    total = transcurrido + total

archivoTiempo.write('ConfB: ' + str(total) + '\n')
archivo.close()

#PARA LA CONFIGURACION C
arreglo = configuraciones.confC('RadixSort')

archivo = open('ordenadoCRadixSort.txt', 'a')
total = 0

for i in arreglo:
    start_time = time()
    radixsort(i)
    transcurrido = time() - start_time
    archivo.write(str(i) + '\n')
    total = transcurrido + total

archivoTiempo.write('ConfC: ' + str(total) + '\n')
archivo.close()

#PARA LA CONFIGURACION D
arreglo = configuraciones.confD('RadixSort')

archivo = open('ordenadoDRadixSort.txt', 'a')
total = 0

for i in arreglo:
    start_time = time()
    radixsort(i)
    transcurrido = time() - start_time
    archivo.write(str(i) + '\n')
    total = transcurrido + total

archivoTiempo.write('ConfD: ' + str(total) + '\n')
archivo.close()

#PARA LA CONFIGURACION E
arreglo = configuraciones.confE('RadixSort')

archivo = open('ordenadoERadixSort.txt', 'a')
total = 0

for i in arreglo:
    start_time = time()
    radixsort(i)
    transcurrido = time() - start_time
    archivo.write(str(i) + '\n')
    total = transcurrido + total

archivoTiempo.write('ConfE: ' + str(total) + '\n')
archivo.close()

#PARA LA CONFIGURACION F
arreglo = configuraciones.confF('RadixSort')

archivo = open('ordenadoFRadixSort.txt', 'a')
total = 0

for i in arreglo:
    start_time = time()
    radixsort(i)
    transcurrido = time() - start_time
    archivo.write(str(i) + '\n')
    total = transcurrido + total

archivoTiempo.write('ConfF: ' + str(total) + '\n')
archivo.close()