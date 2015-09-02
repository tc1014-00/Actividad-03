#encoding: UTF-8
#Autor: José Ramón Mondragón
#Haciendo Música

from Myro import*
#Declara las notas que vas a usar
SOL = 3135.963
LA = 3520
DO = 2093.005
SI = 3951.006
RE = 2349.318
FA = 2793.826
MI = 2637.02

#Primer compas
def reproducirCompasUno(duracion) :
    beep(duracion,SOL)
    beep(duracion,SOL)
    
#Segundo compas
def reproducirCompasDos (duracion) :
    beep(duracion,LA)
    beep(duracion,SOL)
    beep(duracion,DO) 
    
#Trecer compas
def reproducirCompasTres (duracion) :
    beep(2*duracion,SI)
    beep(duracion,SOL)
    beep(duracion,SOL)          
    
#Cuarto compas
def reproducirCompasCuatro (duracion):
    beep(2*duracion,LA)
    beep(duracion,SOL)
    beep(duracion,RE)   
 
#Quinto compas
def reproducirCompasCinco (duracion):
     beep(2*duracion,DO)
     beep(duracion,SOL)
     beep(duracion,SOL)

#Sexto compas
def reproducirCompasSeis (duracion):
    beep(duracion,SOL)
    beep(duracion,MI)
    beep(duracion,DO)
    beep(duracion,DO)
    
#Septimo compas    
def reproducirCompasSiete (duracion):
    beep(duracion,SI)
    beep(duracion,LA)
    beep(duracion,FA)
    beep(duracion,FA)      
                              
#Octavo compas
def reproducirCompasOcho (duracion):
    beep(duracion,MI)
    beep(duracion,DO)
    beep(duracion,RE)   
   
#Noveno compas  
def reproducirCompasNueve (duracion):
    beep(2*duracion,DO)      
                                                                                                                       
tiempo = 0.3
reproducirCompasUno (tiempo)
reproducirCompasDos (tiempo)
reproducirCompasTres (tiempo)
reproducirCompasCuatro (tiempo)
reproducirCompasCinco (tiempo)
reproducirCompasSeis (tiempo)
reproducirCompasSiete (tiempo)
reproducirCompasOcho (tiempo)
reproducirCompasNueve(tiempo)