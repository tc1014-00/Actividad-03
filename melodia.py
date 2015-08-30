#Encoding: UTF-8
#Autor: Manuel Zavala
#Funciones para reproducir musica

from Myro import *
#Declara las notas que vas a usar
mi=659
sol=1567
fa=698
la=1760
do=2093
si=3951
re=2349

#mi sol sol sol fa mi 
#Primer compás
def reproducirCompasUno(duracion):
    beep(duracion,mi)
    beep(duracion,sol)
    beep(duracion,sol)
    beep(duracion,sol)
    beep(duracion,fa)
    beep(duracion,mi)
tiempo=0.4
reproducirCompasUno(tiempo)
    
#sol sol
#Segundo Compás     
def reproducirCompasDos(duracion):
    beep(duracion,sol)
    beep(duracion,sol)
tiempo=0.4
reproducirCompasDos(tiempo)
 
#la fa la do la
#Tercer compas
def reproducirCompasTres(duracion):   
    beep(duracion,la)
    beep(duracion,fa)
    beep(duracion,la)
    beep(duracion,do)
    beep(duracion,la)
tiempo=0.4
reproducirCompasTres(tiempo) 
   
#sol sol
#Cuarto Compas
def reproducirCompasCuatro(duracion):    
    beep(duracion,sol)
    beep(duracion,sol)
tiempo=0.4
reproducirCompasCuatro(tiempo)
    
#la fa la do si la       
#Quinto Compás    
def reproducirCompasQuinto(duracion):
    beep(duracion,la)
    beep(duracion,fa)
    beep(duracion,la)
    beep(duracion,do)
    beep(duracion,si)
    beep(duracion,la)
tiempo=0.4
reproducirCompasQuinto(tiempo) 

# sol la sol mi do mi
#Sexto Compás
def reproducirCompasSexto(duracion):   
    beep(duracion,sol)
    beep(duracion,la)
    beep(duracion,sol)
    beep(duracion,mi)
    beep(duracion,do)
    beep(duracion,mi)
tiempo=0.4
reproducirCompasSexto(tiempo)  
  
# sol sol sol la si
#Septimo Compás    
def reproducirCompasSeptimo(duracion):
    beep(duracion,sol)
    beep(duracion,sol)
    beep(duracion,sol)
    beep(duracion,la)
    beep(duracion,si)
tiempo=0.4
reproducirCompasSeptimo(tiempo) 

#do
#Octavo Compás
def reproducirCompasOctavo(duracion):
    beep(duracion,do)
tiempo=0.4
reproducirCompasOctavo(tiempo)
    
#fa
#Noveno Compás
def reproducirCompasNoveno(duracion):
    beep(duracion,fa)
tiempo=0.4
reproducirCompasNoveno(tiempo)    

#la la la sol fa 
#Decimo compás
def reproducirCompasDecimo(duracion):
    beep(duracion,la)
    beep(duracion,la)
    beep(duracion,la)
    beep(duracion,sol)
    beep(duracion,fa)
tiempo=0.4
reproducirCompasDecimo(tiempo) 

# la la
#Onceavo compas
def reproducirCompasOnce(duracion):
    beep(duracion,la)
    beep(duracion,la)
tiempo=0.4
reproducirCompasOnce(tiempo)          

#si sol si re si
#Doceavo compás
def reproducirCompasDoce(duracion):
    beep(duracion,si)
    beep(duracion,sol)
    beep(duracion,si)
    beep(duracion,re)
    beep(duracion,si)
tiempo=0.4
reproducirCompasDoce(tiempo)

#la la
#Treceavo compas
def reproducirCompasTrece(duracion):
    beep(duracion,la)
    beep(duracion,la)
tiempo=0.4
reproducirCompasTrece(tiempo)            

 # si sol si re do# si 
#Catorce compás
def reproducirCompasCatorce(duracion):
    beep(duracion,si)
    beep(duracion,sol)
    beep(duracion,si)
    beep(duracion,re)
    beep(duracion,do)
    beep(duracion,si)
tiempo=0.4
reproducirCompasCatorce(tiempo)    

#la si la fa re fa
#Quince compás
def reproducirCompasQuince(duracion):
    beep(duracion,la)
    beep(duracion,si)
    beep(duracion,la)
    beep(duracion,fa)
    beep(duracion,re)
    beep(duracion,fa)
tiempo=0.4
reproducirCompasQuince(tiempo)

#la la l si do re
#Dieciseis compas
def reproducirCompasDieciseis(duracion):
    beep(duracion,la)
    beep(duracion,la)
    beep(duracion,la)
    beep(duracion,si)
    beep(duracion,re)
    beep(duracion,fa)
tiempo=0.4
reproducirCompasDieciseis(tiempo)                                    
    