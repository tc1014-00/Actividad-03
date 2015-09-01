# encoding UTF-8
# Autor: Mauricio Medrano, A01272273
# Funciones para reproducir musica 

from Myro import * 

SI = 1975
DO = 1108
RE = 1244
LA = 1760
SOL = 1975

def reproducirCompasUno (duracion) :
    beep(duracion*2,SI) 
    beep(duracion,DO) 
    beep(duracion,RE)
    
def reproducirCompasDos (duracion) : 
    beep(duracion,RE)
    beep(duracion,DO)
    beep(duracion,SI)
    beep(duracion,LA)
    
def reproducirCompasTres (duracion) : 
    beep(duracion,SOL)
    beep(duracion,SOL)
    beep(duracion,LA)
    beep(duracion,SI)
    
def reproducirCompasCuatro (duracion) : 
    beep(duracion,SI)
    beep(duracion,LA)
    beep(duracion*2,LA) 
    
def reproducirCompasCinco (duracion) : 
    beep(duracion*2,LA)
    beep(duracion,SI)
    beep(duracion,SOL)
   
def reproducirCompasSeis (duracion) : 
    beep(duracion,LA)
    beep(duracion/2,SI)
    beep(duracion/2,DO)
    beep(duracion,SI)
    beep(duracion,SOL)
    
def reproducirCompasSiete (duracion) :
    beep(duracion,LA)
    beep(duracion/2,SI)
    beep(duracion/2,DO)
    beep(duracion,SI)
    beep(duracion,LA)
    
def reproducirCompasOcho (duracion) :  
    beep(duracion,SOL)
    beep(duracion,LA)
    beep(duracion*2,RE)
    
   
    
    
tiempo = 0.25
reproducirCompasUno(tiempo) 
reproducirCompasDos(tiempo)
reproducirCompasTres(tiempo)
reproducirCompasCuatro(tiempo) 
reproducirCompasUno(tiempo)
reproducirCompasDos(tiempo)
reproducirCompasTres(tiempo)
reproducirCompasCuatro(tiempo)
reproducirCompasCinco(tiempo)
reproducirCompasSeis(tiempo)
reproducirCompasSiete(tiempo)
reproducirCompasOcho(tiempo)


'''Aqui esta donde saque la partitura
https://youtube.com/watch?v=dnrHvA-DwJo

En realidad son 12 compases solo que se repiten'''








