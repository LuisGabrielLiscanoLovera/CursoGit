__author__ = 'HICC2'
#coding: utf-8
def funcion():
    return ("Hola mundo")


a =object()
b=int()
print(a)
print(b)
print(funcion())
#lista
yo="soy"
l1=["liscano",25,"luis","1991","Hola",yo,"tengo"]
print(l1[4],l1[5],l1[2],l1[0],("Naci en el año ")+l1[3],l1[6],l1[1])
#Tuples
l2=(1,"2",3,4,"5")
for i in l2:
    print(i)
master="Lord Luis Liscano"
departamento={
    2:1000,
    "Name":master,
    "Age":21,
    "Firsdate":"1991"
    }
print (departamento["Name"])
string="21"
#print (string+2) linea da error ya que string no es un entero y por esao no la suma 406 hay que convertila
conversionDstring=int(string)
print (conversionDstring+2)
rango=range(24)
r1=map(str,rango)
print (sum(rango))

################################# Al descomentar suena la musica ######################
import pyglet as glet
print (dir (glet))
music = glet.resource.media('BONUS TRACK - JEREMIAS 17-5.mp3')
music.play()
glet.app.run()

#ordenar
l3=[4,8,9,6,3]
print(l3)
print (sorted(l3))
#REversa
print (l3.reverse())
print(round(3.14555,3))

for i in range(10):
    l4=[4]
    print (l4,"%i"%i)
