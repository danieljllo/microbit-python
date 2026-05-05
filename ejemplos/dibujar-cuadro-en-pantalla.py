from microbit import *
import sys

milisegundos = 250
intensidad = 9
tamano = 3
inicio_x = 1
inicio_y = 1

if tamano + inicio_x > 5 or tamano + inicio_y > 5:
    print("Error: el tamano maximo de pantalla es 5")
    sys.exit(1)

if intensidad > 9:
    print("Error: intensidad maxima es 9")
    sys.exit(2)

# Code in a 'while True:' loop repeats forever
while True:
    display.clear()
    sleep(milisegundos * 2)
    
    for i in range(tamano - 1):
        display.set_pixel(i + inicio_x, 0 + inicio_y, intensidad)
        sleep(milisegundos)
    
    for i in range(tamano - 1):
        display.set_pixel(tamano - 1 + inicio_x, i + inicio_y, intensidad)
        sleep(milisegundos)

    for i in range(tamano - 1, 0, -1):
        display.set_pixel(i + inicio_x, tamano - 1 + inicio_y, intensidad)
        sleep(milisegundos)

    for i in range(tamano - 1, 0, -1):
        display.set_pixel(0 + inicio_x, i + inicio_y, intensidad)
        sleep(milisegundos) 
