#encoding: UTF-8
#Autor: Sergio Alberto Hernandez Mendez
#Descripcion: Utilizar funciones para reproducir musica

from Myro import *

mi4 = 329.63
fa4 = 349.23
sol4 = 392.00
la4 = 440.00
si4 = 493.88
do5 = 523.25
re5 = 587.33
mi5 = 659.26
tiempo = 2.00

def compasUno (duracion):
	beep (duracion/8, mi5)
	beep (duracion/8, si4)
	beep (duracion/8, sol4)
	beep (duracion/8, mi5)
	beep (duracion/8, si4)
	beep (duracion/8, sol4)
	beep (duracion/8, mi5)
	beep (duracion/8, si4)
    
def compasDos (duracion):
    beep (duracion/8, re5)
    beep (duracion/8, si4)
    beep (duracion/8, fa4)
    beep (duracion/8, re5)
    beep (duracion/8, si4)
    beep (duracion/8, fa4)
    beep (duracion/8, re5)
    beep (duracion/8, si4)

def compasCuatro (duracion):
    beep (duracion/8, do5)
    beep (duracion/8, la4)
    beep (duracion/8, fa4)
    beep (duracion/8, do5)
    beep (duracion/8, la4)
    beep (duracion/8, fa4)
    beep (duracion/8, do5)
    beep (duracion/8, la4)

def compasNueve (duracion):
    beep (duracion/4, mi5)
    beep (duracion/48, 0)
    beep (duracion/4, mi5)
    beep (duracion/48, 0)
    beep (duracion/4, mi5)
    beep (duracion/48, 0)
    beep (duracion/8, mi5)
    beep (duracion/8, do5)
    
def compasDiez (duracion):
    beep (duracion/8, re5)
    beep (duracion/4, do5)
    beep (duracion/8, si4)
    beep (duracion/48, 0)
    beep (duracion/4, si4)
    beep (duracion/4, 0)
    
def compasOnce (duracion):
    beep (duracion/4, re5)
    beep (duracion/48, 0)
    beep (duracion/8, re5)
    beep (duracion/48, 0)
    beep (duracion/8, re5)
    beep (duracion/48, 0)
    beep ((duracion/4)*(3/2), re5)
    beep (duracion/48, 0)
    beep (duracion/8, re5)
    
def compasDoce (duracion):
    beep (duracion/8, do5)
    beep (duracion/4, si4)
    beep (duracion/8, la4)
    beep (duracion/48, 0)
    beep (duracion/4, la4)
    beep (duracion/8, fa4)
    beep (duracion/8, mi4)
    
def compasTrece (duracion):
    beep (duracion/4, mi5)
    beep (duracion/48, 0)
    beep (duracion/4, mi5)
    beep (duracion/48, 0)
    beep ((duracion/4)*(3/2), mi5)
    beep (duracion/48, 0)
    beep (duracion/8, mi5)
    
def compasQuince (duracion):
    beep ((duracion/4)*(3/2), re5)
    beep (duracion/48, 0)
    beep (duracion/8, re5)
    beep (duracion/48, 0)
    beep ((duracion/4)*(3/2), re5)
    beep (duracion/8, si4)

def compasDieciseis (duracion):
    beep (duracion/8, do5)
    beep (duracion/4, si4)
    beep (duracion/8, la4)
    beep (duracion/48, 0)
    beep (duracion/4, la4)
    beep (duracion/8, fa4)
    beep (duracion/8, mi4)

def main():
    for repetir in range (0,2) :
        compasUno (tiempo)
        compasDos (tiempo)
        compasDos (tiempo)
        compasCuatro (tiempo)    
    compasNueve (tiempo)
    compasDiez (tiempo)
    compasOnce (tiempo)
    compasDoce (tiempo)
    compasTrece (tiempo)
    compasDiez (tiempo)
    compasQuince (tiempo)
    compasDieciseis (tiempo)
    for repetir in range (0,2) :
        compasUno (tiempo)
        compasDos (tiempo)
        compasDos (tiempo)
        compasCuatro (tiempo)
    
main()