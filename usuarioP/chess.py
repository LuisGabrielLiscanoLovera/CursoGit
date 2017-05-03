__author__ = 'HICC2'
#lista ordenadas en python
'''cosmo=4*2 #usando potencia
l1 =[10]*8
print( l1 )
'''
#*********************ejmplo simple de matriz*-****
'''lista= [0]*5
print (lista)
matriz=[lista]*4
matriz [0][2]=3
print (matriz)'''

matriz =[]
filas = int(input("Incerte cantida de filas: "))
columnas=int(input("incerte la cantidad de columnsa: "))
for i in range(filas):
    matriz.append([0]*columnas)
for f in range (filas):
    for c in range (columnas):
        matriz [f][c]=int (input("elementos  %d, %d :" % (f,c)))
print(matriz)
#matriz[0][2]="Jake" (modificar un valor de la columna)
#*******************Acceder a la matriz
l4=[["uno",[3]],[4]]
l5=[4,3,2,0,1,[5,7],[6,8]]
print(l5)
l5 [5]=[10,11,12]
print(l5[5])
#Medir la cantidad de elememtos en una matriz
print (len(l5))
#medir la cantida de elementos e una matriz
print(len(matriz[0]))
