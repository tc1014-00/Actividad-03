#encoding: UTF-8
#Autor: Hector Manuel Takami Flores
#Lector de partituras: Titanic

Fa=698.45
Sol=783.99
La=880
Do1=1046.5
LaS=932.3
Re=587.3
Mi=656.25
Do=523.25
Re1=1174.65

from Myro import*
def introCancion(duracion):
    beep(duracion,Fa)
    beep(duracion,Sol)
    beep(duracion,Sol)
    beep(duracion*4,La)
    beep(duracion/2,0)
    
    beep(duracion/2,Sol)
    beep(duracion/2,La)
    beep(duracion/2,Sol)
    beep(duracion/2,Fa)
    beep(duracion/2,Sol)
    beep(duracion*4,Do1)
    
    beep(duracion/2,0)
    beep(duracion,LaS)
    beep(duracion,La)
    beep(duracion*2,Fa)
    beep(duracion*2,Re)
    beep(duracion*4,Do)
    beep(duracion*2,Fa)
    beep(duracion,0)
    
    beep(duracion,Mi) 
    beep(duracion,Sol)
    beep(duracion,Sol)
    beep(duracion*4,La)
    
    beep(duracion,LaS)
    beep(duracion,La)
    beep(duracion/2,Sol)
    beep(duracion/2,Fa)
    beep(duracion/2,Sol)
    beep(duracion*4,Do1)
    beep(duracion/2,0)
    
    beep(duracion,La)
    beep(duracion*2,Do1)
    beep(duracion*3,Re1)
    beep(duracion*2,Do1)
    beep(duracion*4,Sol)
    beep(duracion*2,0)
    
def estrofa(duracion):
    beep(duracion*1.3,Fa) 
   # beep(duracion/4,0) 
    beep(duracion*1.2,Fa)
   # beep(duracion/8,0)
    beep(duracion*1.3,Fa)
   # beep(duracion/4,0)
    beep(duracion*1.5,Fa)
   # beep(duracion/8,0)
    beep(duracion,Mi)
    beep(duracion*2,Fa) 
    beep(duracion,0) 
    
    beep(duracion,Fa)
    beep(duracion,Mi)
    beep(duracion,Fa)
    beep(duracion/2,0)
    
    beep(duracion*2,Sol)
    beep(duracion,La)
    beep(duracion/2,LaS)
    beep(duracion/2,La)
    beep(duracion*2,Sol)
    beep(duracion*2,0)
    
    beep(duracion*1.3,Fa)
   # beep(duracion/2,0)  
    beep(duracion*1.2,Fa)
   # beep(duracion/4,0)
    beep(duracion*1.3,Fa)
   # beep(duracion/8,0)
    beep(duracion*1.5,Fa)
   # beep(duracion/8,0)
    beep(duracion,Mi)
    beep(duracion*2,Fa) 
    beep(duracion,0) 
    
    beep(duracion*2,Fa)
    beep(duracion*4,Do)
    
def Coro(duracion):
    beep(duracion*4,Fa)
    beep(duracion*6,Sol)
    
    beep(duracion,Do)
    beep(duracion*4,Do1)
    beep(duracion*1.5,LaS)
    beep(duracion*1.5,La)
    beep(duracion*2,Sol)
    beep(duracion,0)
    
    beep(duracion,La)
    beep(duracion*1.5,LaS)
    beep(duracion*2,La)
    beep(duracion/2,0)
    
    beep(duracion,Sol)
    beep(duracion*1.5,Fa)
    beep(duracion*1.5,Mi)
    beep(duracion*2,Fa)
    beep(duracion,0)
    
    beep(duracion*2,Mi)
    beep(duracion*4,Re)
    beep(duracion*4,Do)
    beep(duracion*2,Re)
    beep(duracion*4,Mi)
    beep(duracion,0)
    
    beep(duracion*5,Fa)
    beep(duracion*6,Sol)
    
    beep(duracion,Do)
    beep(duracion*4,Do1)
    beep(duracion*1.5,LaS)
    beep(duracion*1.5,La)
    beep(duracion*2,Sol)
    beep(duracion,0)
    
    beep(duracion,La)
    beep(duracion,LaS)
    beep(duracion*2,La)
    beep(duracion/2,0)
    
    beep(duracion,Sol)
    beep(duracion,Fa)
    beep(duracion,Mi)
    beep(duracion*2,Fa)
    beep(duracion,0)
    
    beep(duracion,Mi)
    beep(duracion,Mi)
    beep(duracion*2,Fa)
    beep(duracion,0)
    
    beep(duracion*2,Sol)
    beep(duracion*1.5,La)
    beep(duracion/2,LaS)
    beep(duracion/2,La)
    beep(duracion,Sol)
    
    beep(duracion*2,Fa)
    beep(duracion*8,Fa)
    beep(duracion*2,0)



    
time = 0.4    
introCancion(time)
estrofa(time)
estrofa(time)
Coro(time)
introCancion(time)




"""Do  5:  523.251     
Do# 5:  554.365     
Re  5:  587.33      
Re# 5:  622.254     
Mi  5:  659.255     
Fa  5:  698.456     
Fa# 5:  739.989     
Sol 5:  783.991     
Sol#5:  830.609     
La  5:  880     
La# 5:  932.328     
Si  5:  987.767 
Do  6:  1046.502        
Do# 6:  1108.731        
Re  6:  1174.659        
Re# 6:  1244.508        
Mi  6:  1318.51     
Fa  6:  1396.913        
Fa# 6:  1479.978        
Sol 6:  1567.982        
Sol#6:  1661.219        
La  6:  1760        
La# 6:  1864.655        
Si  6:  1975.533        
Do  7:  2093.005        
Do# 7:  2217.461        
Re  7:  2349.318        
Re# 7:  2489.016        
Mi  7:  2637.02     
Fa  7:  2793.826        
Fa# 7:  2959.955        
Sol 7:  3135.963        
Sol#7:  3322.438        
La  7:  3520        
La# 7:  3729.31     
Si  7:  3951.066"""