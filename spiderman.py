# Encoding: UTF-8
# Autor: Ernesto Cruz López A01169052
# Reproducir una canción en calico usando funciones.


from Myro import *

Do=261
Re=293
Mi=329
Fa=349
Sol=392
La=440
Si=493
DO=523
sh=0

def reproducirCompasUno(duracion):
    beep(duracion/2,sh)
    beep(duracion/2,Do)
    beep(duracion,Do)
    beep(duracion/2,Mi)
    beep((duracion/2)+.25,Sol)
    
def reproducirCompasDos(duracion):
    beep(duracion/2,sh)
    beep(duracion/2,Sol)
    beep(duracion,Sol)
    beep(duracion/2,Mi)
    beep((duracion/2)+.25,Do)
    
def reproducirCompasTres(duracion):
    beep(duracion/2,sh)
    beep(duracion/2,Do)
    beep(duracion,Do)
    beep(duracion/2,Mi)
    beep((duracion/2+.25),Sol)
    
def reproducirCompasCuatro(duracion):
    beep(duracion,Sol)
    beep(duracion,Fa)
    beep(duracion/2,Re)
    beep((duracion/2)+.25,Do)
    
def reproducirCompasCinco(duracion):
    beep(duracion/2,sh)
    beep(duracion/2,Do)
    beep(duracion,Fa)
    beep(duracion/2,La)
    beep((duracion/2)+.25,DO)
    
def reproducirCompasSeis(duracion):
    beep(duracion/2,sh)
    beep(duracion/2,DO)
    beep(duracion,DO)
    beep(duracion/2,La)
    beep((duracion/2)+.25,Fa)
    
def reproducirCompasSiete (duracion):
    beep(duracion,Sol)
    beep(duracion,Fa)
    beep(duracion/2,Re)
    beep((duracion/2)+.50,Do)
    
def reproducirCompasOcho (duracion):
    beep(duracion/2,sh)
    beep(duracion/2,Sol)
    beep(duracion,Sol)
    beep(duracion/2,Fa)
    beep(duracion+.125,Sol)
    
def reproducirCompasNueve (duracion):
    beep(duracion/2,Re)
    beep((duracion/2)+.25,Do)
    
    
tiempo=.25
reproducirCompasUno(tiempo)
reproducirCompasDos(tiempo)
reproducirCompasTres(tiempo)
reproducirCompasCuatro(tiempo)
reproducirCompasCinco(tiempo)
reproducirCompasSeis(tiempo)
reproducirCompasTres(tiempo)
reproducirCompasSiete(tiempo)
reproducirCompasOcho(tiempo)
reproducirCompasOcho(tiempo)
reproducirCompasNueve(tiempo)
