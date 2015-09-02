#Encoding: UTF-8
#Autor: Paola Castillo Nacif
#Funciones para reproducir musica

from Myro import*
#Notas 
si=987.767
do=523.251
re=587.33
la=880
sol=783.991
mi=659.255
fa=698.456

#Primer compas
def reproducirCompasUno (duracion):
    beep(duracion*2,mi)
    beep(duracion,mi)
    beep(duracion,fa)
    beep(duracion,sol)

#Segundo compas
def reproducirCompasDos(duracion):
    beep(duracion,sol)
    beep(duracion,fa)
    beep(duracion,mi)
    beep(duracion,re)

#Tercer compas
def reproducirCompasTres(duracion):
    beep(duracion,do)
    beep(duracion,do)
    beep(duracion,re)
    beep(duracion,mi)

#Cuarto compas
def reproducirCompasCuatro(duracion):
    beep(duracion*2,mi)
    beep(duracion/2,re)
    beep(duracion*2,re)

#Quinto compas
def reproducirCompasCinco(duracion):
    beep(duracion*2,mi)
    beep(duracion,mi)
    beep(duracion,fa)
    beep(duracion,sol)
    
#Sexto compas
def reproducirCompasSeis(duracion):
    beep(duracion,sol)
    beep(duracion,fa)
    beep(duracion,mi)
    beep(duracion,re)

#Septimo compas
def reproducirCompasSiete(duracion):
    beep(duracion,do)
    beep(duracion,do)
    beep(duracion,re)
    beep(duracion,mi)

#Octavo compas
def reproducirCompasOcho(duracion):
    beep(duracion*2,re)
    beep(duracion/2,do)
    beep(duracion*2,do)

#Noveno compas
def reproducirCompasNueve(duracion):
    beep(duracion*2,la)
    beep(duracion,si)
    beep(duracion,sol)

#Decimo compas
def reproducirCompasDiez(duracion):
    beep(duracion,la)
    beep(duracion/2,si)
    beep(duracion/2,do)
    beep(duracion,si)
    beep(duracion,sol)

#Undecimo compas    
def reproducirCompasOnce(duracion):
    beep(duracion,la)
    beep(duracion/2,si)
    beep(duracion/2,do)
    beep(duracion,si)
    beep(duracion,la)

#Duodecimo compas
def reproducirCompasDoce(duracion):
    beep(duracion,sol)
    beep(duracion,la)
    beep(duracion*2,re)

#Decimotercer compas
def reproducirCompasTrece(duracion):
    beep(duracion*2,sol)
    beep(duracion,la)
    beep(duracion,si)

#Decimocuarto compas
def reproducirCompasCatorce(duracion):
    beep(duracion,re)
    beep(duracion,do)
    beep(duracion,si)
    beep(duracion,la)  
  
#Decimoquino compas
def reproducirCompasQuince(duracion):
    beep(duracion,sol)
    beep(duracion,sol)
    beep(duracion,la)
    beep(duracion,si)

#Decimosexto compas
def reproducirCompasDieciseis(duracion):
    beep(duracion*3,la)
    beep(duracion,sol)
    beep(duracion*2,sol)   
    
reproducirCompasUno(0.25)
reproducirCompasDos(0.25)
reproducirCompasTres(0.25)
reproducirCompasCuatro(0.25)
reproducirCompasCinco(0.25)
reproducirCompasSeis(0.25)
reproducirCompasOcho(0.25)
reproducirCompasNueve(0.25)
reproducirCompasDiez(0.25)
reproducirCompasOnce(0.25)
reproducirCompasDoce(0.25)
reproducirCompasTrece(0.25)
reproducirCompasCatorce(0.25)
reproducirCompasQuince(0.25)
reproducirCompasDieciseis(0.25)