__author__ = 'HICC2'

def AreaTriangulo(base, altura):
    area= base * altura / 2.0
    return area
#R=AreaTriangulo(int(input("Indique base: ")),int(input("Indique altura: ")))
R=AreaTriangulo(4,8)
print("EL area de del triangulo es: (%i)" % R)

def duplicar(lista):
    for i in range (len(lista)):
        lista[i]=lista[i]*2
    return

numeros=list(range(11))
print(numeros)
duplicar(numeros)
print(numeros)
