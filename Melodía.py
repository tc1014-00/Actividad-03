#encoding: UTF-8
#Autor: Jorge Daniel Juárez R.
#Descripción: Tocar una melodía

from Myro import*
do=523
re=587
mi=659
fa=698
sol=784
la=880
si=987
p=0

def compasUno (d):
    beep(d,mi)
    beep(d,mi)
    beep(d,fa)
    beep(d,sol)
    
def compasDos(d):
    beep(d,sol)
    beep(d,fa)
    beep(d,mi)
    beep(d,re)
    
def compasTres(d):
    beep(d,do)
    beep(d,do)
    beep(d,re)
    beep(d,mi)
    
def compasCuatro(d):
    beep((d*1.5),mi)
    beep(d/2,re)
    beep((2*d),re)
    
def compasCinco(d):
    beep((d*1.5),re)
    beep(d/2,do)
    beep((2*d),do)
    
def compasSeis(d):
    beep(d,re)
    beep(d,re)
    beep(d,mi)
    beep(d,do)
            
def compasSiete(d):
    beep(d,re)
    beep(d/2,mi)
    beep(d/2,fa)
    beep(d,mi)
    beep(d,do)
    
def compasOcho(d):
    beep(d,re)
    beep(d/2,mi)
    beep(d/2,fa)
    beep(d,mi)
    beep(d,re)
    
def compasNueve(d):
    beep(d,do)
    beep(d,re)
    beep(d,p)
            
compasUno(0.3) 
compasDos(0.3)
compasTres(0.3)
compasCuatro(0.3)
compasUno(0.3) 
compasDos(0.3)
compasTres(0.3)
compasCinco(0.3)
compasSeis(0.3)
compasSiete(0.3)
compasOcho(0.3)
compasNueve(0.3)
compasUno(0.3) 
compasDos(0.3)
compasTres(0.3)
compasCinco(0.3)