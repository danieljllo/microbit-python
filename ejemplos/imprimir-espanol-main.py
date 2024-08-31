# Mostar texto en Español
# Autor: Daniel Jaramillo

# Este programa demuestra como mostrar en la pantalla del micro:bit caracteres en español
# como la letra eñe o las vocales con tilde.

# El programa solo incluye algunas letras de ejemplo para que el estudiante implemente las
# letras faltantes.

from microbit import *

class DisplayEspannol():

    @staticmethod
    def show(texto):
        for letra in texto:
            if letra is 'ñ':
                display.show(Image('99990:'
                                   '00000:'
                                   '99900:'
                                   '90090:'
                                   '90090'))
            elif letra is 'á':
                display.show(Image('00090:'
                                   '09900:'
                                   '90090:'
                                   '99990:'
                                   '90090'))
            elif letra is 'ó':
                display.show(Image('00090:'
                                   '09900:'
                                   '90090:'
                                   '90090:'
                                   '09900'))
            else:
                display.show(letra)
            sleep(1000)
                
DisplayEspannol.show("Cañón")
display.clear()
sleep(2000)
DisplayEspannol.show("Bañándose")
