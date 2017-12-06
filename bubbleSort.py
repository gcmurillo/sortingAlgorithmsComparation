
from time import *
import configuraciones

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

# #PARA LA CONFIGURACION A
# confA = configuraciones.confA('BubbleSort')
#
# archivo = open('ordenadoABubleSort.txt', 'a')
archivoTiempo = open('tiempoBubble.txt', 'a')
# total = 0
#
# for i in confA:
#     start_time = time()
#     bubbleSort(i)
#     transcurrido = time() - start_time
#     archivo.write(str(i) + '\n')
#     total = transcurrido + total
#
# archivoTiempo.write('ConfA: ' + str(total) + '\n')
# archivo.close()
#
# #PARA LA CONFIGURACION B
#
# confB = configuraciones.confB('BubbleSort')
#
# archivo = open('ordenadoBBubleSort.txt', 'a')
# total = 0
#
# for i in confB:
#     start_time = time()
#     bubbleSort(i)
#     transcurrido = time() - start_time
#     archivo.write(str(i) + '\n')
#     total = transcurrido + total
#
# archivoTiempo.write('ConfB: ' + str(total) + '\n')
# archivo.close()
#
# #PARA LA CONFIGURACION C
#
# confC = configuraciones.confC('BubbleSort')
#
# archivo = open('ordenadoCBubleSort.txt', 'a')
# total = 0
#
# for i in confC:
#     start_time = time()
#     bubbleSort(i)
#     transcurrido = time() - start_time
#     archivo.write(str(i) + '\n')
#     total = transcurrido + total
#
# archivoTiempo.write('ConfC: ' + str(total) + '\n')
# archivo.close()
#
# #PARA LA CONFIGURACION D
#
# confD = configuraciones.confD('BubbleSort')
#
# archivo = open('ordenadoDBubleSort.txt', 'a')
# total = 0
#
# for i in confD:
#     start_time = time()
#     bubbleSort(i)
#     transcurrido = time() - start_time
#     archivo.write(str(i) + '\n')
#     total = transcurrido + total
#
# archivoTiempo.write('ConfD: ' + str(total) + '\n')
# archivo.close()
#
# #PARA LA CONFIGURACION E
#
# confE = configuraciones.confE('BubbleSort')
#
# archivo = open('ordenadoEBubleSort.txt', 'a')
# total = 0
#
# for i in confE:
#     start_time = time()
#     bubbleSort(i)
#     transcurrido = time() - start_time
#     archivo.write(str(i) + '\n')
#     total = transcurrido + total
#
# archivoTiempo.write('ConfE: ' + str(total) + '\n')
# archivo.close()

#PARA LA CONFIGURACION F

confF = configuraciones.confF('BubbleSort')

archivo = open('ordenadoFBubleSort.txt', 'a')
total = 0

for i in confF:
    start_time = time()
    bubbleSort(i)
    transcurrido = time() - start_time
    archivo.write(str(i) + '\n')
    total = transcurrido + total

archivoTiempo.write('ConfF: ' + str(total) + '\n')
archivo.close()