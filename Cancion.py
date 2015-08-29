#encoding: UTF-8
# Armando Tapia Campos A01169413
# Tarea de cacion con funciones

from Myro import*

do6 = 1046.502
re6 = 1174.659
mi6 = 1318.51
fa6 = 1396.931
sol6 = 1567.982
la6 = 1760
sol5 = 783.991

def compasUno(duracion):
    beep(duracion, do6)
    beep(duracion, re6)
    beep(duracion, mi6)
    beep(duracion, do6)
    beep(duracion/5, 0)
    
def compasDos(duracion):
    beep(duracion, mi6)
    beep(duracion, fa6)
    beep(duracion, sol6)
    beep(duracion, 0)

def compasTres(duracion):
    beep(duracion/1.5, sol6)
    beep(duracion/1.5, la6) 
    beep(duracion/1.5, sol6)
    beep(duracion/1.5, fa6)
    beep(duracion, mi6)
    beep(duracion/1.5, do6)
    beep(duracion, 0)
    
def compasCuatro(duracion):
    beep(duracion, do6)
    beep(duracion, sol5)
    beep(duracion, do6)
    beep(duracion, 0)
    
tiempo = float(input("que tan rapido quieres que toque"))

def main():
    compasUno(tiempo)
    compasUno(tiempo)
    compasDos(tiempo)
    compasDos(tiempo)
    compasTres(tiempo)
    compasTres(tiempo)
    compasCuatro(tiempo)
    compasCuatro(tiempo)
    
main()            
    
    