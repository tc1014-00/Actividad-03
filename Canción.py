#encoding: UTF-8
#Autor: Abraham Gandaria Alonso, A01377349
#Description: Cancion Mario Bros

from Myro import*

#Notas

do=523.251
re=587.33
mi=659.255
fa=698.456
sol=783.991
la=880
si=987.767
fas=739.989
sols=830.609

#Primer compas
def reproducirCompasUno (duracion):
    beep(duracion,mi)
    beep(duracion,do)
    beep(duracion,mi)
    beep(duracion,sol)

#Segundo compas
def reproducirCompasDos (duracion):
    beep(duracion,do)
    beep(duracion,sol)
    beep(duracion,mi)
    beep(duracion,la)
    beep(duracion*2,si)
    beep(duracion,sol)
    beep(duracion,mi)


#Tercer compas
def reproducirCompasTres (duracion):
    beep(duracion,sol)
    beep(duracion,la)
    beep(duracion,fa)
    beep(duracion,sol)
    beep(duracion,mi)
    beep(duracion,do)
    beep(duracion,re)
    beep(duracion,si)

#Cuarto compas
def reproducirCompasCuatro (duracion):
    beep(duracion,do)
    beep(duracion,sol)
    beep(duracion,mi)
    beep(duracion,la)
    beep(duracion*2,si)
    beep(duracion,sol)
    beep(duracion,mi)

#Quinto compas
def reproducirCompasCinco (duracion):
    beep(duracion,sol)
    beep(duracion,la)
    beep(duracion,fa)
    beep(duracion,sol)
    beep(duracion,mi)
    beep(duracion,do)
    beep(duracion,re)
    beep(duracion,si)


#Sexto compas
def reproducirCompasSeis(duracion):
    beep(duracion,sol)
    beep(duracion,fas)
    beep(duracion,fa)
    beep(duracion,mi)
    beep(duracion,sols)
    beep(duracion,la)
    beep(duracion,do)
    beep(duracion,la)
    beep(duracion,do)
    beep(duracion,re)
    
#Septimo compas
def reproducirCompasSiete (duracion):
    beep(duracion,sols)
    beep(duracion,fas)
    beep(duracion,fa)
    beep(duracion,mi)
    beep(duracion,do)
    
#Octavo compas
def reproducirCompasOcho (duracion):
    beep(duracion,sol)
    beep(duracion,fas)
    beep(duracion,fa)
    beep(duracion,mi)
   
#Noveno compas
def reproducirCompasNueve (duracion):
    beep(duracion,sols)
    beep(duracion,la)
    beep(duracion,do)
    beep(duracion,re)
    beep(duracion,mi)
    beep(duracion,re)
    beep(duracion,do)
    
#Decimo compas
def reproducirCompasDiez (duracion):
    beep(duracion,sol)
    beep(duracion,fas)
    beep(duracion,fa)
    beep(duracion,mi)
    
#Decimoprimero compas
def reproducirCompasOnce (duracion):
    beep(duracion,sols)
    beep(duracion,la)
    beep(duracion,do)
    beep(duracion,re)
    beep(duracion,mi)
    beep(duracion,re)
    beep(duracion,do)


reproducirCompasUno(0.3)
reproducirCompasDos(0.3)
reproducirCompasTres(0.3)
reproducirCompasCuatro(0.3)
reproducirCompasCinco(0.3)
reproducirCompasSeis(0.3)
reproducirCompasOcho(0.3)
reproducirCompasNueve(0.3)
reproducirCompasDiez(0.3)
reproducirCompasOnce(0.3)