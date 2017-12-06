
from time import *
import configuraciones

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      print("After increments of size",sublistcount,
                                   "The list is",alist)

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

#PARA LA CONFIGURACION A
arreglo = configuraciones.confA('ShellSort')

archivo = open('ordenadoAShellSort.txt', 'a')
archivoTiempo = open('tiempoShell.txt', 'a')
total = 0

for i in arreglo:
    start_time = time()
    shellSort(i)
    transcurrido = time() - start_time
    archivo.write(str(i) + '\n')
    total = transcurrido + total

archivoTiempo.write('ConfA: ' + str(total) + '\n')
archivo.close()

#PARA LA CONFIGURACION B
arreglo = configuraciones.confB('ShellSort')

archivo = open('ordenadoBShellSort.txt', 'a')
total = 0

for i in arreglo:
    start_time = time()
    shellSort(i)
    transcurrido = time() - start_time
    archivo.write(str(i) + '\n')
    total = transcurrido + total

archivoTiempo.write('ConfB: ' + str(total) + '\n')
archivo.close()

#PARA LA CONFIGURACION C
arreglo = configuraciones.confC('ShellSort')

archivo = open('ordenadoCShellSort.txt', 'a')
total = 0

for i in arreglo:
    start_time = time()
    shellSort(i)
    transcurrido = time() - start_time
    archivo.write(str(i) + '\n')
    total = transcurrido + total

archivoTiempo.write('ConfC: ' + str(total) + '\n')
archivo.close()

#PARA LA CONFIGURACION D
arreglo = configuraciones.confD('ShellSort')

archivo = open('ordenadoDShellSort.txt', 'a')
total = 0

for i in arreglo:
    start_time = time()
    shellSort(i)
    transcurrido = time() - start_time
    archivo.write(str(i) + '\n')
    total = transcurrido + total

archivoTiempo.write('ConfD: ' + str(total) + '\n')
archivo.close()

#PARA LA CONFIGURACION E
arreglo = configuraciones.confE('ShellSort')

archivo = open('ordenadoEShellSort.txt', 'a')
total = 0

for i in arreglo:
    start_time = time()
    shellSort(i)
    transcurrido = time() - start_time
    archivo.write(str(i) + '\n')
    total = transcurrido + total

archivoTiempo.write('ConfE: ' + str(total) + '\n')
archivo.close()

#PARA LA CONFIGURACION F
arreglo = configuraciones.confF('ShellSort')

archivo = open('ordenadoFShellSort.txt', 'a')
total = 0

for i in arreglo:
    start_time = time()
    shellSort(i)
    transcurrido = time() - start_time
    archivo.write(str(i) + '\n')
    total = transcurrido + total

archivoTiempo.write('ConfF: ' + str(total) + '\n')
archivo.close()