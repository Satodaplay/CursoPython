

print("Ingrese su texto:")
texto = input()
print("Ahora ingrsea una letra que quieras saber cuantas veces aparece en el texto")
a = input()
lista = texto.split(" ")
print("El numero de palabras en el texto de de: ", len(lista))
print("El primera caracter del texto es: ", texto[0])
print("El ultimo caracter del texto es: ", texto[-1])
print("El numero de veces que se ha repetido la letra ", a, "es de: " , texto.count(a))