#Actividad-03

###Tarea 3. Haciendo música con el robot Scribbler.

Escribe un programa que reproduzca una melodía sencilla (entre 10 y 20 compases está bien).
Cada compas debe reproducirse con una función que recibe como parámetro la duración de la nota negra.

SUGERENCIA:
Declara al inicio del programa la frecuencia de las notas que vas a reproducir para que sea más sencillo codificar tu melodía.

Ejemplo:
```
#encoding: UTF-8
# Autor: Roberto Mtz. Román
# Funciones para reproducir música

from Myro import *
# Declara las notas que vas a usar
MI = 659
RE = 587
DO = 523

#Primer compás (USA LAS VARIABLES DECLARADAS ARRIBA)
def reproducirCompasUno(duracion) :
    beep(duracion,MI)
    beep(duracion,RE)
    beep(duracion,DO)
    beep(duracion,RE)

# Llamas a cada función
tiempo = 0.25
reproducirCompasUno(tiempo)
```
Escribe tu programa y agrégalo al repositorio en github. Agrega también la partitura de la melodía que estás codificando.
