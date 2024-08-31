# Combinar pines en forma binaria para ejecutar hasta 8 acciones
# Autor: Daniel Jaramillo

# Este programa demuestra como combinar los 3 pines de proposito general P0, P1 y P2
# para formar un valor usando el sistema binario y obtener 8 estados diferentes.

# P2 | P1 | P0 | Estado | Accion
# ---+----+----+--------+-------
#  0 |  0 |  0 |   0    | Silencio
#  0 |  0 |  1 |   1    | Tocar nota C
#  0 |  1 |  0 |   2    | Tocar nota D
#  0 |  1 |  1 |   3    | Tocar nota E
#  1 |  0 |  0 |   4    | Tocar nota F
#  1 |  0 |  1 |   5    | Tocar nota G
#  1 |  1 |  0 |   6    | Tocar nota A
#  1 |  1 |  1 |   7    | Tocar nota B

# Este programa se puede probar en el simulador (https://python.microbit.org/v/3/reference) 
# usando la opcion avanzada de los pines que permite 'Mantener pulsado' uno o varios pines.

from microbit import *
import music

while True:
    valor = 0
    if pin0.is_touched():
        valor += 1
    if pin1.is_touched():
        valor += 2
    if pin2.is_touched():
        valor += 4
    
    display.show(valor)

    if valor == 0:
        pass
    elif valor == 1:
        music.play('c')
    elif valor == 2:
        music.play('d')
    elif valor == 3:
        music.play('e')
    elif valor == 4:
        music.play('f')
    elif valor == 5:
        music.play('g')
    elif valor == 6:
        music.play('a')
    elif valor == 7:
        music.play('b')
    else:
        display.clear()
    
    sleep(500)