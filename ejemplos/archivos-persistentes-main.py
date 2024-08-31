# Almacenar archivos en el micro:bit que persisten cuando se reinicia
# Autor: Daniel Jaramillo

# Este programa demuestra que se pueden almacenar archivos en el micro:bit
# los cuales persisten cuando el micro:bit se reinicia.

# El programa inspecciona si archivo.txt existe:
#  - Si no existe, se crea archivo.txt el cual contiene el valor '1'
#  - Si existe, se lee el valor almacenado en archivo.txt, y se aumenta

# Este programa se puede probar en el simulador (https://python.microbit.org/v/3/reference) 
# usando el botón que permite reiniciar la ejecución (boton con flechas en círculo debajo del pin 2).

from microbit import *
import os

nombre_archivo = "archivo.txt"

lista_archivos = os.listdir()
print("Lista archivos inicial: ")
print(lista_archivos)

valor = 1
if nombre_archivo in lista_archivos:
    with open(nombre_archivo, 'r') as archivo:
        valor = int(archivo.read())
        valor += 1
        
with open(nombre_archivo, 'w') as archivo:
    archivo.write(str(valor))

lista_archivos = os.listdir()
print("Lista archivos final: ")
print(lista_archivos)

while True:
    display.show(valor)
    sleep(500)
    display.clear()
    sleep(500)
