#encoding: UTF-8
#Brian Saggiante Parra A01377511
#Funciones para reproducir musica (Be Yourself-Audioslave)

from Myro import*

DOs=277     #DO sostenido
RE=293
MI=329
FAs=185     #FA sostenido
FAs2=369
LA=220
SI=246
d=1.5
d2=0.1
d3=1
d4=0.3

def compasUno(duracion):
    beep(d,RE)
    beep(d2,DOs)
    beep(d2,RE)
    beep(d3,DOs)
    beep(d4,FAs)
    beep(d4,LA)
    beep(d4,SI)
    beep(d4,RE)
    beep(d4,MI)
    beep(d,FAs2)
    
compasUno(d)

def compasDos(duracion):
    beep(d,RE)
    beep(d2,DOs)
    beep(d2,RE)
    beep(d3,DOs)
    beep(d4,FAs)
    beep(d4,LA)
    beep(d4,SI)
    beep(d4,RE)
    beep(d4,MI)
    beep(d,FAs2)
    
compasDos(d)

DOs=554
RE=587
MI=659
FAs=369
LA=440
SI=493
t=1.5
t2=1
t3=0.5
t4=0.3

def compasTres(tiempo):
    beep(t,SI)
    beep(t4,FAs)
    beep(t,LA)
    beep(t3,DOs)
    beep(t,RE)
    beep(t3,MI)
    beep(t2,DOs)
    beep(t3,RE)
    beep(t3,LA)
    beep(t,SI)
    
compasTres(t)

def compasCuatro(tiempo):
    beep(t4,FAs)
    beep(t,LA)
    beep(t3,DOs)
    beep(t,RE)
    beep(t3,DOs)
    beep(t2,LA)
    beep(t3,FAs)
    beep(t3,DOs)
    beep(t,SI)
    
compasCuatro(t)
