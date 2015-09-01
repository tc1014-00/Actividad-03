#encoding UTF-8
#Pablo Alejadro Sanchez Tadeo
#Tarea 3: reproduciendo musica (La Vie en Rose)

from Myro import *

#Notas que se van a usar
do = 1046
re = 1174
mi = 1318
fa = 1396
sol = 1567
la = 1760
si = 1975
#notas que se usan una octava mas arriba
do1 = 2093
re1 = 2349

#primer compas
def compasUno(d) :
    beep(d*2,do1)
    beep(d,si)
    beep(d,la)
    beep(d,sol)
    beep(d,mi)
    beep(d,do1)
#segundo compas
def compasDos(d) :
    beep(d*2,si)
    beep(d,la)
    beep(d,sol)
    beep(d,mi)
    beep(d,do)
    beep(d,si)
#tercer compas
def compasTres(d) :
    beep(d*2,la)
    beep(d,sol)
    beep(d,mi)
    beep(d,do)
    beep(d,re)
    beep(d,si)
#cuarto compas
def compasCuatro(d) :
    beep(d*2,la)
    beep(d,re)
    beep(d,mi)
    beep(d,fa)
    beep(d,la)
    beep(d*2,sol)
#quinto compas
def compasCinco(d) :
    beep(d*2,re1)
    beep(d,do1)
    beep(d,si)
    beep(d,la)
    beep(d,fa)
    beep(d,do1)
#sexto compas
def compasSeis(d) :
    beep(d*2,si)
    beep(d/2,la)
    beep(d/2,si)
    beep(d,la)
    beep(d,sol)
    beep(d,fa)
    beep(d,re)
    beep(d,si)
#septimo compas
def compasSiete(d) :
    beep(d*2,la)
    beep(d,sol)
    beep(d,fa)
    beep(d,mi)
    beep(d,re)
    beep(d,la)
#octavo compas
def compasOcho(d) :
    beep(d,la)
    beep(d,si)
    beep(d,si)
    beep(d,la)
    beep(d*2,sol)
    beep(d,sol)
#noveno compas
def compasNueve(d) :
    beep(d*2,do1)
    beep(d/2,si)
    beep(d/2,do1)
    beep(d,si)
    beep(d,la)
    beep(d,sol)
    beep(d,mi)
    beep(d,do1)
#decimo compas
def compasDiez(d) :
    beep(d*2,si)
    beep(d,la)
    beep(d,sol)
    beep(d,mi)
    beep(d,do)
    beep(d,si)
#onceavo compas
def compasOnce(d) :
    beep(d*2,la)
    beep(d,sol)
    beep(d,mi)
    beep(d,do)
    beep(d*2,do1)
     
    
t = 0.5
compasUno(t)
compasDos(t)
compasTres(t)
compasCuatro(t)
compasCinco(t)
compasSeis(t)
compasSiete(t)
compasOcho(t)
compasNueve(t)
compasDiez(t)
compasOnce(t)