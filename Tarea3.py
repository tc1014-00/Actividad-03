# encoding: UTF-8
# Autor: Humberto Serra Mendieta
# Funciones para reproducir musica

from Myro import*

do=523.251
sol=783.991
la=880
fa=698.456
mi=659.255
re=587.33

def reproducirCompas(tempo): 
    beep(tempo,do)
    beep(tempo,0)
    beep(tempo,do)
    beep(tempo,0)
    beep(tempo,sol)
    beep(tempo,0)
    beep(tempo,sol)
    beep(tempo,0)
    beep(tempo,la)
    beep(tempo,0)
    beep(tempo,la)
    beep(tempo,0)
    beep(tempo*2,sol)
    beep(tempo,0)
    beep(tempo,fa)
    beep(tempo,0)
    beep(tempo,fa)
    beep(tempo,0)
    beep(tempo,mi)
    beep(tempo,0)
    beep(tempo,mi)
    beep(tempo,0)
    beep(tempo,re)
    beep(tempo,0)
    beep(tempo,re)
    beep(tempo,0)
    beep(tempo*2,do)
    
tiempo=0.2
reproducirCompas(tiempo)