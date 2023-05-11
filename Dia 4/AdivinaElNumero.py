from random import *

intentos = 8
numero = randint(1, 100)
print("Cual es tu nombre?")
nombre = input()
print(f"Hola {nombre} vamos a jugar a un juego, voy a pensar un numero del 1 al 100 y tienes que adivinar cual es, solo tienes 8 intentos")


while intentos > 0:
    respuesta = input()

    if int(respuesta) == numero:
        print(f"Correcto el numero era {numero}, solo te quedaban {intentos} !!")
    elif int(respuesta) > numero:
        print(f"El numero que estoy pensando es mas pequeño que {respuesta}")
    elif int(respuesta) < numero:
        print(f"El numero que estoy pensando es mas grande que {respuesta}")
    else:
        print("Incorrecto")
    intentos -= 1

if intentos == 0 and not int(respuesta) == numero:
    print("Perdiste!!")